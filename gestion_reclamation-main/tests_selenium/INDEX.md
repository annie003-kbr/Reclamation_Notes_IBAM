# 📚 INDEX - Tests Fonctionnels Selenium

## 🎯 Bienvenue !

Ce dossier contient tous les tests fonctionnels pour l'authentification de votre plateforme de gestion des réclamations.

---

## 🗂️ Navigation Rapide

### 🚀 Pour Commencer

| Fichier | Description | Quand l'utiliser |
|---------|-------------|------------------|
| **[EXERCICE_RESUME.md](EXERCICE_RESUME.md)** | 📋 Résumé complet de l'exercice | **COMMENCEZ ICI** - Vue d'ensemble |
| **[README.md](README.md)** | 📖 Guide d'utilisation | Pour installer et exécuter les tests |
| **[requirements.txt](requirements.txt)** | 📦 Dépendances Python | Pour installer les packages nécessaires |

### 📝 Fichiers de Test

| Fichier | Description | Commande |
|---------|-------------|----------|
| **[test_auth_reussie.py](test_auth_reussie.py)** | ✅ Test d'authentification réussie | `python test_auth_reussie.py` |
| **[test_auth_echouee.py](test_auth_echouee.py)** | ❌ Test d'authentification échouée (3 tentatives) | `python test_auth_echouee.py` |
| **[test_suite.py](test_suite.py)** | 🎯 Suite complète de tests | `python test_suite.py` |
| **[demo_avec_screenshots.py](demo_avec_screenshots.py)** | 📸 Démonstration avec captures d'écran | `python demo_avec_screenshots.py` |

### 📚 Documentation

| Fichier | Description | Pour qui |
|---------|-------------|----------|
| **[GUIDE_EXPLICATION_CODE.md](GUIDE_EXPLICATION_CODE.md)** | 🎓 Explication détaillée du code | Étudiants / Débutants Selenium |
| **[IMPLEMENTATION_BLOCAGE.md](IMPLEMENTATION_BLOCAGE.md)** | 🔧 Guide d'implémentation backend | Développeurs backend |
| **[config.py](config.py)** | ⚙️ Configuration des tests | Pour personnaliser les paramètres |

---

## 🎯 Parcours Recommandé

### Pour les Débutants

```
1. EXERCICE_RESUME.md          → Comprendre l'objectif
2. README.md                   → Installer les dépendances
3. GUIDE_EXPLICATION_CODE.md   → Apprendre Selenium
4. test_auth_reussie.py        → Exécuter le premier test
5. test_auth_echouee.py        → Exécuter le second test
```

### Pour les Développeurs Expérimentés

```
1. EXERCICE_RESUME.md          → Vue d'ensemble rapide
2. requirements.txt            → pip install -r requirements.txt
3. config.py                   → Adapter la configuration
4. test_suite.py               → Exécuter tous les tests
5. IMPLEMENTATION_BLOCAGE.md   → Implémenter le backend
```

### Pour la Démonstration

```
1. demo_avec_screenshots.py    → Exécuter la démo
2. screenshots/                → Consulter les captures
3. rapport_tests.html          → Voir le rapport
```

---

## 📋 Checklist Complète

### Installation

- [ ] Python 3.8+ installé
- [ ] Chrome installé
- [ ] `pip install -r requirements.txt` exécuté
- [ ] `config.py` configuré avec vos identifiants

### Préparation de l'Application

- [ ] Backend lancé (http://localhost:8000)
- [ ] Frontend lancé (http://localhost:3000)
- [ ] Base de données migrée
- [ ] Utilisateur de test créé

### Exécution des Tests

- [ ] Test 1 exécuté : `python test_auth_reussie.py`
- [ ] Test 2 exécuté : `python test_auth_echouee.py`
- [ ] Suite complète : `pytest -v --html=rapport_tests.html`
- [ ] Démonstration : `python demo_avec_screenshots.py`

### Vérification des Résultats

- [ ] Tous les tests passent (✅)
- [ ] Captures d'écran générées dans `screenshots/`
- [ ] Rapport HTML créé : `rapport_tests.html`
- [ ] Logs affichés dans la console

---

## 🎓 Concepts Couverts

### Tests Fonctionnels

- ✅ Navigation web automatisée
- ✅ Recherche d'éléments (By.NAME, By.XPATH, etc.)
- ✅ Interaction avec les formulaires
- ✅ Vérification des résultats
- ✅ Gestion des attentes
- ✅ Captures d'écran automatiques
- ✅ Génération de rapports

### Scénarios Testés

- ✅ Authentification réussie
- ✅ Authentification échouée (1ère tentative)
- ✅ Authentification échouée (2ème tentative)
- ✅ Authentification échouée (3ème tentative)
- ✅ Blocage du compte après 3 tentatives
- ✅ Vérification du blocage persistant
- ✅ Déconnexion

---

## 🔧 Configuration Rapide

### 1. Installer les dépendances

```bash
cd tests_selenium
pip install -r requirements.txt
```

### 2. Configurer les identifiants

Éditez `config.py` :

```python
VALID_PHONE = "0612345678"      # Votre utilisateur de test
VALID_PASSWORD = "password123"   # Votre mot de passe de test
```

### 3. Lancer les tests

```bash
# Test individuel
python test_auth_reussie.py

# Tous les tests
pytest -v

# Avec rapport HTML
pytest -v --html=rapport_tests.html --self-contained-html

# Démonstration avec screenshots
python demo_avec_screenshots.py
```

---

## 📊 Structure des Tests

```
Test d'Authentification
│
├── Setup (Initialisation)
│   ├── Ouvrir le navigateur Chrome
│   ├── Maximiser la fenêtre
│   └── Configurer les attentes
│
├── Test (Exécution)
│   ├── Navigation vers la page
│   ├── Recherche des éléments
│   ├── Interaction (saisie, clic)
│   ├── Vérification des résultats
│   └── Captures d'écran
│
└── Teardown (Nettoyage)
    └── Fermer le navigateur
```

---

## 🎨 Exemple Visuel du Flux

```
┌─────────────────────────────────────────────────────────────┐
│                    TEST 1: AUTHENTIFICATION RÉUSSIE          │
└─────────────────────────────────────────────────────────────┘

1. 🌐 http://localhost:3000/login
   ↓
2. 📋 Formulaire affiché
   ↓
3. ⌨️  Saisie: email + password
   ↓
4. 🖱️  Clic sur "Connexion"
   ↓
5. ✅ Redirection → /dashboard
   ↓
6. 🚪 Clic sur "Déconnexion"
   ↓
7. ↩️  Retour → /login

┌─────────────────────────────────────────────────────────────┐
│                    TEST 2: AUTHENTIFICATION ÉCHOUÉE          │
└─────────────────────────────────────────────────────────────┘

1. 🌐 http://localhost:3000/login
   ↓
2. ❌ Tentative 1 (invalide) → ⚠️  "Erreur 1/3"
   ↓
3. ❌ Tentative 2 (invalide) → ⚠️  "Erreur 2/3"
   ↓
4. ❌ Tentative 3 (invalide) → 🔒 "Compte bloqué"
   ↓
5. ✅ Tentative 4 (valide) → 🔒 "Toujours bloqué"
```

---

## 📞 Aide et Support

### Problèmes Courants

| Problème | Solution | Fichier |
|----------|----------|---------|
| "Element not found" | Augmenter les temps d'attente | `config.py` |
| "ChromeDriver not found" | `pip install --upgrade webdriver-manager` | Terminal |
| "Connection refused" | Vérifier que l'app tourne | `docker-compose up` |
| Code incompréhensible | Lire les explications | `GUIDE_EXPLICATION_CODE.md` |
| Backend non implémenté | Suivre le guide | `IMPLEMENTATION_BLOCAGE.md` |

### Ressources Externes

- 📖 [Selenium Python Docs](https://selenium-python.readthedocs.io/)
- 📖 [Pytest Documentation](https://docs.pytest.org/)
- 📖 [XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)
- 📖 [CSS Selectors](https://www.w3schools.com/cssref/css_selectors.asp)

---

## 🎉 Résumé

Vous avez maintenant :

| ✅ | Élément |
|----|---------|
| ✅ | 2 tests fonctionnels complets |
| ✅ | Documentation détaillée (4 fichiers) |
| ✅ | Guide d'implémentation backend |
| ✅ | Script de démonstration avec screenshots |
| ✅ | Configuration personnalisable |
| ✅ | Génération de rapports HTML |
| ✅ | Explications ligne par ligne du code |

---

## 🚀 Prochaines Étapes

1. ✅ Lire `EXERCICE_RESUME.md`
2. ✅ Installer les dépendances
3. ✅ Configurer `config.py`
4. ✅ Lancer l'application
5. ✅ Exécuter les tests
6. ✅ Consulter les résultats
7. ✅ Implémenter le backend (si nécessaire)

---

**Bon courage avec vos tests ! 💪🚀**

*Créé pour le projet IBAM - Gestion des Réclamations*
