"""
Script de Démonstration avec Captures d'Écran
Ce script exécute les tests et prend des captures d'écran à chaque étape
"""

import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import config


class DemonstrationTests:
    """
    Classe pour démonstration avec captures d'écran
    """
    
    def __init__(self):
        """Initialisation"""
        self.driver = None
        self.wait = None
        self.screenshot_dir = "screenshots"
        self.screenshot_counter = 1
        
        # Créer le dossier screenshots s'il n'existe pas
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
            print(f"✓ Dossier '{self.screenshot_dir}' créé")
    
    def setup(self):
        """Configuration du navigateur"""
        print("\n" + "="*80)
        print("INITIALISATION DU NAVIGATEUR")
        print("="*80)
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(config.IMPLICIT_WAIT)
        self.wait = WebDriverWait(self.driver, config.EXPLICIT_WAIT)
        
        print("✓ Navigateur Chrome initialisé")
        print("✓ Fenêtre maximisée")
    
    def teardown(self):
        """Fermeture du navigateur"""
        print("\n" + "="*80)
        print("FERMETURE DU NAVIGATEUR")
        print("="*80)
        time.sleep(2)
        self.driver.quit()
        print("✓ Navigateur fermé")
    
    def take_screenshot(self, description):
        """
        Prendre une capture d'écran avec description
        
        Args:
            description: Description de la capture
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.screenshot_counter:02d}_{description}_{timestamp}.png"
        filepath = os.path.join(self.screenshot_dir, filename)
        
        self.driver.save_screenshot(filepath)
        print(f"📸 Capture d'écran sauvegardée: {filename}")
        
        self.screenshot_counter += 1
        time.sleep(1)
    
    def demo_authentification_reussie(self):
        """
        Démonstration: Authentification réussie
        """
        print("\n" + "="*80)
        print("DÉMONSTRATION 1: AUTHENTIFICATION RÉUSSIE")
        print("="*80)
        
        # Étape 1: Navigation
        print("\n--- Étape 1: Navigation vers la page de connexion ---")
        self.driver.get(f"{config.BASE_URL}/login")
        time.sleep(2)
        self.take_screenshot("01_page_connexion")
        print(f"✓ URL: {self.driver.current_url}")
        
        # Étape 2: Formulaire visible
        print("\n--- Étape 2: Vérification du formulaire ---")
        try:
            phone_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            password_input = self.driver.find_element(By.NAME, "password")
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            
            print("✓ Champ téléphone/email trouvé")
            print("✓ Champ mot de passe trouvé")
            print("✓ Bouton de connexion trouvé")
            
            self.take_screenshot("02_formulaire_vide")
            
        except Exception as e:
            print(f"✗ Erreur: {e}")
            self.take_screenshot("02_erreur_formulaire")
            return
        
        # Étape 3: Remplissage du formulaire
        print("\n--- Étape 3: Remplissage avec identifiants valides ---")
        phone_input.clear()
        phone_input.send_keys(config.VALID_PHONE)
        print(f"✓ Téléphone saisi: {config.VALID_PHONE}")
        time.sleep(1)
        
        password_input.clear()
        password_input.send_keys(config.VALID_PASSWORD)
        print(f"✓ Mot de passe saisi: {'*' * len(config.VALID_PASSWORD)}")
        time.sleep(1)
        
        self.take_screenshot("03_formulaire_rempli")
        
        # Étape 4: Soumission
        print("\n--- Étape 4: Soumission du formulaire ---")
        login_button.click()
        print("✓ Formulaire soumis")
        time.sleep(3)
        
        self.take_screenshot("04_apres_soumission")
        
        # Étape 5: Vérification connexion
        print("\n--- Étape 5: Vérification de la connexion ---")
        try:
            self.wait.until(
                lambda driver: "login" not in driver.current_url.lower()
            )
            print(f"✓ Connexion réussie!")
            print(f"✓ URL actuelle: {self.driver.current_url}")
            
            self.take_screenshot("05_connexion_reussie")
            
        except Exception as e:
            print(f"⚠ Erreur de connexion: {e}")
            self.take_screenshot("05_erreur_connexion")
        
        print("\n✅ DÉMONSTRATION 1 TERMINÉE")
    
    def demo_authentification_echouee(self):
        """
        Démonstration: Authentification échouée avec 3 tentatives
        """
        print("\n" + "="*80)
        print("DÉMONSTRATION 2: AUTHENTIFICATION ÉCHOUÉE (3 TENTATIVES)")
        print("="*80)
        
        # Réinitialiser le compteur de screenshots
        self.screenshot_counter = 1
        
        # Navigation
        print("\n--- Navigation vers la page de connexion ---")
        self.driver.get(f"{config.BASE_URL}/login")
        time.sleep(2)
        self.take_screenshot("01_page_connexion")
        
        # Tentatives échouées
        for tentative in range(1, 4):
            print("\n" + "="*60)
            print(f"TENTATIVE {tentative}/3")
            print("="*60)
            
            try:
                # Trouver les éléments
                phone_input = self.driver.find_element(By.NAME, "email")
                password_input = self.driver.find_element(By.NAME, "password")
                login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
                
                # Remplir le formulaire
                phone_input.clear()
                phone_input.send_keys(config.INVALID_PHONE)
                time.sleep(0.5)
                
                password_input.clear()
                password_input.send_keys(config.INVALID_PASSWORD)
                time.sleep(0.5)
                
                self.take_screenshot(f"0{tentative+1}_tentative_{tentative}_formulaire")
                
                # Soumettre
                login_button.click()
                print(f"✓ Tentative {tentative} soumise")
                time.sleep(2)
                
                # Capture après soumission
                self.take_screenshot(f"0{tentative+2}_tentative_{tentative}_resultat")
                
                # Vérifier le message d'erreur
                try:
                    error_element = self.wait.until(
                        EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'error') or contains(@class, 'alert')]"))
                    )
                    print(f"✓ Message d'erreur: {error_element.text}")
                except:
                    print("⚠ Message d'erreur non trouvé")
                
                if tentative == 3:
                    print("\n🔒 COMPTE BLOQUÉ APRÈS 3 TENTATIVES")
                    self.take_screenshot("07_compte_bloque")
                
                time.sleep(2)
                
            except Exception as e:
                print(f"✗ Erreur lors de la tentative {tentative}: {e}")
                self.take_screenshot(f"erreur_tentative_{tentative}")
        
        # Tentative avec bons identifiants (devrait échouer car bloqué)
        print("\n" + "="*60)
        print("VÉRIFICATION: Tentative avec bons identifiants")
        print("="*60)
        
        try:
            phone_input = self.driver.find_element(By.NAME, "email")
            password_input = self.driver.find_element(By.NAME, "password")
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            
            phone_input.clear()
            phone_input.send_keys(config.VALID_PHONE)
            password_input.clear()
            password_input.send_keys(config.VALID_PASSWORD)
            
            self.take_screenshot("08_tentative_apres_blocage")
            
            login_button.click()
            time.sleep(2)
            
            self.take_screenshot("09_resultat_apres_blocage")
            
            if "login" in self.driver.current_url.lower():
                print("✓ Le compte reste bloqué même avec bons identifiants")
            else:
                print("⚠ Le compte n'est pas bloqué (fonctionnalité à implémenter)")
                
        except Exception as e:
            print(f"⚠ Erreur: {e}")
        
        print("\n✅ DÉMONSTRATION 2 TERMINÉE")
    
    def run_all_demos(self):
        """
        Exécuter toutes les démonstrations
        """
        print("\n" + "="*80)
        print("DÉMARRAGE DES DÉMONSTRATIONS")
        print("="*80)
        print(f"📁 Les captures d'écran seront sauvegardées dans: {self.screenshot_dir}/")
        
        self.setup()
        
        try:
            # Démo 1
            self.demo_authentification_reussie()
            time.sleep(3)
            
            # Démo 2
            self.demo_authentification_echouee()
            
        except Exception as e:
            print(f"\n❌ ERREUR GLOBALE: {e}")
            self.take_screenshot("erreur_globale")
        
        finally:
            self.teardown()
        
        print("\n" + "="*80)
        print("TOUTES LES DÉMONSTRATIONS TERMINÉES")
        print("="*80)
        print(f"📸 Consultez les captures d'écran dans: {self.screenshot_dir}/")


if __name__ == "__main__":
    """
    Exécution des démonstrations
    """
    demo = DemonstrationTests()
    demo.run_all_demos()
