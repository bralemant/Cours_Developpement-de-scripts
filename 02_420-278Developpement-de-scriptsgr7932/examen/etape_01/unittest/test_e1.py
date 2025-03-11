import unittest
from e1_main import obtenir_infos_utilisateur  # Importamos la función desde main.py

class TestSaisieUtilisateur(unittest.TestCase):
    def test_entrees_valides(self):
        #Test avec des entrées valides.
        result = obtenir_infos_utilisateur("Alice", "25", "3.1415")
        self.assertEqual(result, ("Alice", 25, 3.1415))

    def test_age_invalide(self):
        #Test avec un âge invalide (non numérique).
        with self.assertRaises(ValueError):
            obtenir_infos_utilisateur("Bob", "abc", "3.14")

    def test_pi_invalide(self):
        # Test avec une valeur de PI hors des limites acceptées.
        with self.assertRaises(ValueError):
            obtenir_infos_utilisateur("Charlie", "30", "3.2")

    def test_pi_avec_virgule(self):
        # Test si la virgule est bien convertie en point pour PI.
        result = obtenir_infos_utilisateur("David", "40", "3,1415")
        self.assertEqual(result, ("David", 40, 3.1415))

if __name__ == "__main__":
    unittest.main(verbosity=2)
