# 🎓 EXERCICE 1 - TESTS FONCTIONNELS SELENIUM
## Plateforme de Gestion des Réclamations - IBAM

---

## 📦 LIVRABLE COMPLET

```
tests_selenium/
│
├── 📄 INDEX.md                      ← 🎯 COMMENCEZ ICI !
├── 📄 EXERCICE_RESUME.md            ← Vue d'ensemble de l'exercice
├── 📄 README.md                     ← Guide d'utilisation
├── 📄 GUIDE_EXPLICATION_CODE.md     ← Explications détaillées
├── 📄 IMPLEMENTATION_BLOCAGE.md     ← Guide backend
│
├── 🧪 test_auth_reussie.py         ← Test 1: Authentification réussie
├── 🧪 test_auth_echouee.py         ← Test 2: Authentification échouée
├── 🧪 test_suite.py                 ← Suite complète
├── 🧪 demo_avec_screenshots.py      ← Démonstration visuelle
│
├── ⚙️  config.py                     ← Configuration
└── 📦 requirements.txt              ← Dépendances Python
```

**Total : 11 fichiers | ~75 Ko de documentation et code**

---

## 🎯 OBJECTIFS DE L'EXERCICE

### Test 1 : Authentification Réussie ✅

```
┌──────────────────────────────────────────────────────────────┐
│  SCÉNARIO : Utilisateur se connecte avec succès              │
└──────────────────────────────────────────────────────────────┘

   Utilisateur                    Système
       │                             │
       │  1. Ouvre /login            │
       ├────────────────────────────>│
       │                             │
       │  2. Affiche formulaire      │
       │<────────────────────────────┤
       │                             │
       │  3. Saisit identifiants     │
       │     (valides)               │
       ├────────────────────────────>│
       │                             │
       │  4. Vérifie & redirige      │
       │     vers /dashboard         │
       │<────────────────────────────┤
       │                             │
       │  5. Clique "Déconnexion"    │
       ├────────────────────────────>│
       │                             │
       │  6. Redirige vers /login    │
       │<────────────────────────────┤
       │                             │

✅ RÉSULTAT : Connexion et déconnexion réussies
```

### Test 2 : Authentification Échouée ❌

```
┌──────────────────────────────────────────────────────────────┐
│  SCÉNARIO : Blocage après 3 tentatives échouées              │
└──────────────────────────────────────────────────────────────┘

   Utilisateur                    Système
       │                             │
       │  1. Tentative 1 (invalide)  │
       ├────────────────────────────>│
       │                             │
       │  ⚠️  "Erreur 1/3"            │
       │  📝 Échec enregistré         │
       │<────────────────────────────┤
       │                             │
       │  2. Tentative 2 (invalide)  │
       ├────────────────────────────>│
       │                             │
       │  ⚠️  "Erreur 2/3"            │
       │  📝 Échec enregistré         │
       │<────────────────────────────┤
       │                             │
       │  3. Tentative 3 (invalide)  │
       ├────────────────────────────>│
       │                             │
       │  🔒 "Compte bloqué"          │
       │  🚫 Compte désactivé         │
       │<────────────────────────────┤
       │                             │
       │  4. Tentative (valide)      │
       ├────────────────────────────>│
       │                             │
       │  🔒 "Toujours bloqué"        │
       │<────────────────────────────┤
       │                             │

✅ RÉSULTAT : Compte bloqué après 3 tentatives
```

---

## 🚀 DÉMARRAGE RAPIDE (3 MINUTES)

### Étape 1 : Installation (1 min)

```bash
cd tests_selenium
pip install -r requirements.txt
```

### Étape 2 : Configuration (30 sec)

Éditez `config.py` :
```python
VALID_PHONE = "0612345678"      # Votre utilisateur
VALID_PASSWORD = "password123"   # Votre mot de passe
```

### Étape 3 : Exécution (1 min 30)

```bash
# Test 1
python test_auth_reussie.py

# Test 2
python test_auth_echouee.py

# Tous les tests
pytest -v --html=rapport_tests.html
```

---

## 📊 ARCHITECTURE DES TESTS

```
┌─────────────────────────────────────────────────────────────┐
│                    ARCHITECTURE SELENIUM                     │
└─────────────────────────────────────────────────────────────┘

┌──────────────┐
│   Python     │  Langage de programmation
└──────┬───────┘
       │
┌──────▼───────┐
│   Selenium   │  Framework de test web
└──────┬───────┘
       │
┌──────▼───────┐
│ ChromeDriver │  Pilote du navigateur
└──────┬───────┘
       │
┌──────▼───────┐
│   Chrome     │  Navigateur web
└──────┬───────┘
       │
┌──────▼───────┐
│ Application  │  http://localhost:3000
└──────────────┘
```

---

## 🔧 COMPOSANTS TECHNIQUES

### 1. WebDriver (Contrôleur)

```python
driver = webdriver.Chrome()
driver.get("http://localhost:3000/login")
```

**Rôle** : Contrôle le navigateur comme un utilisateur réel

### 2. Sélecteurs (Recherche)

```python
element = driver.find_element(By.NAME, "email")
```

**Rôle** : Trouve les éléments dans la page HTML

### 3. Actions (Interaction)

```python
element.send_keys("test@example.com")
button.click()
```

**Rôle** : Simule les actions utilisateur (saisie, clic)

### 4. Assertions (Vérification)

```python
assert "dashboard" in driver.current_url
```

**Rôle** : Vérifie que le résultat est correct

---

## 📸 CAPTURES D'ÉCRAN AUTOMATIQUES

Le script `demo_avec_screenshots.py` génère :

```
screenshots/
├── 01_page_connexion.png          ← Page de login
├── 02_formulaire_vide.png         ← Formulaire vide
├── 03_formulaire_rempli.png       ← Formulaire rempli
├── 04_apres_soumission.png        ← Après clic
├── 05_connexion_reussie.png       ← Dashboard
├── 06_tentative_1_resultat.png    ← Erreur 1/3
├── 07_tentative_2_resultat.png    ← Erreur 2/3
├── 08_tentative_3_resultat.png    ← Compte bloqué
└── 09_resultat_apres_blocage.png  ← Toujours bloqué
```

---

## 📈 RAPPORT DE TESTS

Après exécution avec pytest :

```
rapport_tests.html
├── Résumé des tests
│   ├── ✅ Tests réussis : 2/2
│   ├── ❌ Tests échoués : 0/2
│   └── ⏱️  Temps total : 45s
│
├── Détails par test
│   ├── test_authentification_reussie
│   │   ├── Statut : ✅ PASSED
│   │   ├── Durée : 20s
│   │   └── Logs : [voir détails]
│   │
│   └── test_authentification_echouee
│       ├── Statut : ✅ PASSED
│       ├── Durée : 25s
│       └── Logs : [voir détails]
│
└── Captures d'écran (si échec)
```

---

## 🎓 CONCEPTS SELENIUM EXPLIQUÉS

### Exemple Commenté

```python
# 1. INITIALISATION
driver = webdriver.Chrome()              # Ouvre Chrome
driver.maximize_window()                 # Plein écran
driver.implicitly_wait(10)               # Attend 10s max

# 2. NAVIGATION
driver.get("http://localhost:3000/login") # Va sur la page

# 3. RECHERCHE D'ÉLÉMENTS
email = driver.find_element(By.NAME, "email")     # Trouve le champ
password = driver.find_element(By.NAME, "password") # Trouve le champ
button = driver.find_element(By.XPATH, "//button[@type='submit']")

# 4. INTERACTION
email.send_keys("test@example.com")      # Tape l'email
password.send_keys("password123")        # Tape le mot de passe
button.click()                           # Clique sur le bouton

# 5. ATTENTE
time.sleep(2)                            # Attend 2 secondes

# 6. VÉRIFICATION
assert "dashboard" in driver.current_url # Vérifie l'URL

# 7. NETTOYAGE
driver.quit()                            # Ferme le navigateur
```

---

## 🔒 IMPLÉMENTATION BACKEND

Pour que les tests fonctionnent, le backend doit :

### 1. Ajouter les champs dans la BDD

```sql
ALTER TABLE users ADD COLUMN login_attempts INT DEFAULT 0;
ALTER TABLE users ADD COLUMN account_locked BOOLEAN DEFAULT FALSE;
ALTER TABLE users ADD COLUMN locked_at TIMESTAMP NULL;
```

### 2. Modifier le contrôleur d'authentification

```php
// Incrémenter les tentatives
$user->login_attempts += 1;

// Bloquer après 3 tentatives
if ($user->login_attempts >= 3) {
    $user->account_locked = true;
    return response()->json(['message' => 'Compte bloqué'], 403);
}

// Réinitialiser après succès
$user->login_attempts = 0;
```

**Voir `IMPLEMENTATION_BLOCAGE.md` pour le code complet**

---

## ✅ CHECKLIST DE VALIDATION

### Avant l'exécution

- [ ] Python 3.8+ installé
- [ ] Chrome installé
- [ ] `pip install -r requirements.txt`
- [ ] Backend lancé (port 8000)
- [ ] Frontend lancé (port 3000)
- [ ] Utilisateur de test créé

### Pendant l'exécution

- [ ] Le navigateur s'ouvre automatiquement
- [ ] Les actions sont visibles à l'écran
- [ ] Les logs s'affichent dans la console
- [ ] Aucune erreur n'apparaît

### Après l'exécution

- [ ] Tests passent (✅ PASSED)
- [ ] Captures d'écran générées
- [ ] Rapport HTML créé
- [ ] Navigateur fermé proprement

---

## 📚 DOCUMENTATION FOURNIE

| Fichier | Pages | Contenu |
|---------|-------|---------|
| INDEX.md | 1 | Navigation et vue d'ensemble |
| EXERCICE_RESUME.md | 2 | Résumé de l'exercice |
| README.md | 3 | Guide d'utilisation |
| GUIDE_EXPLICATION_CODE.md | 8 | Explications détaillées |
| IMPLEMENTATION_BLOCAGE.md | 4 | Guide backend |
| **TOTAL** | **18 pages** | **Documentation complète** |

---

## 🎯 COMPÉTENCES ACQUISES

Après cet exercice, vous maîtrisez :

✅ **Selenium WebDriver**
- Initialisation du navigateur
- Navigation web automatisée
- Recherche d'éléments (By.NAME, By.XPATH, etc.)

✅ **Interactions Web**
- Saisie de texte (send_keys)
- Clics (click)
- Vérification d'URL

✅ **Gestion des Attentes**
- Attentes implicites
- Attentes explicites (WebDriverWait)
- Conditions d'attente (EC)

✅ **Tests Fonctionnels**
- Structure d'un test (setup/test/teardown)
- Assertions
- Gestion des erreurs

✅ **Automatisation**
- Captures d'écran automatiques
- Génération de rapports
- Exécution en batch

---

## 🏆 RÉSULTAT FINAL

```
┌─────────────────────────────────────────────────────────────┐
│                    LIVRABLE COMPLET                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ✅ 2 Tests fonctionnels complets                           │
│  ✅ 18 pages de documentation                               │
│  ✅ Code commenté et expliqué                               │
│  ✅ Guide d'implémentation backend                          │
│  ✅ Démonstration avec captures d'écran                     │
│  ✅ Génération de rapports HTML                             │
│  ✅ Configuration personnalisable                           │
│                                                              │
│  🎓 Prêt pour présentation et évaluation                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 COMMANDES ESSENTIELLES

```bash
# Installation
pip install -r requirements.txt

# Test individuel
python test_auth_reussie.py
python test_auth_echouee.py

# Tous les tests
pytest -v

# Avec rapport HTML
pytest -v --html=rapport_tests.html --self-contained-html

# Démonstration
python demo_avec_screenshots.py
```

---

## 📞 AIDE

| Problème | Solution |
|----------|----------|
| Element not found | Augmenter les temps d'attente dans `config.py` |
| ChromeDriver error | `pip install --upgrade webdriver-manager` |
| Connection refused | Vérifier que l'app tourne sur localhost:3000 |
| Code incompréhensible | Lire `GUIDE_EXPLICATION_CODE.md` |

---

## 🎉 FÉLICITATIONS !

Vous disposez maintenant d'une suite de tests complète et professionnelle pour votre plateforme de gestion des réclamations.

**Bon courage pour votre présentation ! 💪🚀**

---

*Développé avec ❤️ pour l'IBAM*  
*Tests Fonctionnels Selenium - Python*  
*Exercice 1 : Authentification*
