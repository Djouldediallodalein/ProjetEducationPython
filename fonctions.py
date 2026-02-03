## Fichier contenant toutes les fonctions utilitaires pour l'application d'apprentissage

import ollama
import random 
import json
import os
from progression import est_exercice_complete

FICHIER_BANQUE = 'banque_exercices.json'

def charger_banque():
    """Charge la banque d'exercices depuis le fichier JSON"""
    if os.path.exists(FICHIER_BANQUE):
        with open(FICHIER_BANQUE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {}

def sauvegarder_banque(banque):
    """Sauvegarde la banque d'exercices dans le fichier JSON"""
    with open(FICHIER_BANQUE, 'w', encoding='utf-8') as f:
        json.dump(banque, f, indent=2, ensure_ascii=False)
        
        


def ajouter_exercice_banque(theme, niveau, exercice):
    """Ajoute un exercice généré par l'IA dans la banque s'il n'existe pas déjà"""
    banque = charger_banque()
    
    if theme not in banque:
        banque[theme] = {"1": [], "2": [], "3": []}
    
    niveau_str = str(niveau)
    if niveau_str not in banque[theme]:
        banque[theme][niveau_str] = []
    
    if exercice not in banque[theme][niveau_str]:
        banque[theme][niveau_str].append(exercice)
        sauvegarder_banque(banque)



def generer_exercice(niveau, theme):
    """Génère un exercice : d'abord depuis la banque (non complété), sinon via l'IA"""
    
    banque = charger_banque()
    niveau_str = str(niveau)
    
    if theme in banque and niveau_str in banque[theme] and banque[theme][niveau_str]:
        exercices_disponibles = [
            ex for ex in banque[theme][niveau_str] 
            if not est_exercice_complete(theme, niveau, str(ex))
        ]
        
        if exercices_disponibles:
            exercice = random.choice(exercices_disponibles)
            print("[Exercice depuis la banque]")
            return exercice
    
    print("[Generation par IA...]")
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
    exercice_ia = response['message']['content']
    
    exercice = {
        "type": "code",
        "enonce": exercice_ia
    }
    
    ajouter_exercice_banque(theme, niveau, exercice)
    
    return exercice



def afficher_qcm(exercice):
    """Affiche un QCM et retourne la réponse de l'utilisateur"""
    print(exercice['question'])
    print()
    
    for i, choix in enumerate(exercice['choix'], 1):
        print(f"{i}. {choix}")
    
    print()
    while True:
        try:
            reponse_num = int(input("Votre réponse (1-4) : "))
            if 1 <= reponse_num <= len(exercice['choix']):
                return exercice['choix'][reponse_num - 1]
            else:
                print("Choix invalide. Entrez un nombre entre 1 et 4.")
        except ValueError:
            print("Veuillez entrer un nombre.")



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
    
    correction_upper = correction.upper()
    
    if 'CORRECT' in correction_upper and 'INCORRECT' not in correction_upper:
        return True
    else:
        return False




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

