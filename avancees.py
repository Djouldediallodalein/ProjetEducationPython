## Fichier pour les fonctionnalités avancées : badges, révisions, analyse

import json
from datetime import datetime, timedelta
from progression import charger_progression, sauvegarder_progression


# Définition des badges disponibles
BADGES = {
    'premier_pas': {'nom': 'Premier Pas', 'desc': 'Réussir votre premier exercice', 'condition': lambda p: p['exercices_reussis'] >= 1},
    'debutant': {'nom': 'Débutant', 'desc': 'Réussir 5 exercices', 'condition': lambda p: p['exercices_reussis'] >= 5},
    'apprenti': {'nom': 'Apprenti', 'desc': 'Réussir 10 exercices', 'condition': lambda p: p['exercices_reussis'] >= 10},
    'competent': {'nom': 'Compétent', 'desc': 'Réussir 25 exercices', 'condition': lambda p: p['exercices_reussis'] >= 25},
    'expert': {'nom': 'Expert', 'desc': 'Réussir 50 exercices', 'condition': lambda p: p['exercices_reussis'] >= 50},
    'maitre': {'nom': 'Maître', 'desc': 'Réussir 100 exercices', 'condition': lambda p: p['exercices_reussis'] >= 100},
    'perfectionniste': {'nom': 'Perfectionniste', 'desc': 'Atteindre 90% de taux de réussite avec au moins 20 exercices', 'condition': lambda p: p['exercices_totaux'] >= 20 and (p['exercices_reussis'] / p['exercices_totaux']) >= 0.9},
    'explorateur': {'nom': 'Explorateur', 'desc': 'Essayer 5 thèmes différents', 'condition': lambda p: len(p.get('themes', {})) >= 5},
    'specialiste': {'nom': 'Spécialiste', 'desc': 'Réussir 10 exercices dans un seul thème', 'condition': lambda p: any(stats['reussis'] >= 10 for stats in p.get('themes', {}).values())},
}


def verifier_nouveaux_badges():
    """Vérifie et attribue les nouveaux badges gagnés"""
    progression = charger_progression()
    
    if 'badges' not in progression:
        progression['badges'] = []
    
    nouveaux_badges = []
    
    for badge_id, badge_info in BADGES.items():
        if badge_id not in progression['badges']:
            if badge_info['condition'](progression):
                progression['badges'].append(badge_id)
                nouveaux_badges.append(badge_info['nom'])
    
    if nouveaux_badges:
        sauvegarder_progression(progression)
    
    return nouveaux_badges


def afficher_badges():
    """Affiche tous les badges de l'utilisateur"""
    progression = charger_progression()
    badges_obtenus = progression.get('badges', [])
    
    print("\nVOS BADGES")
    print("="*60)
    
    if badges_obtenus:
        for badge_id in badges_obtenus:
            if badge_id in BADGES:
                badge = BADGES[badge_id]
                print(f"  {badge['nom']} - {badge['desc']}")
    else:
        print("Aucun badge obtenu pour le moment.")
    
    print("\nBADGES DISPONIBLES")
    print("-"*60)
    for badge_id, badge in BADGES.items():
        if badge_id not in badges_obtenus:
            print(f"  [ ] {badge['nom']} - {badge['desc']}")


def analyser_faiblesses():
    """Analyse les thèmes où l'utilisateur a le plus de difficultés"""
    progression = charger_progression()
    themes = progression.get('themes', {})
    
    if not themes:
        return None
    
    faiblesses = []
    for theme, stats in themes.items():
        if stats['totaux'] >= 3:
            taux = stats['reussis'] / stats['totaux']
            if taux < 0.5:
                faiblesses.append((theme, taux))
    
    faiblesses.sort(key=lambda x: x[1])
    return faiblesses[:3] if faiblesses else None


def suggerer_theme_revision():
    """Suggère un thème à réviser basé sur les faiblesses"""
    faiblesses = analyser_faiblesses()
    
    if faiblesses:
        return faiblesses[0][0]
    
    progression = charger_progression()
    themes = progression.get('themes', {})
    
    if themes:
        theme_moins_pratique = min(themes.items(), key=lambda x: x[1]['totaux'])
        return theme_moins_pratique[0]
    
    return None
