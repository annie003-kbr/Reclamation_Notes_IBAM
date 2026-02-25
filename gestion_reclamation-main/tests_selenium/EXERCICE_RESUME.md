# 🎯 EXERCICE 1 : Tests Fonctionnels d'Authentification

## 📋 Résumé de l'Exercice

Vous avez maintenant un ensemble complet de tests fonctionnels Selenium pour votre plateforme de gestion des réclamations.

---

## 📁 Fichiers Créés

```
tests_selenium/
├── 📄 requirements.txt              # Dépendances Python
├── 📄 config.py                     # Configuration des tests
├── 📄 test_auth_reussie.py         # Test 1: Authentification réussie
├── 📄 test_auth_echouee.py         # Test 2: Authentification échouée (3 tentatives)
├── 📄 test_suite.py                 # Suite complète de tests
├── 📄 demo_avec_screenshots.py      # Démonstration avec captures d'écran
├── 📄 README.md                     # Documentation d'utilisation
├── 📄 GUIDE_EXPLICATION_CODE.md     # Explication détaillée du code
└── 📄 IMPLEMENTATION_BLOCAGE.md     # Guide d'implémentation backend
```

---

## 🚀 Démarrage Rapide

### 1️⃣ Installation

```bash
cd tests_selenium
pip install -r requirements.txt
```

### 2️⃣ Configuration

Modifiez `config.py` avec vos identifiants de test :

```python
VALID_PHONE = "0612345678"      # Remplacer par un utilisateur existant
VALID_PASSWORD = "password123"   # Remplacer par le bon mot de passe
```

### 3️⃣ Lancer l'Application

```bash
# Terminal 1 : Backend
cd backend
docker-compose up

# Terminal 2 : Frontend
cd frontend
npm run dev
```

### 4️⃣ Exécuter les Tests

```bash
# Test 1 : Authentification réussie
python test_auth_reussie.py

# Test 2 : Authentification échouée
python test_auth_echouee.py

# Tous les tests avec rapport
pytest -v --html=rapport_tests.html --self-contained-html

# Démonstration avec captures d'écran
python demo_avec_screenshots.py
```

---

## 📊 Scénarios de Test

### ✅ Test 1 : Authentification Réussie

**Fichier** : `test_auth_reussie.py`

**Étapes** :
1. 🌐 Saisir l'URL dans le navigateur → `http://localhost:3000/login`
2. 📋 Le système affiche le formulaire (téléphone + mot de passe)
3. ⌨️ Remplir le formulaire avec identifiants valides
4. ✅ Le système vérifie et redirige vers la page d'accueil
5. 🚪 L'utilisateur clique sur "Déconnexion"
6. ↩️ Le système redirige vers la page de connexion

**Résultat attendu** : Connexion réussie et déconnexion fonctionnelle

---

### ❌ Test 2 : Authentification Échouée (3 Tentatives)

**Fichier** : `test_auth_echouee.py`

**Étapes** :

#### Tentative 1 :
- ⌨️ Saisie d'identifiants invalides
- ⚠️ Message : "Identifiants incorrects (tentative 1/3)"
- 📝 Le système enregistre l'échec

#### Tentative 2 :
- ⌨️ Saisie d'identifiants invalides
- ⚠️ Message : "Identifiants incorrects (tentative 2/3)"
- 📝 Le système enregistre l'échec

#### Tentative 3 :
- ⌨️ Saisie d'identifiants invalides
- 🔒 Message : "Compte bloqué après 3 tentatives"
- 🚫 Le système désactive le compte

#### Vérification :
- ⌨️ Tentative avec bons identifiants
- 🔒 Le compte reste bloqué

**Résultat attendu** : Compte bloqué après 3 tentatives, même avec bons identifiants

---

## 🎨 Exemple de Code Simplifié

### Test Basique (pour comprendre)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Ouvrir le navigateur
driver = webdriver.Chrome()
driver.get("http://localhost:3000/login")

# 2. Trouver les éléments
email_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

# 3. Remplir le formulaire
email_input.send_keys("test@example.com")
password_input.send_keys("password123")

# 4. Soumettre
login_button.click()
time.sleep(2)

# 5. Vérifier
if "dashboard" in driver.current_url:
    print("✅ Connexion réussie !")
else:
    print("❌ Connexion échouée !")

# 6. Fermer
driver.quit()
```

---

## 📸 Captures d'Écran Automatiques

Le script `demo_avec_screenshots.py` génère automatiquement des captures d'écran :

```
screenshots/
├── 01_page_connexion.png
├── 02_formulaire_vide.png
├── 03_formulaire_rempli.png
├── 04_apres_soumission.png
├── 05_connexion_reussie.png
├── 06_tentative_1_resultat.png
├── 07_compte_bloque.png
└── ...
```

---

## 🔧 Implémentation Backend Requise

Pour que les tests fonctionnent complètement, le backend doit implémenter :

### 1. Champs dans la table `users`

```sql
ALTER TABLE users ADD COLUMN login_attempts INT DEFAULT 0;
ALTER TABLE users ADD COLUMN account_locked BOOLEAN DEFAULT FALSE;
ALTER TABLE users ADD COLUMN locked_at TIMESTAMP NULL;
```

### 2. Logique dans AuthController

```php
// Incrémenter les tentatives
$user->login_attempts += 1;

// Bloquer après 3 tentatives
if ($user->login_attempts >= 3) {
    $user->account_locked = true;
    $user->locked_at = now();
}

// Réinitialiser après connexion réussie
$user->login_attempts = 0;
```

**Voir le fichier `IMPLEMENTATION_BLOCAGE.md` pour le code complet**

---

## 📖 Documentation Complète

| Fichier | Description |
|---------|-------------|
| `README.md` | Guide d'utilisation des tests |
| `GUIDE_EXPLICATION_CODE.md` | Explication détaillée de chaque ligne de code |
| `IMPLEMENTATION_BLOCAGE.md` | Guide pour implémenter le blocage dans le backend |

---

## ✅ Checklist de Validation

### Avant d'exécuter les tests :

- [ ] Python 3.8+ installé
- [ ] Chrome installé
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] Backend lancé (http://localhost:8000)
- [ ] Frontend lancé (http://localhost:3000)
- [ ] Base de données migrée
- [ ] Utilisateur de test créé

### Après exécution :

- [ ] Test 1 passe (authentification réussie)
- [ ] Test 2 passe (3 tentatives + blocage)
- [ ] Captures d'écran générées
- [ ] Rapport HTML créé

---

## 🎓 Concepts Selenium Utilisés

| Concept | Utilité | Ligne de Code |
|---------|---------|---------------|
| **WebDriver** | Contrôler le navigateur | `webdriver.Chrome()` |
| **find_element** | Trouver un élément | `driver.find_element(By.NAME, "email")` |
| **send_keys** | Saisir du texte | `element.send_keys("texte")` |
| **click** | Cliquer | `button.click()` |
| **WebDriverWait** | Attendre | `wait.until(EC.presence_of_element_located())` |
| **assert** | Vérifier | `assert "login" in url` |
| **screenshot** | Capture d'écran | `driver.save_screenshot("image.png")` |

---

## 🐛 Dépannage

### Problème : "Element not found"

**Solution** :
```python
# Augmenter les temps d'attente dans config.py
IMPLICIT_WAIT = 15  # Au lieu de 10
EXPLICIT_WAIT = 20  # Au lieu de 15
```

### Problème : "ChromeDriver not found"

**Solution** :
```bash
pip install --upgrade webdriver-manager
```

### Problème : "Connection refused"

**Solution** :
- Vérifier que le frontend tourne : `http://localhost:3000`
- Vérifier que le backend tourne : `http://localhost:8000`

---

## 📚 Ressources Supplémentaires

- [Documentation Selenium Python](https://selenium-python.readthedocs.io/)
- [Documentation Pytest](https://docs.pytest.org/)
- [Sélecteurs CSS](https://www.w3schools.com/cssref/css_selectors.asp)
- [XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)

---

## 🎉 Félicitations !

Vous avez maintenant :

✅ **2 tests fonctionnels complets** pour l'authentification  
✅ **Documentation détaillée** avec explications du code  
✅ **Guide d'implémentation** pour le backend  
✅ **Captures d'écran automatiques** pour la démonstration  
✅ **Rapport HTML** pour visualiser les résultats  

**Prêt à tester votre plateforme de gestion des réclamations ! 🚀**

---

## 📞 Support

Pour toute question sur les tests :
1. Consultez `GUIDE_EXPLICATION_CODE.md` pour comprendre le code
2. Consultez `README.md` pour l'utilisation
3. Consultez `IMPLEMENTATION_BLOCAGE.md` pour le backend

**Bon courage avec vos tests ! 💪**
