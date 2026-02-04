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
        'streak_actuel': 0,
        'streak_record': 0,
        'derniere_connexion': datetime.now().strftime('%Y-%m-%d'),
        'date_creation': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'historique': []
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

def mettre_a_jour_streak():
    """Met à jour le streak quotidien de l'utilisateur"""
    progression = charger_progression()
    
    aujourd_hui = datetime.now().strftime('%Y-%m-%d')
    
    # Initialiser si nécessaire
    if 'streak_actuel' not in progression:
        progression['streak_actuel'] = 1
        progression['streak_record'] = 1
        progression['derniere_connexion'] = aujourd_hui
        sauvegarder_progression(progression)
        return 1, True
    
    derniere_connexion = progression.get('derniere_connexion', aujourd_hui)
    
    # Calculer la différence de jours
    date_derniere = datetime.strptime(derniere_connexion, '%Y-%m-%d')
    date_aujourd_hui = datetime.strptime(aujourd_hui, '%Y-%m-%d')
    diff_jours = (date_aujourd_hui - date_derniere).days
    
    if diff_jours == 0:
        # Même jour, pas de changement
        return progression['streak_actuel'], False
    elif diff_jours == 1:
        # Jour consécutif, on incrémente
        progression['streak_actuel'] += 1
        nouveau_streak = True
    else:
        # Streak cassé, on recommence à 1
        progression['streak_actuel'] = 1
        nouveau_streak = False
    
    # Mise à jour du record
    if progression['streak_actuel'] > progression.get('streak_record', 0):
        progression['streak_record'] = progression['streak_actuel']
    
    # Mise à jour de la date
    progression['derniere_connexion'] = aujourd_hui
    
    sauvegarder_progression(progression)
    
    return progression['streak_actuel'], nouveau_streak


def afficher_streak():
    """Affiche le streak actuel de l'utilisateur"""
    progression = charger_progression()
    streak = progression.get('streak_actuel', 0)
    record = progression.get('streak_record', 0)
    
    if streak > 0:
        print(f"\nSTREAK : {streak} jour{'s' if streak > 1 else ''} consecutif{'s' if streak > 1 else ''} !")
        if record > streak:
            print(f"Record : {record} jours")
        else:
            print("C'est votre record !")
    else:
        print("\nCommencez votre streak aujourd'hui !")


def ajouter_a_historique(theme, niveau, exercice, tentatives, reussi):
    """Ajoute un exercice complété à l'historique"""
    progression = charger_progression()
    
    if 'historique' not in progression:
        progression['historique'] = []
    
    exercice_str = str(exercice)[:100]
    
    entree = {
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'theme': theme,
        'niveau': niveau,
        'exercice': exercice_str,
        'tentatives': tentatives,
        'reussi': reussi
    }
    
    progression['historique'].append(entree)
    sauvegarder_progression(progression)


def afficher_historique(limite=10):
    """Affiche l'historique des derniers exercices"""
    progression = charger_progression()
    historique = progression.get('historique', [])
    
    if not historique:
        print("\nAucun exercice dans l'historique.")
        return
    
    print("\n" + "="*80)
    print("HISTORIQUE DES EXERCICES")
    print("="*80)
    
    # Afficher les derniers exercices (ordre inversé)
    for i, entree in enumerate(reversed(historique[-limite:]), 1):
        statut = "REUSSI" if entree['reussi'] else "PASSE"
        print(f"\n{i}. [{entree['date']}]")
        print(f"   Theme: {entree['theme']} | Niveau: {entree['niveau']}")
        print(f"   Exercice: {entree['exercice']}")
        print(f"   Tentatives: {entree['tentatives']} | Statut: {statut}")
    
    print("\n" + "="*80)
    print(f"Total d'exercices: {len(historique)}")
    

def afficher_statistiques_detaillees():
    """Affiche des statistiques détaillées basées sur l'historique"""
    progression = charger_progression()
    historique = progression.get('historique', [])
    
    if not historique:
        print("\nPas encore d'historique pour calculer des statistiques.")
        return
    
    print("\n" + "="*80)
    print("STATISTIQUES DETAILLEES")
    print("="*80)
    
    # Calculs des statistiques
    total = len(historique)
    reussis = sum(1 for h in historique if h['reussi'])
    tentatives_totales = sum(h['tentatives'] for h in historique)
    tentatives_moyennes = tentatives_totales / total if total > 0 else 0
    taux_reussite = (reussis / total) * 100 if total > 0 else 0
    
    # Statistiques par thème
    themes_stats = {}
    for h in historique:
        theme = h['theme']
        if theme not in themes_stats:
            themes_stats[theme] = {'total': 0, 'reussis': 0, 'tentatives': 0}
        themes_stats[theme]['total'] += 1
        if h['reussi']:
            themes_stats[theme]['reussis'] += 1
        themes_stats[theme]['tentatives'] += h['tentatives']
    
    print(f"\nExercices totaux: {total}")
    print(f"Exercices reussis: {reussis} ({taux_reussite:.1f}%)")
    print(f"Tentatives moyennes par exercice: {tentatives_moyennes:.1f}")
    
    print("\n" + "-"*80)
    print("STATISTIQUES PAR THEME")
    print("-"*80)
    
    for theme, stats in sorted(themes_stats.items(), key=lambda x: x[1]['total'], reverse=True):
        taux_theme = (stats['reussis'] / stats['total']) * 100 if stats['total'] > 0 else 0
        tentatives_moy_theme = stats['tentatives'] / stats['total'] if stats['total'] > 0 else 0
        print(f"\n{theme}:")
        print(f"  - Exercices: {stats['total']}")
        print(f"  - Reussis: {stats['reussis']} ({taux_theme:.1f}%)")
        print(f"  - Tentatives moyennes: {tentatives_moy_theme:.1f}")
    
    print("\n" + "="*80)    