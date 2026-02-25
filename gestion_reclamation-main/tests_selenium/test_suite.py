"""
Suite de tests complète pour l'authentification
Exécute tous les tests d'authentification
"""

import pytest
import sys
import os

# Ajouter le répertoire courant au path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from test_auth_reussie import TestAuthenticationReussie
from test_auth_echouee import TestAuthenticationEchouee


class TestSuiteAuthentication:
    """
    Suite de tests complète pour l'authentification
    """
    
    def test_01_authentification_reussie(self):
        """
        Test 1: Authentification réussie
        """
        print("\n" + "="*80)
        print("EXÉCUTION DU TEST 1: AUTHENTIFICATION RÉUSSIE")
        print("="*80)
        
        test = TestAuthenticationReussie()
        test.setup_method()
        try:
            test.test_authentification_reussie()
        finally:
            test.teardown_method()
    
    def test_02_authentification_echouee(self):
        """
        Test 2: Authentification échouée avec 3 tentatives
        """
        print("\n" + "="*80)
        print("EXÉCUTION DU TEST 2: AUTHENTIFICATION ÉCHOUÉE")
        print("="*80)
        
        test = TestAuthenticationEchouee()
        test.setup_method()
        try:
            test.test_authentification_echouee_3_tentatives()
        finally:
            test.teardown_method()


if __name__ == "__main__":
    """
    Exécution de la suite de tests avec pytest
    """
    pytest.main([
        __file__,
        "-v",  # Mode verbose
        "--html=rapport_tests.html",  # Génération d'un rapport HTML
        "--self-contained-html"  # Rapport HTML autonome
    ])
