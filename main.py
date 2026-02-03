## Programme principal pour une application simple

from fonctions import generer_exercice, verifier_reponse, analyser_verdict, choisir_theme, afficher_qcm
from progression import charger_progression, mettre_a_jour_progression, afficher_progression, marquer_exercice_complete

progression = charger_progression()

niveau = progression['niveau']

    
if __name__ == "__main__":
    print("\nBienvenue dans l'apprentissage Python par exercices !")
    print("L'objectif est d'apprendre Python en resolvant des exercices par theme.")
    print("="*60)
    
    choix = 0
    
    while choix != 3:
        print("\nMENU PRINCIPAL")
        print("="*60)
        try:
            choix = int(input("Veuillez choisir une option :\n1. Commencer les exercices\n2. Voir ma progression\n3. Quitter\n\nVotre choix : "))
        except ValueError:
            print("Erreur : Entrez uniquement un numero (1, 2 ou 3)")
            continue
        
        if choix == 1:
            theme = choisir_theme()
            
            if theme is None:
                print("Retour au menu principal...")
                continue
            
            print("\n" + "="*60)
            print("EXERCICE")
            print("="*60)
            
            exercice = generer_exercice(niveau, theme)
            
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
                    verification = verifier_reponse(enonce, solution)
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
            
            if avancement:
                marquer_exercice_complete(theme, niveau, exercice)
            
            mettre_a_jour_progression(theme, avancement)
            
        elif choix == 2:
            afficher_progression()
            
        elif choix == 3:
            print("\n" + "="*60)
            print("Merci d'avoir utilise l'application !")
            print("A bientot pour de nouveaux exercices.")
            print("="*60)
            
        else:
            print("Erreur : Choix invalide. Veuillez choisir 1, 2 ou 3.")
                       
    
