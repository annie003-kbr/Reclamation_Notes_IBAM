# 🧪 Tests Fonctionnels Selenium - Authentification

Ce dossier contient les tests fonctionnels automatisés pour tester l'authentification de la plateforme de gestion des réclamations.

## 📋 Prérequis

- Python 3.8 ou supérieur
- Google Chrome installé
- L'application doit être lancée (frontend sur http://localhost:3000)

## 🚀 Installation

### 1. Installer les dépendances Python

```bash
cd tests_selenium
pip install -r requirements.txt
```

### 2. Configuration

Modifier le fichier `config.py` si nécessaire pour adapter :
- L'URL de base de l'application
- Les identifiants de test
- Les temps d'attente

## 📝 Structure des Tests

### Test 1 : Authentification Réussie (`test_auth_reussie.py`)

**Objectif** : Vérifier qu'un utilisateur peut se connecter avec des identifiants valides

**Étapes testées** :
1. ✅ Navigation vers la page de connexion
2. ✅ Affichage du formulaire (téléphone + mot de passe)
3. ✅ Saisie des identifiants valides
4. ✅ Vérification de la connexion réussie
5. ✅ Redirection vers la page d'accueil
6. ✅ Test de déconnexion

**Exécution** :
```bash
python test_auth_reussie.py
```

### Test 2 : Authentification Échouée (`test_auth_echouee.py`)

**Objectif** : Vérifier le système de blocage après 3 tentatives échouées

**Étapes testées** :
1. ✅ Navigation vers la page de connexion
2. ✅ **Tentative 1** : Identifiants invalides → Message d'erreur + Échec enregistré
3. ✅ **Tentative 2** : Identifiants invalides → Message d'erreur + Échec enregistré
4. ✅ **Tentative 3** : Identifiants invalides → Message de blocage + Compte désactivé
5. ✅ Vérification que le compte reste bloqué même avec bons identifiants

**Exécution** :
```bash
python test_auth_echouee.py
```

## 🎯 Exécution des Tests

### Exécuter un test individuel

```bash
# Test d'authentification réussie
python test_auth_reussie.py

# Test d'authentification échouée
python test_auth_echouee.py
```

### Exécuter tous les tests avec pytest

```bash
# Exécution simple
pytest -v

# Avec génération de rapport HTML
pytest -v --html=rapport_tests.html --self-contained-html

# Exécuter la suite complète
python test_suite.py
```

## 📊 Rapport de Tests

Après l'exécution avec pytest, un rapport HTML est généré : `rapport_tests.html`

Ouvrez ce fichier dans un navigateur pour voir :
- ✅ Tests réussis
- ❌ Tests échoués
- ⏱️ Temps d'exécution
- 📸 Captures d'écran (si configurées)

## 🔧 Personnalisation

### Modifier les identifiants de test

Éditez `config.py` :

```python
# Identifiants valides (à adapter selon votre base de données)
VALID_PHONE = "0612345678"
VALID_PASSWORD = "password123"

# Identifiants invalides
INVALID_PHONE = "0699999999"
INVALID_PASSWORD = "wrongpassword"
```

### Adapter les sélecteurs

Si votre interface utilise des sélecteurs différents, modifiez les fichiers de test :

```python
# Exemple : Changer le sélecteur du champ email
phone_input = self.driver.find_element(By.NAME, "email")  # ou By.ID, By.CSS_SELECTOR, etc.
```

## 📖 Explication du Code

### Structure d'un test Selenium

```python
class TestAuthentication:
    def setup_method(self):
        # 1. Initialisation du navigateur
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
    def test_exemple(self):
        # 2. Navigation
        self.driver.get("http://localhost:3000/login")
        
        # 3. Recherche d'éléments
        element = self.driver.find_element(By.NAME, "email")
        
        # 4. Interaction
        element.send_keys("test@example.com")
        
        # 5. Vérification
        assert "dashboard" in self.driver.current_url
    
    def teardown_method(self):
        # 6. Nettoyage
        self.driver.quit()
```

### Méthodes Selenium utilisées

| Méthode | Description | Exemple |
|---------|-------------|---------|
| `driver.get(url)` | Naviguer vers une URL | `driver.get("http://localhost:3000")` |
| `find_element(By.X, "value")` | Trouver un élément | `find_element(By.NAME, "email")` |
| `element.send_keys(text)` | Saisir du texte | `element.send_keys("test@mail.com")` |
| `element.click()` | Cliquer sur un élément | `button.click()` |
| `element.clear()` | Effacer un champ | `input.clear()` |
| `WebDriverWait().until()` | Attendre une condition | `wait.until(EC.presence_of_element_located())` |

### Sélecteurs disponibles

```python
By.ID           # Par ID : <input id="email">
By.NAME         # Par nom : <input name="email">
By.CLASS_NAME   # Par classe : <div class="error">
By.TAG_NAME     # Par balise : <button>
By.CSS_SELECTOR # Par CSS : "input[type='email']"
By.XPATH        # Par XPath : "//button[@type='submit']"
```

## ⚠️ Notes Importantes

### Pour que les tests fonctionnent correctement :

1. **Backend** : Doit implémenter le système de blocage après 3 tentatives
   - Ajouter un champ `login_attempts` dans la table `users`
   - Ajouter un champ `account_locked` dans la table `users`
   - Modifier le contrôleur d'authentification pour gérer le compteur

2. **Frontend** : Doit afficher les messages d'erreur appropriés
   - Message pour tentatives 1 et 2 : "Identifiants incorrects"
   - Message pour tentative 3 : "Compte bloqué après 3 tentatives"

3. **Base de données** : Créer un utilisateur de test
   ```sql
   INSERT INTO users (name, email, password, role_id) 
   VALUES ('Test User', '0612345678', '$2y$10$...', 1);
   ```

## 🐛 Dépannage

### Erreur : "ChromeDriver not found"
```bash
pip install --upgrade webdriver-manager
```

### Erreur : "Element not found"
- Vérifier que l'application est bien lancée
- Augmenter les temps d'attente dans `config.py`
- Vérifier les sélecteurs dans les fichiers de test

### Erreur : "Connection refused"
- Vérifier que le frontend tourne sur http://localhost:3000
- Vérifier que le backend tourne sur http://localhost:8000

## 📚 Ressources

- [Documentation Selenium Python](https://selenium-python.readthedocs.io/)
- [Documentation Pytest](https://docs.pytest.org/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

## 👨‍💻 Auteur

Tests créés pour le projet IBAM - Gestion des Réclamations
