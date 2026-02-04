## Programme principal pour une application simple

from gestion_erreurs import (
    initialiser_logging, log_info, log_erreur, log_avertissement,
    verifier_integrite_systeme, gestionnaire_erreur_global, menu_logs
)
from fonctions import generer_exercice, verifier_reponse, analyser_verdict, choisir_theme, afficher_qcm
from progression import (charger_progression, mettre_a_jour_progression, afficher_progression, 
                        marquer_exercice_complete, mettre_a_jour_streak, afficher_streak,
                        ajouter_a_historique, afficher_historique, afficher_statistiques_detaillees,
                        obtenir_domaine_actif, changer_domaine_actif, obtenir_progression_domaine)
from avancees import verifier_nouveaux_badges, afficher_badges, suggerer_theme_revision
from xp_systeme import calculer_xp, ajouter_xp, afficher_info_xp, afficher_details_xp_gagne
from utilisateurs import (
    initialiser_systeme_utilisateurs, menu_utilisateurs, 
    obtenir_utilisateur_actif, lister_utilisateurs, selectionner_utilisateur
)
from repetition_espacee import (
    enregistrer_revision, obtenir_exercices_a_reviser, 
    afficher_exercices_a_reviser, mode_revision, afficher_statistiques_srs
)
from export_import import menu_export_import
from domaines import choisir_domaine, obtenir_nom_domaine, charger_domaines

progression = charger_progression()

# Obtenir le domaine actif
domaine_actif = obtenir_domaine_actif()
prog_domaine = obtenir_progression_domaine(domaine_actif)
niveau = prog_domaine['niveau']

    
if __name__ == "__main__":
    # Initialiser le système de logs et gestion d'erreurs
    initialiser_logging()
    gestionnaire_erreur_global()
    log_info("Demarrage de l'application")
    
    # Vérifier l'intégrité du système
    if not verifier_integrite_systeme():
        print("\nProblemes detectes lors de la verification.")
        print("L'application peut ne pas fonctionner correctement.")
        continuer = input("\nContinuer quand meme ? (oui/non) : ")
        if continuer.lower() not in ['oui', 'o', 'yes', 'y']:
            print("Application interrompue.")
            exit(1)
    
    # Initialiser le système multi-utilisateurs
    initialiser_systeme_utilisateurs()
    
    # Vérifier si un utilisateur est sélectionné
    utilisateur_actif = obtenir_utilisateur_actif()
    
    if not utilisateur_actif:
        print("\n" + "="*60)
        print("BIENVENUE ! Aucun utilisateur selectionne.")
        print("="*60)
        print("\nVoulez-vous :")
        print("1. Creer un nouvel utilisateur")
        print("2. Selectionner un utilisateur existant")
        print("3. Continuer sans profil (mode classique)")
        
        try:
            choix_init = int(input("\nVotre choix : "))
            if choix_init == 1:
                nom = input("\nNom du nouvel utilisateur : ").strip()
                if nom:
                    from utilisateurs import creer_utilisateur
                    if creer_utilisateur(nom):
                        selectionner_utilisateur(nom)
                        utilisateur_actif = nom
            elif choix_init == 2:
                liste = lister_utilisateurs()
                if liste:
                    num = int(input("\nNumero de l'utilisateur : "))
                    if 1 <= num <= len(liste):
                        selectionner_utilisateur(liste[num - 1])
                        utilisateur_actif = liste[num - 1]
        except (ValueError, Exception) as e:
            print("\nContinuation en mode classique...")
    
    print("\nBienvenue dans l'apprentissage universel par exercices !")
    if utilisateur_actif:
        print(f"Utilisateur connecte : {utilisateur_actif}")
    
    # Afficher le domaine actif
    domaine_actif = obtenir_domaine_actif()
    nom_domaine = obtenir_nom_domaine(domaine_actif)
    print(f"Domaine d'apprentissage : {nom_domaine}")
    print("L'objectif est d'apprendre en resolvant des exercices par theme.")
    print("="*60)
    
    # Mise à jour et affichage du streak
    streak, nouveau = mettre_a_jour_streak()
    if streak > 1:
        print(f"\nSTREAK : {streak} jours consecutifs ! Continuez comme ca !")
    elif streak == 1:
        if nouveau:
            print(f"\nVotre streak demarre aujourd'hui ! Revenez demain pour continuer !")
        else:
            print(f"\nBon retour ! Votre streak a ete reinitialise.")
    
    # Suggérer un thème à réviser
    theme_suggere = suggerer_theme_revision()
    if theme_suggere:
        print(f"\nSuggestion : Revisez '{theme_suggere}' pour progresser !")
    
    # Afficher les exercices à réviser (SRS)
    exercices_a_reviser = obtenir_exercices_a_reviser()
    if exercices_a_reviser:
        print(f"\nATTENTION : {len(exercices_a_reviser)} exercice(s) a reviser aujourd'hui !")
    
    choix = 0
    
    while choix != 14:
        # Récupérer le domaine actif pour l'affichage
        domaine_actif = obtenir_domaine_actif()
        nom_domaine = obtenir_nom_domaine(domaine_actif)
        prog_domaine = obtenir_progression_domaine(domaine_actif)
        niveau = prog_domaine['niveau']
        
        print("\nMENU PRINCIPAL")
        print("="*60)
        print(f"🌍 Domaine actif : {nom_domaine} | Niveau : {niveau}")
        print("="*60)
        try:
            choix = int(input("Veuillez choisir une option :\n0. 🌐 CHANGER DE DOMAINE\n1. Commencer les exercices\n2. Voir ma progression\n3. Voir mes badges\n4. Voir l'historique\n5. Statistiques detaillees\n6. Systeme XP et niveaux\n7. Gestion des utilisateurs\n8. Mode Revision (SRS)\n9. Exercices a reviser\n10. Stats repetition espacee\n11. Sauvegardes (Export/Import)\n12. Consulter les logs\n13. Lister tous les domaines\n14. Quitter\n\nVotre choix : "))
        except ValueError:
            print("Erreur : Entrez uniquement un numero (0-14)")
            log_avertissement("Entree invalide dans le menu principal")
            continue
        except KeyboardInterrupt:
            print("\n\nInterruption detectee. Au revoir !")
            log_info("Application interrompue par l'utilisateur")
            break
        
        if choix == 0:
            # Changer de domaine
            print("\n" + "="*70)
            id_domaine, info_domaine = choisir_domaine()
            if id_domaine:
                changer_domaine_actif(id_domaine)
                domaine_actif = id_domaine
                nom_domaine = obtenir_nom_domaine(domaine_actif)
                print(f"\n✅ Domaine changé : {nom_domaine}")
                log_info(f"Changement de domaine : {id_domaine}")
            else:
                print("\nAucun changement effectué.")
        
        elif choix == 1:
            # Obtenir le domaine actif
            domaine_actif = obtenir_domaine_actif()
            prog_domaine = obtenir_progression_domaine(domaine_actif)
            niveau = prog_domaine['niveau']
            
            theme = choisir_theme(domaine_actif)
            
            if theme is None:
                print("Retour au menu principal...")
                continue
            
            print("\n" + "="*60)
            print("EXERCICE")
            print("="*60)
            
            exercice = generer_exercice(niveau, theme, domaine_actif)
            
            # Vérifier le type d'exercice
            if isinstance(exercice, dict) and exercice.get('type') == 'qcm':
                # C'est un QCM
                print(exercice['question'])
                print()
                for i, choix in enumerate(exercice['choix'], 1):
                    print(f"{i}. {choix}")
                print("\n" + "-"*60)
                
                avancement = False
                tentatives = 0
                exercice_passe = False
                
                while not avancement and not exercice_passe:
                    tentatives += 1
                    print(f"\nTentative {tentatives}")
                    
                    try:
                        reponse_num = int(input("\nVotre réponse (1-4) : "))
                        if 1 <= reponse_num <= len(exercice['choix']):
                            reponse_utilisateur = exercice['choix'][reponse_num - 1]
                            
                            if reponse_utilisateur == exercice['reponse']:
                                print("\nCORRECT ! Bravo !")
                                avancement = True
                            else:
                                print(f"\nINCORRECT. La bonne réponse était : {exercice['reponse']}")
                                if tentatives >= 3:
                                    choix_passer = input("\nVous avez fait 3 tentatives. Voulez-vous passer cet exercice ? (oui/non) : ")
                                    if choix_passer.lower() in ['oui', 'o', 'yes', 'y']:
                                        print("\nExercice passe. Aucun point attribue.")
                                        exercice_passe = True
                                    else:
                                        # Reset le compteur pour laisser l'utilisateur continuer
                                        tentatives = 0
                        else:
                            print("Choix invalide. Entrez un nombre entre 1 et 4.")
                            tentatives -= 1
                    except ValueError:
                        print("Veuillez entrer un nombre.")
                        tentatives -= 1
            
            else:
                # C'est un exercice de code
                enonce = exercice.get('enonce') if isinstance(exercice, dict) else exercice
                print(enonce)
                print("\n" + "-"*60)
                
                tentatives = 0
                avancement = False
                exercice_passe = False
                
                while not avancement and not exercice_passe:
                    tentatives += 1
                    print(f"\nTentative {tentatives}")
                    
                    solution = input("\nVeuillez entrer votre solution Python :\n")
                    
                    print("\n" + "="*60)
                    print("VERIFICATION")
                    print("="*60)
                    verification = verifier_reponse(enonce, solution, domaine_actif)
                    print(verification)
                    
                    avancement = analyser_verdict(verification)
                    
                    if avancement:
                        print("\nResultat : EXERCICE REUSSI !")
                    else:
                        print("\nResultat : Reessayez, vous pouvez y arriver !")
                        if tentatives >= 3:
                            choix_passer = input("\nVous avez fait 3 tentatives. Voulez-vous passer cet exercice ? (oui/non) : ")
                            if choix_passer.lower() in ['oui', 'o', 'yes', 'y']:
                                print("\nExercice passe. Aucun point attribue.")
                                exercice_passe = True
                            else:
                                # Reset le compteur pour laisser l'utilisateur continuer
                                tentatives = 0
            
            # Ajouter à l'historique (que ce soit réussi ou passé)
            ajouter_a_historique(theme, niveau, exercice, tentatives, avancement)
            
            # Enregistrer dans le système de répétition espacée
            enregistrer_revision(theme, niveau, exercice, avancement, tentatives)
            
            if avancement:
                marquer_exercice_complete(theme, niveau, exercice, domaine_actif)
                
                # Calculer et ajouter l'XP
                progression_actuelle = charger_progression()
                streak_actuel = progression_actuelle.get('streak_actuel', 0)
                type_ex = exercice.get('type', 'code') if isinstance(exercice, dict) else 'code'
                
                xp_gagne = calculer_xp(type_ex, niveau, tentatives, streak_actuel)
                niveau_avant, niveau_apres, niveau_monte = ajouter_xp(xp_gagne)
                
                # Afficher l'XP gagné
                afficher_details_xp_gagne(xp_gagne, type_ex, niveau, tentatives, streak_actuel)
                
                # Vérifier si de nouveaux badges sont gagnés
                nouveaux_badges = verifier_nouveaux_badges()
                if nouveaux_badges:
                    print(f"\n BADGE GAGNE : {', '.join(nouveaux_badges)} !")
                
                # Afficher la montée de niveau
                if niveau_monte:
                    print(f"\n" + "="*60)
                    print(f"NIVEAU SUPERIEUR ! Vous etes maintenant au niveau {niveau_apres} !")
                    print("="*60)
            
            mettre_a_jour_progression(theme, avancement, domaine_actif)
        
        elif choix == 2:
            domaine_actif = obtenir_domaine_actif()
            afficher_progression(domaine_actif)
            
        elif choix == 3:
            afficher_badges()
            
        elif choix == 4:
            afficher_historique()
            
        elif choix == 5:
            afficher_statistiques_detaillees()
            
        elif choix == 6:
            afficher_info_xp()
            
        elif choix == 7:
            menu_utilisateurs()
            
        elif choix == 8:
            mode_revision()
            
        elif choix == 9:
            afficher_exercices_a_reviser()
            
        elif choix == 10:
            afficher_statistiques_srs()
            
        elif choix == 11:
            menu_export_import()
            
        elif choix == 12:
            menu_logs()
        
        elif choix == 13:
            # Lister tous les domaines disponibles
            print("\n" + "="*70)
            print("🌍 DOMAINES DISPONIBLES".center(70))
            print("="*70)
            domaines = charger_domaines()
            domaines_tries = sorted(domaines.items(), key=lambda x: x[1].get('popularite', 99))
            
            for i, (id_dom, info) in enumerate(domaines_tries, 1):
                emoji = info.get('emoji', '📚')
                nom = info['nom']
                type_dom = info.get('type', 'Divers')
                description = info.get('description', '')
                nb_themes = len(info.get('themes', []))
                print(f"\n{i}. {emoji} {nom}")
                print(f"   Type : {type_dom}")
                print(f"   Description : {description}")
                print(f"   Thèmes disponibles : {nb_themes}")
            
            print("\n" + "="*70)
            input("\nAppuyez sur Entrée pour continuer...")
        
        elif choix == 14:
            log_info("Application fermee normalement")
            print("\n" + "="*60)
            print("Merci d'avoir utilise l'application !")
            print("A bientot pour de nouveaux exercices.")
            print("="*60)
            
        else:
            print("Erreur : Choix invalide. Veuillez choisir entre 1 et 13.")
                       
    
