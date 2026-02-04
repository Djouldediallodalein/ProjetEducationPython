"""
Test d'intégration simple: vérifier que tous les modules peuvent être chargés
et que les fonctions menu existent
"""

import sys


def test_import_modules():
    """Test l'importation de tous les modules d'amélioration"""
    print("\n" + "="*70)
    print("🧪 TEST D'INTÉGRATION - IMPORTATION DES MODULES")
    print("="*70)
    
    modules_a_tester = [
        ('defis_quotidiens', 'menu_defis'),
        ('comparaison_domaines', 'menu_comparaison'),
        ('classement', 'menu_classement'),
        ('quetes', 'menu_quetes'),
        ('export_avance', 'menu_export_avance'),
        ('themes', 'menu_themes'),
        ('notifications', 'menu_notifications'),
        ('mode_hors_ligne', 'menu_mode_hors_ligne'),
        ('analytics', 'menu_analytics'),
        ('collaboratif', 'menu_collaboratif')
    ]
    
    resultats = []
    
    for nom_module, nom_fonction in modules_a_tester:
        try:
            # Importer le module
            module = __import__(nom_module)
            
            # Vérifier que la fonction menu existe
            if hasattr(module, nom_fonction):
                print(f"✅ {nom_module:<25} - Import OK + fonction {nom_fonction} trouvée")
                resultats.append(True)
            else:
                print(f"⚠️  {nom_module:<25} - Import OK mais fonction {nom_fonction} manquante")
                resultats.append(False)
                
        except ImportError as e:
            print(f"❌ {nom_module:<25} - Erreur d'import: {e}")
            resultats.append(False)
        except Exception as e:
            print(f"❌ {nom_module:<25} - Erreur: {e}")
            resultats.append(False)
    
    print("\n" + "="*70)
    reussis = sum(resultats)
    total = len(resultats)
    print(f"📊 RÉSULTAT: {reussis}/{total} modules OK ({reussis/total*100:.1f}%)")
    print("="*70)
    
    return reussis == total


def test_import_main():
    """Test que main.py peut importer tous les nouveaux modules"""
    print("\n" + "="*70)
    print("🧪 TEST - IMPORTATION DANS MAIN.PY")
    print("="*70)
    
    try:
        # Simuler les imports de main.py
        from defis_quotidiens import menu_defis
        from comparaison_domaines import menu_comparaison
        from classement import menu_classement
        from quetes import menu_quetes
        from export_avance import menu_export_avance
        from themes import menu_themes
        from notifications import menu_notifications
        from mode_hors_ligne import menu_mode_hors_ligne
        from analytics import menu_analytics
        from collaboratif import menu_collaboratif
        
        print("✅ Tous les imports de main.py fonctionnent correctement")
        print("✅ Les 10 fonctions menu sont disponibles")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors des imports: {e}")
        return False


def test_fonctionnalites_base():
    """Test rapide de quelques fonctionnalités de base"""
    print("\n" + "="*70)
    print("🧪 TEST - FONCTIONNALITÉS DE BASE")
    print("="*70)
    
    tests_reussis = 0
    tests_total = 0
    
    # Test 1: Défis quotidiens
    try:
        from defis_quotidiens import obtenir_defi_du_jour
        defi = obtenir_defi_du_jour()
        if defi:
            print("✅ Défis quotidiens - obtenir_defi_du_jour() fonctionne")
            tests_reussis += 1
    except Exception as e:
        print(f"❌ Défis quotidiens: {e}")
    tests_total += 1
    
    # Test 2: Comparaison domaines
    try:
        from comparaison_domaines import calculer_score_competence
        from progression import obtenir_progression_domaine
        prog_dom = obtenir_progression_domaine('python')
        score = calculer_score_competence(prog_dom)
        if 0 <= score <= 100:
            print("✅ Comparaison domaines - calculer_score_competence() fonctionne")
            tests_reussis += 1
    except Exception as e:
        print(f"❌ Comparaison domaines: {e}")
    tests_total += 1
    
    # Test 3: Classement
    try:
        from classement import calculer_points_globaux
        points = calculer_points_globaux()
        if points >= 0:
            print("✅ Classement - calculer_points_globaux() fonctionne")
            tests_reussis += 1
    except Exception as e:
        print(f"❌ Classement: {e}")
    tests_total += 1
    
    # Test 4: Quêtes
    try:
        from quetes import charger_quetes
        quetes = charger_quetes()
        if isinstance(quetes, dict):
            print("✅ Quêtes - charger_quetes() fonctionne")
            tests_reussis += 1
    except Exception as e:
        print(f"❌ Quêtes: {e}")
    tests_total += 1
    
    # Test 5: Export avancé
    try:
        from export_avance import lister_exports
        exports = lister_exports()
        print("✅ Export avancé - lister_exports() fonctionne")
        tests_reussis += 1
    except Exception as e:
        print(f"❌ Export avancé: {e}")
    tests_total += 1
    
    # Test 6: Thèmes
    try:
        from themes import obtenir_config_theme, obtenir_themes_disponibles
        config = obtenir_config_theme()
        themes_dispo = obtenir_themes_disponibles()
        if config and len(themes_dispo) >= 5:
            print("✅ Thèmes - fonctions de base fonctionnent")
            tests_reussis += 1
    except Exception as e:
        print(f"❌ Thèmes: {e}")
    tests_total += 1
    
    # Test 7: Notifications
    try:
        from notifications import obtenir_notifications_non_lues
        non_lues = obtenir_notifications_non_lues()
        print("✅ Notifications - obtenir_notifications_non_lues() fonctionne")
        tests_reussis += 1
    except Exception as e:
        print(f"❌ Notifications: {e}")
    tests_total += 1
    
    # Test 8: Mode hors ligne
    try:
        from mode_hors_ligne import charger_cache, charger_config_offline
        cache = charger_cache()
        config = charger_config_offline()
        if isinstance(cache, dict) and isinstance(config, dict):
            print("✅ Mode hors ligne - fonctions de base fonctionnent")
            tests_reussis += 1
    except Exception as e:
        print(f"❌ Mode hors ligne: {e}")
    tests_total += 1
    
    # Test 9: Analytics
    try:
        from analytics import calculer_statistiques_avancees
        stats = calculer_statistiques_avancees()
        if isinstance(stats, dict):
            print("✅ Analytics - calculer_statistiques_avancees() fonctionne")
            tests_reussis += 1
    except Exception as e:
        print(f"❌ Analytics: {e}")
    tests_total += 1
    
    # Test 10: Collaboratif
    try:
        from collaboratif import charger_donnees_communaute
        communaute = charger_donnees_communaute()
        if isinstance(communaute, dict):
            print("✅ Collaboratif - charger_donnees_communaute() fonctionne")
            tests_reussis += 1
    except Exception as e:
        print(f"❌ Collaboratif: {e}")
    tests_total += 1
    
    print(f"\n📊 Fonctionnalités testées: {tests_reussis}/{tests_total} OK")
    return tests_reussis == tests_total


if __name__ == "__main__":
    print("\n" + "="*70)
    print("🚀 TEST D'INTÉGRATION DES 10 MODULES D'AMÉLIORATION")
    print("="*70)
    
    # Test 1: Imports
    test1 = test_import_modules()
    
    # Test 2: Imports dans main
    test2 = test_import_main()
    
    # Test 3: Fonctionnalités de base
    test3 = test_fonctionnalites_base()
    
    # Résumé final
    print("\n" + "="*70)
    print("📊 RÉSUMÉ FINAL")
    print("="*70)
    print(f"Test imports modules:        {'✅ RÉUSSI' if test1 else '❌ ÉCHOUÉ'}")
    print(f"Test imports main.py:        {'✅ RÉUSSI' if test2 else '❌ ÉCHOUÉ'}")
    print(f"Test fonctionnalités base:   {'✅ RÉUSSI' if test3 else '❌ ÉCHOUÉ'}")
    
    succes_global = test1 and test2 and test3
    print("\n" + "="*70)
    if succes_global:
        print("✅ TOUS LES TESTS SONT RÉUSSIS - SYSTÈME PRÊT !")
    else:
        print("⚠️  Certains tests ont échoué - Vérifier les erreurs ci-dessus")
    print("="*70 + "\n")
    
    sys.exit(0 if succes_global else 1)
