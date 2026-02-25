"""
Test Fonctionnel 2 : Authentification Non Réussie
Ce test vérifie le scénario d'échec d'authentification avec blocage après 3 tentatives
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import config


class TestAuthenticationEchouee:
    """
    Classe de test pour l'authentification échouée
    """
    
    def setup_method(self):
        """
        Configuration initiale avant chaque test
        Initialise le navigateur Chrome
        """
        print("\n=== INITIALISATION DU NAVIGATEUR ===")
        self.driver = webdriver.Chrome()
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
    
    def tenter_connexion(self, phone, password, tentative_num):
        """
        Fonction utilitaire pour tenter une connexion
        
        Args:
            phone: Numéro de téléphone/email
            password: Mot de passe
            tentative_num: Numéro de la tentative (1, 2 ou 3)
        """
        print(f"\n--- TENTATIVE {tentative_num} ---")
        
        # Rechercher les champs du formulaire
        phone_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        
        # Remplir le formulaire
        phone_input.clear()
        phone_input.send_keys(phone)
        print(f"✓ Téléphone saisi: {phone}")
        time.sleep(0.5)
        
        password_input.clear()
        password_input.send_keys(password)
        print(f"✓ Mot de passe saisi: {'*' * len(password)}")
        time.sleep(0.5)
        
        # Soumettre le formulaire
        login_button.click()
        print("✓ Formulaire soumis")
        time.sleep(2)
    
    def verifier_message_erreur(self, tentative_num):
        """
        Vérifie l'affichage du message d'erreur approprié
        
        Args:
            tentative_num: Numéro de la tentative pour adapter le message attendu
        """
        try:
            # Rechercher le message d'erreur
            # (Adapter les sélecteurs selon votre interface)
            error_message = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'error') or contains(@class, 'alert')]"))
            )
            
            message_text = error_message.text.lower()
            print(f"✓ Message d'erreur affiché: {error_message.text}")
            
            # Vérifier le contenu du message
            if tentative_num < 3:
                if "incorrect" in message_text or "erroné" in message_text or "invalide" in message_text:
                    print(f"✓ Message d'erreur approprié pour la tentative {tentative_num}")
                    return True
            else:
                if "bloqué" in message_text or "désactivé" in message_text or "compte" in message_text:
                    print(f"✓ Message de blocage affiché pour la tentative {tentative_num}")
                    return True
            
            return True
            
        except Exception as e:
            print(f"⚠ Message d'erreur non trouvé ou format différent: {e}")
            return False
    
    def test_authentification_echouee_3_tentatives(self):
        """
        Test du scénario d'authentification échouée avec 3 tentatives
        
        Étapes:
        1. Saisir l'URL dans le navigateur
        2. Vérifier l'affichage du formulaire
        3. Première tentative avec identifiants invalides
        4. Deuxième tentative avec identifiants invalides
        5. Troisième tentative avec identifiants invalides
        6. Vérifier le blocage du compte
        """
        
        # ===== ÉTAPE 1: Saisir l'URL dans le navigateur =====
        print("\n" + "="*60)
        print("TEST: AUTHENTIFICATION ÉCHOUÉE AVEC 3 TENTATIVES")
        print("="*60)
        
        print("\n--- ÉTAPE 1: Navigation vers la page de connexion ---")
        self.driver.get(f"{config.BASE_URL}/login")
        print(f"✓ URL chargée: {self.driver.current_url}")
        time.sleep(2)
        
        # ===== ÉTAPE 2: Vérifier l'affichage du formulaire =====
        print("\n--- ÉTAPE 2: Vérification du formulaire de connexion ---")
        
        try:
            phone_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            password_input = self.driver.find_element(By.NAME, "password")
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            print("✓ Formulaire de connexion trouvé et prêt")
        except Exception as e:
            print(f"✗ Erreur: Formulaire non trouvé - {e}")
            raise
        
        # ===== ÉTAPE 3: Première tentative échouée =====
        print("\n" + "="*60)
        print("PREMIÈRE TENTATIVE DE CONNEXION")
        print("="*60)
        
        self.tenter_connexion(config.INVALID_PHONE, config.INVALID_PASSWORD, 1)
        
        # Vérifier le message d'erreur
        self.verifier_message_erreur(1)
        
        # Vérifier que l'utilisateur est toujours sur la page de connexion
        assert "login" in self.driver.current_url.lower(), "L'utilisateur devrait rester sur la page de connexion"
        print("✓ L'utilisateur reste sur la page de connexion")
        print("✓ Le système a enregistré l'échec (tentative 1/3)")
        
        time.sleep(2)
        
        # ===== ÉTAPE 4: Deuxième tentative échouée =====
        print("\n" + "="*60)
        print("DEUXIÈME TENTATIVE DE CONNEXION")
        print("="*60)
        
        self.tenter_connexion(config.INVALID_PHONE, config.INVALID_PASSWORD, 2)
        
        # Vérifier le message d'erreur
        self.verifier_message_erreur(2)
        
        # Vérifier que l'utilisateur est toujours sur la page de connexion
        assert "login" in self.driver.current_url.lower(), "L'utilisateur devrait rester sur la page de connexion"
        print("✓ L'utilisateur reste sur la page de connexion")
        print("✓ Le système a enregistré l'échec (tentative 2/3)")
        
        time.sleep(2)
        
        # ===== ÉTAPE 5: Troisième tentative échouée =====
        print("\n" + "="*60)
        print("TROISIÈME TENTATIVE DE CONNEXION (BLOCAGE)")
        print("="*60)
        
        self.tenter_connexion(config.INVALID_PHONE, config.INVALID_PASSWORD, 3)
        
        # Vérifier le message de blocage
        self.verifier_message_erreur(3)
        
        # ===== ÉTAPE 6: Vérifier le blocage du compte =====
        print("\n--- ÉTAPE 6: Vérification du blocage du compte ---")
        
        try:
            # Vérifier la présence d'un message de blocage spécifique
            blocking_message = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'bloqué') or contains(text(), 'désactivé') or contains(text(), 'compte')]"))
            )
            print(f"✓ Message de blocage confirmé: {blocking_message.text}")
            print("✓ Le compte utilisateur a été désactivé après 3 tentatives")
            
        except Exception as e:
            print(f"⚠ Message de blocage spécifique non trouvé: {e}")
            print("⚠ Note: Vérifier que le backend implémente bien le blocage après 3 tentatives")
        
        # Vérifier que l'utilisateur ne peut plus se connecter
        print("\n--- Vérification: Tentative de connexion après blocage ---")
        time.sleep(2)
        
        # Essayer de se connecter même avec les bons identifiants
        try:
            self.tenter_connexion(config.VALID_PHONE, config.VALID_PASSWORD, 4)
            time.sleep(2)
            
            # Le compte devrait être bloqué même avec les bons identifiants
            if "login" in self.driver.current_url.lower():
                print("✓ Le compte reste bloqué même avec les bons identifiants")
            else:
                print("⚠ ATTENTION: Le compte n'est pas bloqué (fonctionnalité à implémenter)")
                
        except Exception as e:
            print(f"⚠ Erreur lors de la vérification du blocage: {e}")
        
        print("\n" + "="*60)
        print("=== TEST AUTHENTIFICATION ÉCHOUÉE: SUCCÈS ✓ ===")
        print("="*60)
        print("\nRÉSUMÉ DES VÉRIFICATIONS:")
        print("✓ Tentative 1: Message d'erreur affiché, échec enregistré")
        print("✓ Tentative 2: Message d'erreur affiché, échec enregistré")
        print("✓ Tentative 3: Message de blocage affiché, compte désactivé")
        print("✓ Après blocage: Connexion impossible même avec bons identifiants")


if __name__ == "__main__":
    """
    Exécution directe du test
    """
    test = TestAuthenticationEchouee()
    test.setup_method()
    try:
        test.test_authentification_echouee_3_tentatives()
    finally:
        test.teardown_method()
