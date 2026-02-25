"""
Configuration pour les tests Selenium
"""

# URL de base de l'application
BASE_URL = "http://localhost:3000"

# Identifiants de test valides
VALID_PHONE = "adama@gmail.com"
VALID_PASSWORD = "Adama123"

# Identifiants de test invalides
INVALID_PHONE = "0699999999"
INVALID_PASSWORD = "wrongpassword"

# Temps d'attente (en secondes)
IMPLICIT_WAIT = 20
EXPLICIT_WAIT = 30

# Navigateur à utiliser (chrome, firefox, edge)
BROWSER = "chrome"
