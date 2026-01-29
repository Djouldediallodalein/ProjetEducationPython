## Programme principal pour une application simple

from fonctions import generer_exercice, verifier_reponse, analyser_verdict

niveau = 2

# Liste des thèmes disponibles
themes_disponibles = {
    '1': 'Variables et types de données',
    '2': 'Conditions (if/elif/else)',
    '3': 'Boucles (for/while)',
    '4': 'Fonctions',
    '5': 'Listes et tuples',
    '6': 'Dictionnaires',
    '7': 'Manipulation de strings',
    '8': 'Fichiers (lecture/écriture)',
    '9': 'Gestion des erreurs (try/except)',
    '10': 'Programmation orientée objet (classes)',
    '0': 'Thème personnalisé'
}

def choisir_theme():
    """Permet à l'utilisateur de choisir un thème d'exercice"""
    print("L'objectif est d'apprendre python en resolvant des exos par theme.\nCHOIX DU THÈME D'APPRENTISSAGE")
    
    for key, value in themes_disponibles.items():
        if key == '0':
            print(f"\n{key}.{value}")
        else:
            print(f"{key}.{value}")
    
    print("="*50)
    
    choix_theme = input("\nChoisissez un thème (1-10 ou 0 pour personnaliser) : ")
    
    if choix_theme in themes_disponibles and choix_theme != '0':
        theme_selectionne = themes_disponibles[choix_theme]
        print(f"Thème sélectionné : {theme_selectionne}")
        return theme_selectionne
    elif choix_theme == '0':
        theme_personnalise = input("Entrez votre thème personnalisé : ")
        print(f"Thème personnalisé : {theme_personnalise}")
        return theme_personnalise
    else:
        print("Choix invalide ! Thème par défaut : Conditions")
        return "Conditions (if/elif/else)"

# Sélection du thème au démarrage
theme = choisir_theme()

    
if __name__ == "__main__":
    print("Bienvenue !")
    choix = 0
    
    while choix != 3 :
        try:
            choix = int(input("Veillez choisir une option :\n1. Commencer les exercices\n2. Voir ma progression\n3. Quitter\n"))
        except ValueError:
            print("Entrez juste le numéro (1, 2 ou 3)")
            continue
        print("Vous avez choisi :", choix)
        
        if choix == 1 :
            print("Lancement des exercices")
            
            exercice = generer_exercice(niveau, theme) # On génére l'exercice
            print(exercice)
            
            solution = input("veillez entrer la solution de l'exercice :")
            print("\nVoici la verification :\n")
            verification = verifier_reponse(exercice,solution)
            print(verification)
            
            avancement = analyser_verdict(verification)
            print(avancement)
            
            
        elif choix == 2 : 
            print("Affichage de la progression") 
        elif choix == 3 : 
            print("Au revoir")
        else :
            print("Choix Invalide")
                       
    
