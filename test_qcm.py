## Test rapide du système QCM

from fonctions import generer_exercice
from progression import charger_progression

progression = charger_progression()
niveau = progression['niveau']
theme = "Variables et types de données"

print("Test de génération d'exercice:")
exercice = generer_exercice(niveau, theme)

print("\nType d'exercice:", type(exercice))
print("\nContenu:")
print(exercice)

if isinstance(exercice, dict):
    print("\nType détecté:", exercice.get('type'))
    if exercice.get('type') == 'qcm':
        print("C'est bien un QCM !")
        print("Question:", exercice.get('question'))
        print("Choix:", exercice.get('choix'))
        print("Réponse correcte:", exercice.get('reponse'))
