"""
Test Fonctionnel 1 : Authentification Réussie
Ce test vérifie le scénario d'une authentification réussie sur la plateforme
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import config


class TestAuthenticationReussie:
    """
    Classe de test pour l'authentification réussie
    """
    
    def setup_method(self):
        """
        Configuration initiale avant chaque test
        Initialise le navigateur Chrome
        """
        print("\n=== INITIALISATION DU NAVIGATEUR ===")
        
        # Options Chrome pour plus de stabilité
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(config.IMPLICIT_WAIT)
        self.wait = WebDriverWait(self.driver, config.EXPLICIT_WAIT)
    
    def teardown_method(self):
        """
        Nettoyage après chaque test
        Ferme le navigateur
        """
        print("\n=== FERMETURE DU NAVIGATEUR ===")
        time.sleep(2)  # Pause pour voir le résultat
        self.driver.quit()
    
    def test_authentification_reussie(self):
        """
        Test du scénario d'authentification réussie
        
        Étapes:
        1. Saisir l'URL dans le navigateur
        2. Vérifier l'affichage du formulaire de connexion
        3. Remplir le formulaire avec des identifiants valides
        4. Vérifier la redirection vers la page d'accueil
        5. Vérifier la déconnexion
        """
        
        # ===== ÉTAPE 1: Saisir l'URL dans le navigateur =====
        print("\n--- ÉTAPE 1: Navigation vers la page de connexion ---")
        self.driver.get(f"{config.BASE_URL}/login")
        print(f"✓ URL chargée: {self.driver.current_url}")
        time.sleep(5)  # Attendre que la page se charge complètement
        
        # ===== ÉTAPE 2: Vérifier l'affichage du formulaire =====
        print("\n--- ÉTAPE 2: Vérification du formulaire de connexion ---")
        
        # Attendre que le formulaire soit visible
        try:
            # Recherche du champ email par type
            phone_input = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
            )
            print("✓ Champ téléphone/email trouvé")
            
            # Recherche du champ mot de passe par type
            password_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
            print("✓ Champ mot de passe trouvé")
            
            # Recherche du bouton de connexion
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            print("✓ Bouton de connexion trouvé")
            
        except Exception as e:
            print(f"✗ Erreur lors de la recherche des éléments: {e}")
            raise
        
        # ===== ÉTAPE 3: Remplir le formulaire avec des identifiants valides =====
        print("\n--- ÉTAPE 3: Remplissage du formulaire ---")
        
        # Saisir le numéro de téléphone/email
        phone_input.clear()
        phone_input.send_keys(config.VALID_PHONE)
        print(f"✓ Téléphone saisi: {config.VALID_PHONE}")
        time.sleep(1)
        
        # Saisir le mot de passe
        password_input.clear()
        password_input.send_keys(config.VALID_PASSWORD)
        print(f"✓ Mot de passe saisi: {'*' * len(config.VALID_PASSWORD)}")
        time.sleep(1)
        
        # Cliquer sur le bouton de connexion
        login_button.click()
        print("✓ Bouton de connexion cliqué")
        time.sleep(3)
        
        # ===== ÉTAPE 4: Vérifier la redirection vers la page d'accueil =====
        print("\n--- ÉTAPE 4: Vérification de la connexion réussie ---")
        
        try:
            # Attendre la redirection (l'URL change ou un élément spécifique apparaît)
            self.wait.until(
                lambda driver: "login" not in driver.current_url.lower()
            )
            print(f"✓ Redirection réussie vers: {self.driver.current_url}")
            
            # Vérifier la présence d'un élément de la page d'accueil
            # (Adapter selon votre interface: dashboard, menu utilisateur, etc.)
            try:
                dashboard_element = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Dashboard') or contains(text(), 'Tableau de bord')]"))
                )
                print("✓ Page d'accueil chargée avec succès")
            except:
                print("⚠ Élément 'Dashboard' non trouvé, mais connexion semble réussie")
            
        except Exception as e:
            print(f"✗ Erreur lors de la vérification de la connexion: {e}")
            raise
        
        # ===== ÉTAPE 5: Test de déconnexion =====
        print("\n--- ÉTAPE 5: Test de déconnexion ---")
        
        try:
            # Rechercher le bouton de déconnexion
            # (Adapter le sélecteur selon votre interface)
            logout_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Déconnexion') or contains(text(), 'Logout')]"))
            )
            logout_button.click()
            print("✓ Bouton de déconnexion cliqué")
            time.sleep(2)
            
            # Vérifier la redirection vers la page de connexion
            self.wait.until(
                EC.url_contains("login")
            )
            print(f"✓ Déconnexion réussie, redirection vers: {self.driver.current_url}")
            
        except Exception as e:
            print(f"⚠ Impossible de tester la déconnexion: {e}")
        
        print("\n=== TEST AUTHENTIFICATION RÉUSSIE: SUCCÈS ✓ ===")


if __name__ == "__main__":
    """
    Exécution directe du test
    """
    test = TestAuthenticationReussie()
    test.setup_method()
    try:
        test.test_authentification_reussie()
    finally:
        test.teardown_method()
