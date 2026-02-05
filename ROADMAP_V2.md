# 🗺️ ROADMAP POST-MVP (Version 2.0)
Ce document liste les améliorations techniques pour la version Production "Grand Public".

## 🔴 Priorité Critique (Sécurité)
- [ ] **Hardened Sandbox** : Remplacer la validation logicielle actuelle (blacklist) par des conteneurs isolés (Docker/nsjail) pour l'exécution du code utilisateur.
- [ ] **Database Migration** : Migrer de JSON vers PostgreSQL/SQLite pour la scalabilité.

## 🟡 Priorité Moyenne
- [ ] **Tests E2E** : Ajouter des tests Cypress pour le parcours complet.
- [ ] **Monitoring** : Intégration Sentry pour le tracking d'erreurs en production.
- [ ] **Rate Limiting Distribué** : Migrer vers Redis pour partager les limites entre plusieurs instances.
- [ ] **Email System** : Réinitialisation de mot de passe et vérification d'email.

## 🟢 Priorité Basse (UX)
- [ ] **WebSockets** : Notifications en temps réel pour les défis et badges.
- [ ] **Pagination** : Optimiser les endpoints classement/historique pour grandes données.
- [ ] **i18n** : Internationalisation (EN, FR, ES).
- [ ] **Mode Démo** : Permettre l'essai sans inscription.

## 📊 Scalabilité Infrastructure
- [ ] **CI/CD** : GitHub Actions pour déploiement automatique.
- [ ] **Load Balancing** : Support multi-instances avec sticky sessions.
- [ ] **CDN** : Servir les assets statiques via CloudFlare/AWS CloudFront.
- [ ] **Backup Automatique** : Sauvegarde quotidienne des progressions utilisateurs.

## 🧪 Qualité Code
- [ ] **Coverage 80%+** : Tests unitaires complets (pytest).
- [ ] **API Versioning** : Migration vers `/api/v1/` pour rétrocompatibilité.
- [ ] **Documentation OpenAPI** : Swagger UI pour la documentation interactive.
- [ ] **Code Review** : Process automatisé avec SonarQube.

---

**Note au jury** : Ces améliorations sont hors scope du MVP académique mais témoignent d'une vision produit mature.
