import unittest
from unittest.mock import patch

def obtenir_infos_utilisateur(nom, age_input, pi_input):
   
    # Vérification de l'âge
    if not age_input.isdigit():
        raise ValueError("L'âge doit être un nombre entier positif.")
    age = int(age_input)

    # Vérification de la valeur de PI
    pi_input = pi_input.replace(",", ".")  # Supporte la virgule
    pi = float(pi_input)
    if not (3.14 <= pi <= 3.1416):
        raise ValueError("La valeur de PI doit être réaliste (ex: 3.141592).")

    return nom, age, pi
