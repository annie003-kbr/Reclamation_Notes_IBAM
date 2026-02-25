"""
Test Simple pour Diagnostiquer
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("=== TEST SIMPLE ===\n")

# Configuration Chrome
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Ouvrir Chrome
print("1. Ouverture de Chrome...")
driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    # Aller sur la page
    print("2. Navigation vers http://localhost:3000/login")
    driver.get("http://localhost:3000/login")
    time.sleep(5)
    
    print(f"✓ Page chargée: {driver.current_url}")
    print(f"✓ Titre: {driver.title}")
    
    # Afficher le HTML de la page
    print("\n3. Recherche des éléments...")
    
    # Essayer de trouver le formulaire
    try:
        # Chercher tous les inputs
        inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"✓ Nombre d'inputs trouvés: {len(inputs)}")
        
        for i, inp in enumerate(inputs):
            name = inp.get_attribute("name")
            type_attr = inp.get_attribute("type")
            print(f"  Input {i+1}: name='{name}', type='{type_attr}'")
        
        # Chercher les boutons
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"\n✓ Nombre de boutons trouvés: {len(buttons)}")
        
        for i, btn in enumerate(buttons):
            text = btn.text
            type_attr = btn.get_attribute("type")
            print(f"  Button {i+1}: text='{text}', type='{type_attr}'")
        
        print("\n✅ TEST RÉUSSI - La page se charge correctement!")
        
    except Exception as e:
        print(f"\n❌ Erreur lors de la recherche: {e}")
    
    time.sleep(3)
    
except Exception as e:
    print(f"\n❌ ERREUR: {e}")

finally:
    print("\n4. Fermeture du navigateur...")
    driver.quit()
    print("✓ Terminé")
