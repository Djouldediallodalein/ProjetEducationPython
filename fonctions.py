## Fichier contenant toutes les fonctions utilitaires pour l'application d'apprentissage

import ollama
import random 


def generer_exercice(niveau, theme):
    """ Cette fonction permet de demander à l'IA de generer un exercice en fonction du niveau.
    
    """
    messages = [
    {
        'role': 'user',
        'content' : f'''Tu es un professeur de Python. Crée un exercice de niveau {niveau} sur : {theme}

IMPORTANT : 
- Donne UNIQUEMENT l\'énoncé de l\'exercice (2-3 phrases maximum)
- NE donne PAS la solution
- NE donne PAS d\'exemple de code
- NE donne PAS d\'explications

Exemple : "Écrivez une fonction qui prend un nombre en paramètre et retourne True s\'il est pair, False sinon."

Énoncé :'''
    }
]
    response = ollama.chat(model='qwen2.5-coder:14b', messages = messages)
    return response['message']['content']





def verifier_reponse(exercice, reponse_utilisateur):
    """ Cette fonction permet de verifier la reponse de l'utilisateur"""
    
    messages = [
    {
        'role': 'user',
        'content': f'''Tu es un correcteur STRICT de code Python.

EXERCICE :
{exercice}

CODE DE L\'ÉLÈVE :
{reponse_utilisateur}

RÈGLES DE CORRECTION :
1. Vérifie que c\'est du CODE PYTHON (pas juste du texte ou l\'énoncé recopié)
2. Vérifie que le code répond EXACTEMENT à la question
3. Si ce n\'est PAS du code Python → INCORRECT
4. Si le code ne résout pas l\'exercice → INCORRECT

Réponse (15 mots max) :
- Si CORRECT : "CORRECT : Bravo !"
- Si INCORRECT : "INCORRECT : [raison courte]. Indice : [2-3 mots]"'''
    }
]
    
    correction = ollama.chat(model='qwen2.5-coder:14b', messages = messages)
    return correction['message']['content']
    





def analyser_verdict(correction):
    """Cette fonction permet de gerer le verdict de l'ia sur la reponse de l'etudiant"""
    
    avancer = False
    messages = [
    {
        'role': 'user',
        'content': f'''Voici la correction d\'un exercice :

{correction}

RÉPONDS UNIQUEMENT PAR UN SEUL MOT : BON ou MAUVAIS
BON = si le code de l\'élève est correct
MAUVAIS = si le code est incorrect

Pas d\'explication, juste UN mot : BON ou MAUVAIS'''
    }
]
    
    reponse = ollama.chat(model='qwen2.5-coder:14b', messages = messages)
    reponse_ia = reponse['message']['content']
    
    if 'BON' in reponse_ia.upper():
        avancer = True
    elif 'MAUVAIS' in reponse_ia.upper():
        avancer = False
    else:
        print("L'IA a mal formulé sa réponse entre BON et MAUVAIS")
        print(f"Réponse reçue : {reponse_ia}")
    
    return avancer




def choisir_theme_aleatoire():
    """Retourne un thème aléatoire parmi les 10 thèmes disponibles"""
    themes = [
        'Variables et types de données',
        'Conditions (if/elif/else)',
        'Boucles (for/while)',
        'Fonctions',
        'Listes et tuples',
        'Dictionnaires',
        'Manipulation de strings',
        'Fichiers (lecture/écriture)',
        'Gestion des erreurs (try/except)',
        'Programmation orientée objet (classes)'
    ]
    theme_selectionne = random.choice(themes)
    print(f"Theme aleatoire selectionne : {theme_selectionne}")
    return theme_selectionne



def choisir_theme():
    """Permet à l'utilisateur de choisir un thème d'exercice"""
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
        '10': 'Programmation orientée objet (classes)'
    }
    
    print("\nCHOIX DU THEME D'APPRENTISSAGE")
    print("="*50)
    
    for key, value in themes_disponibles.items():
        print(f"{key}. {value}")
    
    print("\n11. Theme aleatoire")
    print("0. Retour au menu principal")
    print("="*50)
    
    choix_theme = input("\nChoisissez un theme (1-11 ou 0 pour retourner) : ")
    
    if choix_theme == '0':
        return None
    elif choix_theme == '11':
        return choisir_theme_aleatoire()
    elif choix_theme in themes_disponibles:
        theme_selectionne = themes_disponibles[choix_theme]
        print(f"Theme selectionne : {theme_selectionne}")
        return theme_selectionne
    else:
        print("Choix invalide ! Veuillez reessayer.")
        return choisir_theme()

