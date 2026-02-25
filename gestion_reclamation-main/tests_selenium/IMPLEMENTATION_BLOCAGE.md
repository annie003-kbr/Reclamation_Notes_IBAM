# 🔒 Implémentation du Système de Blocage après 3 Tentatives

Ce document explique comment implémenter le système de blocage de compte après 3 tentatives de connexion échouées dans le backend Laravel.

## 📋 Étapes d'Implémentation

### 1. Créer la Migration pour Ajouter les Champs

```bash
cd backend
php artisan make:migration add_login_attempts_to_users_table
```

Modifier le fichier de migration créé :

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('users', function (Blueprint $table) {
            $table->integer('login_attempts')->default(0)->after('password');
            $table->boolean('account_locked')->default(false)->after('login_attempts');
            $table->timestamp('locked_at')->nullable()->after('account_locked');
        });
    }

    public function down(): void
    {
        Schema::table('users', function (Blueprint $table) {
            $table->dropColumn(['login_attempts', 'account_locked', 'locked_at']);
        });
    }
};
```

Exécuter la migration :

```bash
php artisan migrate
```

### 2. Modifier le Modèle User

Ajouter les champs dans `app/Models/User.php` :

```php
protected $fillable = [
    'name',
    'email',
    'password',
    'role_id',
    'filiere_id',
    'login_attempts',      // Nouveau
    'account_locked',      // Nouveau
    'locked_at',           // Nouveau
];

protected $casts = [
    'email_verified_at' => 'datetime',
    'password' => 'hashed',
    'account_locked' => 'boolean',    // Nouveau
    'locked_at' => 'datetime',        // Nouveau
];
```

### 3. Modifier le Contrôleur d'Authentification

Remplacer la méthode `login` dans `app/Http/Controllers/AuthController.php` :

```php
public function login(Request $request)
{
    $request->validate([
        'email' => 'required|string|email',
        'password' => 'required|string',
        'role_name' => 'required|string|exists:roles,name',
    ]);

    // Rechercher l'utilisateur par email
    $user = User::where('email', $request->email)->first();

    // Vérifier si le compte est bloqué
    if ($user && $user->account_locked) {
        return response()->json([
            'message' => 'Votre compte a été bloqué après 3 tentatives de connexion échouées. Veuillez contacter l\'administrateur.',
            'locked' => true
        ], 403);
    }

    // Tentative de connexion
    if (!Auth::attempt($request->only('email', 'password'))) {
        
        // Incrémenter le compteur de tentatives
        if ($user) {
            $user->login_attempts += 1;
            
            // Bloquer le compte après 3 tentatives
            if ($user->login_attempts >= 3) {
                $user->account_locked = true;
                $user->locked_at = now();
                $user->save();
                
                return response()->json([
                    'message' => 'Votre compte a été bloqué après 3 tentatives de connexion échouées. Veuillez contacter l\'administrateur.',
                    'locked' => true,
                    'attempts' => $user->login_attempts
                ], 403);
            }
            
            $user->save();
            
            return response()->json([
                'message' => "Identifiants incorrects. Tentative {$user->login_attempts}/3",
                'attempts' => $user->login_attempts
            ], 401);
        }
        
        return response()->json([
            'message' => 'Identifiants incorrects',
        ], 401);
    }

    $user = Auth::user();

    // Vérifier le rôle
    if ($user->role->name !== $request->role_name) {
        // Incrémenter aussi pour mauvais rôle
        $user->login_attempts += 1;
        
        if ($user->login_attempts >= 3) {
            $user->account_locked = true;
            $user->locked_at = now();
            $user->save();
            
            return response()->json([
                'message' => 'Votre compte a été bloqué après 3 tentatives de connexion échouées.',
                'locked' => true
            ], 403);
        }
        
        $user->save();
        
        return response()->json([
            'message' => "Rôle invalide. Tentative {$user->login_attempts}/3",
            'attempts' => $user->login_attempts
        ], 401);
    }

    // Connexion réussie : Réinitialiser le compteur
    $user->login_attempts = 0;
    $user->save();

    $token = $user->createToken('auth_token')->plainTextToken;

    return response()->json([
        'user' => $user->load('role', 'filiere'),
        'token' => $token,
    ]);
}
```

### 4. Ajouter une Route pour Débloquer un Compte (Admin)

Dans `routes/api.php`, ajouter :

```php
Route::middleware('auth:sanctum')->group(function () {
    // ... autres routes
    
    // Route pour débloquer un compte (réservée aux admins)
    Route::post('users/{id}/unlock', [UserController::class, 'unlockAccount']);
});
```

Dans `app/Http/Controllers/UserController.php`, ajouter :

```php
public function unlockAccount($id)
{
    $user = User::findOrFail($id);
    
    $user->account_locked = false;
    $user->login_attempts = 0;
    $user->locked_at = null;
    $user->save();
    
    return response()->json([
        'message' => 'Compte débloqué avec succès',
        'user' => $user
    ]);
}
```

## 🎨 Adaptation du Frontend

### Afficher les Messages d'Erreur

Dans votre composant de connexion React/TypeScript, gérer les réponses :

```typescript
const handleLogin = async (data: LoginFormData) => {
  try {
    const response = await axios.post('/api/login', data);
    // Connexion réussie
    setToken(response.data.token);
    navigate('/dashboard');
  } catch (error: any) {
    if (error.response?.status === 403) {
      // Compte bloqué
      setError('Votre compte a été bloqué après 3 tentatives échouées. Contactez l\'administrateur.');
    } else if (error.response?.status === 401) {
      // Identifiants incorrects
      const attempts = error.response?.data?.attempts || 0;
      setError(`Identifiants incorrects. Tentative ${attempts}/3`);
    } else {
      setError('Erreur de connexion');
    }
  }
};
```

## 🧪 Tester l'Implémentation

### 1. Créer un utilisateur de test

```sql
INSERT INTO users (name, email, password, role_id, login_attempts, account_locked) 
VALUES ('Test User', 'test@example.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 1, 0, false);
-- Mot de passe : password
```

### 2. Tester manuellement

```bash
# Tentative 1 (échec)
curl -X POST http://localhost:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"wrong","role_name":"etudiant"}'

# Tentative 2 (échec)
curl -X POST http://localhost:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"wrong","role_name":"etudiant"}'

# Tentative 3 (échec + blocage)
curl -X POST http://localhost:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"wrong","role_name":"etudiant"}'

# Tentative 4 (même avec bon mot de passe, compte bloqué)
curl -X POST http://localhost:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password","role_name":"etudiant"}'
```

### 3. Exécuter les tests Selenium

```bash
cd tests_selenium
python test_auth_echouee.py
```

## 📊 Vérification en Base de Données

```sql
-- Voir les tentatives de connexion
SELECT id, name, email, login_attempts, account_locked, locked_at 
FROM users 
WHERE email = 'test@example.com';

-- Débloquer manuellement un compte
UPDATE users 
SET account_locked = false, login_attempts = 0, locked_at = NULL 
WHERE email = 'test@example.com';
```

## 🔄 Améliorations Possibles

### 1. Déblocage Automatique après X heures

```php
// Dans la méthode login, avant de vérifier le blocage
if ($user && $user->account_locked && $user->locked_at) {
    $hoursSinceLock = now()->diffInHours($user->locked_at);
    
    if ($hoursSinceLock >= 24) {
        // Débloquer automatiquement après 24h
        $user->account_locked = false;
        $user->login_attempts = 0;
        $user->locked_at = null;
        $user->save();
    }
}
```

### 2. Notification par Email lors du Blocage

```php
use App\Mail\AccountLocked;
use Illuminate\Support\Facades\Mail;

// Après avoir bloqué le compte
Mail::to($user)->send(new AccountLocked($user));
```

### 3. Logs de Sécurité

```php
use Illuminate\Support\Facades\Log;

// Enregistrer chaque tentative échouée
Log::warning('Failed login attempt', [
    'email' => $request->email,
    'ip' => $request->ip(),
    'attempts' => $user->login_attempts
]);
```

## ✅ Checklist d'Implémentation

- [ ] Migration créée et exécutée
- [ ] Modèle User mis à jour
- [ ] Contrôleur AuthController modifié
- [ ] Frontend adapté pour afficher les messages
- [ ] Tests manuels effectués
- [ ] Tests Selenium exécutés avec succès
- [ ] Documentation mise à jour

## 🎓 Résumé

Ce système de sécurité :
1. ✅ Compte les tentatives de connexion échouées
2. ✅ Bloque le compte après 3 tentatives
3. ✅ Empêche toute connexion même avec bons identifiants
4. ✅ Permet aux admins de débloquer les comptes
5. ✅ Réinitialise le compteur après connexion réussie
