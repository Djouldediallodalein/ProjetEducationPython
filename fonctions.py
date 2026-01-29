## Fichier contenant toutes les fonctions utilitaires pour l'application d'apprentissage

import ollama 


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

