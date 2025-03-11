import unittest
from e4_main import convertir_en_nombre, somme

class TestFonctionsSomme(unittest.TestCase):

    def test_conversion_nombre(self):
        # Test de conversion des chaînes en nombres.
        self.assertEqual(convertir_en_nombre("42"), 42)
        self.assertEqual(convertir_en_nombre("3.14"), 3.14)
        self.assertEqual(convertir_en_nombre("  100  "), 100)
        self.assertEqual(convertir_en_nombre("3,1416"), 3.1416)

    def test_conversion_chaine(self):
        # Test des entrées qui restent des chaînes.
        self.assertEqual(convertir_en_nombre("hello"), "hello")
        self.assertEqual(convertir_en_nombre("42a"), "42a")

    def test_somme_nombres(self):
        # Test de l'addition de nombres.
        self.assertEqual(somme(3, 4), 7)
        self.assertEqual(somme(2.5, 1.5), 4.0)

    def test_somme_concatenation(self):
        # Test de la concaténation des chaînes.
        self.assertEqual(somme("hello", "world"), "hello world")
        self.assertEqual(somme(10, "chat"), "10 chat")
        self.assertEqual(somme("chien", 7), "chien 7")

if __name__ == "__main__":
    unittest.main(verbosity=2)
