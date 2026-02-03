import json
import os
from datetime import datetime


FICHIER_PROGRESSION = 'progression_utilisateur.json'



def initialiser_progression():
    """Crée la structure de progression initiale pour un nouvel utilisateur"""
    return {
        'niveau': 1,
        'exercices_reussis': 0,
        'exercices_totaux': 0,
        'themes': {},
        'exercices_completes': [],
        'badges': [],
        'date_creation': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    


def charger_progression():
    """Charge la progression depuis le fichier JSON ou crée une nouvelle progression"""
    if os.path.exists(FICHIER_PROGRESSION):
        with open(FICHIER_PROGRESSION, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return initialiser_progression()




def sauvegarder_progression(progression):
    """Sauvegarde la progression dans le fichier JSON"""
    with open(FICHIER_PROGRESSION, 'w', encoding='utf-8') as f:
        json.dump(progression, f, indent=4, ensure_ascii=False)



def mettre_a_jour_progression(theme, reussi):
    """Met à jour la progression après un exercice"""
    progression = charger_progression()
    
    # Mise à jour des compteurs globaux
    progression['exercices_totaux'] += 1
    if reussi:
        progression['exercices_reussis'] += 1
    
    # Mise à jour par thème
    if theme not in progression['themes']:
        progression['themes'][theme] = {'reussis': 0, 'totaux': 0}
    
    progression['themes'][theme]['totaux'] += 1
    if reussi:
        progression['themes'][theme]['reussis'] += 1
    
    # Augmentation du niveau tous les 5 exercices réussis
    if progression['exercices_reussis'] % 5 == 0 and reussi:
        progression['niveau'] += 1
        print(f"\nNIVEAU SUPÉRIEUR ! Vous êtes maintenant au niveau {progression['niveau']} !")
    
    sauvegarder_progression(progression)
    return progression



def afficher_progression():
    """Affiche les statistiques de progression de l'utilisateur"""
    progression = charger_progression()
    

    print("VOTRE PROGRESSION")
    print(f"Niveau actuel : {progression['niveau']}")
    print(f"Exercices réussis : {progression['exercices_reussis']}/{progression['exercices_totaux']}")
    
    if progression['exercices_totaux'] > 0:
        taux = (progression['exercices_reussis'] / progression['exercices_totaux']) * 100
        print(f"Taux de réussite : {taux:.1f}%")

    print("ROGRESSION PAR THÈME")
    
    if progression['themes']:
        for theme, stats in progression['themes'].items():
            taux_theme = (stats['reussis'] / stats['totaux']) * 100 if stats['totaux'] > 0 else 0
            print(f"{theme} : {stats['reussis']}/{stats['totaux']} ({taux_theme:.0f}%)")
    else:
        print("Aucun exercice effectué pour le moment.")
        
        


def marquer_exercice_complete(theme, niveau, exercice):
    """Marque un exercice comme complété pour éviter de le reproposer"""
    progression = charger_progression()
    
    if 'exercices_completes' not in progression:
        progression['exercices_completes'] = []
    
    exercice_str = str(exercice)[:50]
    identifiant = f"{theme}|{niveau}|{exercice_str}"
    
    if identifiant not in progression['exercices_completes']:
        progression['exercices_completes'].append(identifiant)
        sauvegarder_progression(progression)


def est_exercice_complete(theme, niveau, exercice):
    """Vérifie si un exercice a déjà été complété"""
    progression = charger_progression()
    
    if 'exercices_completes' not in progression:
        return False
    
    exercice_str = str(exercice)[:50]
    identifiant = f"{theme}|{niveau}|{exercice_str}"
    return identifiant in progression['exercices_completes']
    