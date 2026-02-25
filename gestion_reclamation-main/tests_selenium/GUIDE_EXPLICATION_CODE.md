# 📚 Guide d'Explication Détaillée du Code des Tests Selenium

Ce document explique en détail chaque partie du code des tests fonctionnels.

---

## 🎯 Structure Générale d'un Test Selenium

### 1. Imports Nécessaires

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

**Explication** :
- `webdriver` : Module principal pour contrôler le navigateur
- `By` : Classe pour spécifier comment trouver les éléments (par ID, nom, classe, etc.)
- `WebDriverWait` : Pour attendre qu'une condition soit remplie avant de continuer
- `expected_conditions (EC)` : Conditions prédéfinies (élément visible, cliquable, etc.)

---

## 🔧 Méthodes de Configuration

### setup_method()

```python
def setup_method(self):
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    self.driver.maximize_window()
    self.driver.implicitly_wait(config.IMPLICIT_WAIT)
    self.wait = WebDriverWait(self.driver, config.EXPLICIT_WAIT)
```

**Explication ligne par ligne** :

1. **`webdriver.Chrome(...)`** : Crée une instance du navigateur Chrome
   - `ChromeDriverManager().install()` : Télécharge automatiquement le driver Chrome compatible

2. **`maximize_window()`** : Agrandit la fenêtre en plein écran
   - Utile pour éviter que des éléments soient cachés

3. **`implicitly_wait(10)`** : Attend jusqu'à 10 secondes pour trouver un élément
   - Si l'élément n'existe pas immédiatement, Selenium réessaie pendant 10 secondes

4. **`WebDriverWait(self.driver, 15)`** : Crée un objet d'attente explicite
   - Permet d'attendre des conditions spécifiques (élément visible, URL changée, etc.)

### teardown_method()

```python
def teardown_method(self):
    time.sleep(2)
    self.driver.quit()
```

**Explication** :
- `time.sleep(2)` : Pause de 2 secondes pour voir le résultat final
- `driver.quit()` : Ferme le navigateur et libère les ressources

---

## 🔍 Recherche d'Éléments

### Méthode 1 : find_element()

```python
phone_input = self.driver.find_element(By.NAME, "email")
```

**Explication** :
- Recherche UN élément dans la page
- `By.NAME` : Cherche par l'attribut `name` de l'élément HTML
- `"email"` : Valeur de l'attribut à chercher
- Retourne l'élément trouvé ou lève une exception si non trouvé

**Équivalent HTML** :
```html
<input name="email" type="text" />
```

### Méthode 2 : Attente Explicite

```python
phone_input = self.wait.until(
    EC.presence_of_element_located((By.NAME, "email"))
)
```

**Explication** :
- Attend jusqu'à 15 secondes (défini dans setup) que l'élément apparaisse
- `EC.presence_of_element_located` : Condition = élément présent dans le DOM
- Plus robuste que `find_element()` car attend le chargement de la page

### Types de Sélecteurs (By)

| Sélecteur | Exemple | HTML Correspondant |
|-----------|---------|-------------------|
| `By.ID` | `By.ID, "login-btn"` | `<button id="login-btn">` |
| `By.NAME` | `By.NAME, "email"` | `<input name="email">` |
| `By.CLASS_NAME` | `By.CLASS_NAME, "error"` | `<div class="error">` |
| `By.TAG_NAME` | `By.TAG_NAME, "button"` | `<button>` |
| `By.CSS_SELECTOR` | `By.CSS_SELECTOR, "input[type='email']"` | `<input type="email">` |
| `By.XPATH` | `By.XPATH, "//button[@type='submit']"` | `<button type="submit">` |

---

## ⌨️ Interaction avec les Éléments

### 1. Saisir du Texte

```python
phone_input.clear()
phone_input.send_keys(config.VALID_PHONE)
```

**Explication** :
- `clear()` : Efface le contenu actuel du champ (important si déjà rempli)
- `send_keys("texte")` : Simule la frappe au clavier
- Équivalent à : L'utilisateur clique dans le champ et tape le texte

### 2. Cliquer sur un Élément

```python
login_button.click()
```

**Explication** :
- Simule un clic de souris sur l'élément
- Déclenche les événements JavaScript associés (onclick, etc.)

### 3. Récupérer du Texte

```python
error_text = error_element.text
```

**Explication** :
- Récupère le texte visible de l'élément
- Exemple : `<div class="error">Identifiants incorrects</div>` → retourne "Identifiants incorrects"

---

## ⏱️ Gestion des Attentes

### 1. Attente Implicite (Globale)

```python
self.driver.implicitly_wait(10)
```

**Explication** :
- S'applique à TOUTES les recherches d'éléments
- Si un élément n'est pas trouvé, Selenium réessaie pendant 10 secondes
- Simple mais moins flexible

### 2. Attente Explicite (Spécifique)

```python
self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
```

**Explication** :
- S'applique à UNE recherche spécifique
- Plus précis et recommandé pour les éléments dynamiques
- Permet d'attendre des conditions complexes

### 3. Attente Simple (Sleep)

```python
time.sleep(2)
```

**Explication** :
- Pause fixe de 2 secondes
- À utiliser avec modération (ralentit les tests)
- Utile pour voir les résultats ou attendre des animations

### Conditions d'Attente Courantes

```python
# Attendre que l'élément soit présent dans le DOM
EC.presence_of_element_located((By.ID, "element"))

# Attendre que l'élément soit visible
EC.visibility_of_element_located((By.ID, "element"))

# Attendre que l'élément soit cliquable
EC.element_to_be_clickable((By.ID, "button"))

# Attendre un changement d'URL
EC.url_contains("dashboard")

# Attendre qu'un texte soit présent
EC.text_to_be_present_in_element((By.ID, "message"), "Succès")
```

---

## 🧪 Assertions et Vérifications

### 1. Vérification d'URL

```python
assert "login" in self.driver.current_url.lower()
```

**Explication** :
- `self.driver.current_url` : Récupère l'URL actuelle
- `.lower()` : Convertit en minuscules pour comparaison insensible à la casse
- `assert` : Lève une exception si la condition est fausse (test échoue)

### 2. Vérification avec Try/Except

```python
try:
    error_element = self.wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "error"))
    )
    print(f"✓ Message d'erreur: {error_element.text}")
except Exception as e:
    print(f"⚠ Message d'erreur non trouvé: {e}")
```

**Explication** :
- `try` : Tente d'exécuter le code
- `except` : Capture l'erreur si le code échoue
- Permet de continuer le test même si un élément n'est pas trouvé

---

## 📸 Captures d'Écran

```python
def take_screenshot(self, description):
    filename = f"{self.screenshot_counter:02d}_{description}.png"
    filepath = os.path.join(self.screenshot_dir, filename)
    self.driver.save_screenshot(filepath)
    self.screenshot_counter += 1
```

**Explication ligne par ligne** :

1. **`f"{self.screenshot_counter:02d}"`** : Formate le numéro avec 2 chiffres (01, 02, 03...)
2. **`os.path.join()`** : Crée un chemin de fichier compatible avec l'OS
3. **`save_screenshot(filepath)`** : Sauvegarde une capture d'écran de la page entière
4. **`screenshot_counter += 1`** : Incrémente le compteur pour la prochaine capture

---

## 🔄 Fonction Utilitaire : tenter_connexion()

```python
def tenter_connexion(self, phone, password, tentative_num):
    print(f"\n--- TENTATIVE {tentative_num} ---")
    
    phone_input = self.driver.find_element(By.NAME, "email")
    password_input = self.driver.find_element(By.NAME, "password")
    login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
    
    phone_input.clear()
    phone_input.send_keys(phone)
    
    password_input.clear()
    password_input.send_keys(password)
    
    login_button.click()
    time.sleep(2)
```

**Explication** :
- Fonction réutilisable pour éviter la duplication de code
- Prend en paramètres : téléphone, mot de passe, numéro de tentative
- Effectue toutes les actions nécessaires pour une tentative de connexion
- Permet de tester facilement les 3 tentatives échouées

---

## 🎯 Test Complet : Authentification Réussie

```python
def test_authentification_reussie(self):
    # 1. Navigation
    self.driver.get(f"{config.BASE_URL}/login")
    
    # 2. Recherche des éléments
    phone_input = self.wait.until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    password_input = self.driver.find_element(By.NAME, "password")
    login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
    
    # 3. Remplissage du formulaire
    phone_input.send_keys(config.VALID_PHONE)
    password_input.send_keys(config.VALID_PASSWORD)
    
    # 4. Soumission
    login_button.click()
    
    # 5. Vérification de la redirection
    self.wait.until(lambda driver: "login" not in driver.current_url.lower())
    
    # 6. Vérification de la page d'accueil
    dashboard_element = self.wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Dashboard')]"))
    )
```

**Flux d'exécution** :
1. ➡️ Ouvre la page de connexion
2. ➡️ Attend que le formulaire soit chargé
3. ➡️ Remplit les champs avec des identifiants valides
4. ➡️ Clique sur le bouton de connexion
5. ➡️ Attend que l'URL change (redirection)
6. ➡️ Vérifie la présence d'un élément de la page d'accueil

---

## 🚫 Test Complet : Authentification Échouée

```python
def test_authentification_echouee_3_tentatives(self):
    # Navigation initiale
    self.driver.get(f"{config.BASE_URL}/login")
    
    # Boucle pour 3 tentatives
    for tentative in range(1, 4):
        # Tentative de connexion avec identifiants invalides
        self.tenter_connexion(config.INVALID_PHONE, config.INVALID_PASSWORD, tentative)
        
        # Vérification du message d'erreur
        self.verifier_message_erreur(tentative)
        
        # Vérification que l'utilisateur reste sur la page de connexion
        assert "login" in self.driver.current_url.lower()
        
        time.sleep(2)
    
    # Vérification du blocage
    self.tenter_connexion(config.VALID_PHONE, config.VALID_PASSWORD, 4)
    
    # Le compte devrait rester bloqué
    if "login" in self.driver.current_url.lower():
        print("✓ Compte bloqué confirmé")
```

**Flux d'exécution** :
1. ➡️ Ouvre la page de connexion
2. ➡️ **Tentative 1** : Identifiants invalides → Message d'erreur
3. ➡️ **Tentative 2** : Identifiants invalides → Message d'erreur
4. ➡️ **Tentative 3** : Identifiants invalides → Message de blocage
5. ➡️ **Vérification** : Même avec bons identifiants, connexion impossible

---

## 🎨 XPath : Sélecteurs Avancés

### Exemples de XPath

```python
# Trouver un bouton par son texte
"//button[contains(text(), 'Connexion')]"

# Trouver un élément par son attribut
"//input[@type='email']"

# Trouver un élément par sa classe
"//*[contains(@class, 'error')]"

# Trouver un élément parent
"//div[@class='form']//input[@name='email']"

# Trouver le premier élément d'une liste
"(//button[@type='submit'])[1]"
```

**Explication** :
- `//` : Cherche dans toute la page
- `*` : N'importe quel élément
- `[@attribut='valeur']` : Filtre par attribut
- `contains()` : Recherche partielle
- `text()` : Texte de l'élément

---

## 📊 Bonnes Pratiques

### 1. Utiliser des Attentes Explicites

❌ **Mauvais** :
```python
time.sleep(5)  # Attend toujours 5 secondes
element = self.driver.find_element(By.ID, "button")
```

✅ **Bon** :
```python
element = self.wait.until(
    EC.element_to_be_clickable((By.ID, "button"))
)  # Attend seulement le temps nécessaire
```

### 2. Gérer les Exceptions

❌ **Mauvais** :
```python
element = self.driver.find_element(By.ID, "button")
# Si l'élément n'existe pas, le test plante
```

✅ **Bon** :
```python
try:
    element = self.driver.find_element(By.ID, "button")
except NoSuchElementException:
    print("Élément non trouvé")
    # Gérer l'erreur ou prendre une capture d'écran
```

### 3. Utiliser des Fonctions Réutilisables

❌ **Mauvais** :
```python
# Répéter le même code 3 fois
phone_input.send_keys("0612345678")
password_input.send_keys("password")
login_button.click()
```

✅ **Bon** :
```python
def tenter_connexion(phone, password):
    phone_input.send_keys(phone)
    password_input.send_keys(password)
    login_button.click()

# Utiliser la fonction
tenter_connexion("0612345678", "password")
```

---

## 🎓 Résumé des Concepts Clés

| Concept | Utilité | Exemple |
|---------|---------|---------|
| **WebDriver** | Contrôler le navigateur | `webdriver.Chrome()` |
| **find_element()** | Trouver un élément | `find_element(By.NAME, "email")` |
| **send_keys()** | Saisir du texte | `element.send_keys("texte")` |
| **click()** | Cliquer | `button.click()` |
| **WebDriverWait** | Attendre une condition | `wait.until(EC.presence_of_element_located())` |
| **assert** | Vérifier une condition | `assert "login" in url` |
| **try/except** | Gérer les erreurs | `try: ... except: ...` |
| **XPath** | Sélecteur avancé | `"//button[contains(text(), 'OK')]"` |

---

## 🚀 Pour Aller Plus Loin

### Actions Avancées

```python
from selenium.webdriver.common.action_chains import ActionChains

# Survol d'un élément
actions = ActionChains(self.driver)
actions.move_to_element(element).perform()

# Double-clic
actions.double_click(element).perform()

# Glisser-déposer
actions.drag_and_drop(source, target).perform()
```

### Gestion des Alertes

```python
# Accepter une alerte JavaScript
alert = self.driver.switch_to.alert
alert.accept()

# Refuser une alerte
alert.dismiss()

# Récupérer le texte de l'alerte
alert_text = alert.text
```

### Gestion des Fenêtres

```python
# Changer de fenêtre/onglet
self.driver.switch_to.window(self.driver.window_handles[1])

# Revenir à la fenêtre principale
self.driver.switch_to.window(self.driver.window_handles[0])
```

---

## ✅ Checklist de Compréhension

Après avoir lu ce guide, vous devriez comprendre :

- [ ] Comment initialiser un navigateur avec Selenium
- [ ] Comment trouver des éléments dans une page web
- [ ] Comment interagir avec les éléments (clic, saisie)
- [ ] Comment attendre le chargement des éléments
- [ ] Comment vérifier les résultats (assertions)
- [ ] Comment gérer les erreurs
- [ ] Comment prendre des captures d'écran
- [ ] Comment structurer un test complet

---

**🎉 Félicitations ! Vous maîtrisez maintenant les bases de Selenium avec Python !**
