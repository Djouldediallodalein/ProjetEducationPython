# 🎓 Projet Éducation Python - Plateforme d'Apprentissage Interactive

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production_Ready-success.svg)]()

> Plateforme complète d'apprentissage interactif avec IA pour maîtriser la programmation

---

## 📋 Vue d'Ensemble

Une application d'apprentissage gamifiée avec intelligence artificielle (Ollama) pour générer des exercices personnalisés et suivre votre progression à travers différents domaines de programmation.

### ✨ Fonctionnalités Principales

- 🤖 **Génération d'exercices avec IA** (Ollama)
- 🌍 **8 domaines de programmation** (Python, Java, JavaScript, HTML/CSS, C, BDD, Algo, Git)
- 📊 **Système de progression** avec XP et niveaux
- 🏆 **Gamification** complète (badges, quêtes, défis, titres)
- 📈 **Analytics avancées** avec visualisations
- 👥 **Multi-utilisateurs** avec profils séparés
- 🔄 **Répétition espacée** (SRS) scientifique
- 🎨 **5 thèmes visuels** personnalisables

---

## 🏗️ Structure du Projet

```
ProjetEducationPython/
├── backend/                    # Backend Python
│   ├── modules/
│   │   ├── core/              # 9 modules de base
│   │   └── features/          # 10 modules d'amélioration
│   ├── data/                  # Données et configurations
│   ├── api/                   # API Flask (à venir)
│   ├── main.py               # Point d'entrée
│   └── requirements.txt      # Dépendances Python
├── frontend/                  # Frontend React (à développer)
│   └── (structure React avec Vite)
├── docs/                      # Documentation
│   ├── BACKEND_COMPLET.md
│   ├── GUIDE_FRONTEND.md
│   └── RESUME_PROJET.md
├── .venv/                     # Environnement virtuel Python
├── .gitignore
├── LICENSE
└── README.md                  # Ce fichier
```

---

## 🚀 Installation Rapide

### Prérequis

- Python 3.8 ou supérieur
- Ollama installé et configuré
- Node.js 18+ (pour le frontend)

### Backend

```bash
# Cloner le projet
git clone https://github.com/votre-username/ProjetEducationPython.git
cd ProjetEducationPython

# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement (Windows)
.venv\Scripts\activate

# Installer les dépendances
cd backend
pip install -r requirements.txt

# Lancer Ollama avec le modèle
ollama pull qwen2.5-coder:14b

# Lancer l'application
python main.py
```

### Frontend (à venir)

```bash
cd frontend
npm install
npm run dev
```

---

## 📚 Documentation

- **[Backend Complet](docs/BACKEND_COMPLET.md)** - Documentation technique complète du backend
- **[Guide Frontend](docs/GUIDE_FRONTEND.md)** - Guide d'apprentissage pour développer le frontend
- **[Résumé Projet](docs/RESUME_PROJET.md)** - Vue d'ensemble et accomplissements

---

## 🎯 Fonctionnalités Détaillées

### Modules Core (9)

1. **fonctions.py** - Génération et vérification d'exercices
2. **progression.py** - Suivi de progression multi-domaines
3. **domaines.py** - Gestion des domaines d'apprentissage
4. **xp_systeme.py** - Système d'expérience et niveaux
5. **avancees.py** - Système de badges
6. **repetition_espacee.py** - Algorithme SRS
7. **utilisateurs.py** - Gestion multi-utilisateurs
8. **export_import.py** - Sauvegarde et restauration
9. **gestion_erreurs.py** - Logging et gestion d'erreurs

### Modules Features (10)

1. **🎯 defis_quotidiens.py** - Défis quotidiens avec bonus XP
2. **📊 comparaison_domaines.py** - Comparaison et scoring
3. **🏆 classement.py** - Système de titres et prestige
4. **🗺️ quetes.py** - 12 quêtes avec récompenses
5. **📦 export_avance.py** - Export multi-formats
6. **🎨 themes.py** - 5 thèmes visuels
7. **🔔 notifications.py** - Système de notifications
8. **✈️ mode_hors_ligne.py** - Cache d'exercices
9. **📈 analytics.py** - Statistiques avancées
10. **🌍 collaboratif.py** - Mode communautaire

---

## 🎮 Utilisation

### Démarrage

```bash
cd backend
python main.py
```

### Menu Principal (25 options)

```
0-13   : Fonctionnalités de base
14-23  : Nouvelles fonctionnalités
24     : Quitter
```

---

## 🛠️ Technologies Utilisées

### Backend
- **Python 3.8+**
- **Ollama** (qwen2.5-coder:14b)
- **JSON** (persistance)

### Frontend (prévu)
- **React.js** avec Vite
- **Tailwind CSS**
- **Recharts** (graphiques)
- **Axios** (API)
- **React Router**

---

## 📊 Statistiques du Projet

- **19 modules Python** (~6300 lignes)
- **8 domaines** avec 48+ thèmes
- **25 fonctionnalités** dans le menu
- **100% tests réussis**

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add AmazingFeature'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Guidelines

- Respectez la structure des dossiers
- Documentez votre code
- Ajoutez des tests si possible
- Suivez les conventions Python (PEP 8)

---

## 🗺️ Roadmap

### Phase 1 - Backend ✅ (Terminée)
- [x] Tous les modules core
- [x] Tous les modules features
- [x] Tests et validation
- [x] Documentation complète

### Phase 2 - Frontend 🚧 (En cours)
- [ ] Setup React + Vite
- [ ] Composants de base
- [ ] Pages principales
- [ ] API Flask
- [ ] Intégration backend/frontend

### Phase 3 - Améliorations 📋 (Planifiée)
- [ ] Mode collaboratif réel (avec serveur)
- [ ] Application mobile (React Native)
- [ ] Support multilingue
- [ ] IA plus avancée
- [ ] Marketplace d'exercices

---

## 📝 License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 👨‍💻 Auteur

**Votre Nom**

- GitHub: [@votre-username](https://github.com/votre-username)
- Email: votre.email@example.com

---

## 🙏 Remerciements

- **Ollama** pour l'IA générative
- La communauté **Python**
- Tous les contributeurs

---

## 📞 Support

Pour toute question ou problème :

1. Consultez la [documentation](docs/)
2. Ouvrez une [Issue](https://github.com/votre-username/ProjetEducationPython/issues)
3. Contactez-nous par email

---

<div align="center">

**⭐ N'oubliez pas de mettre une étoile si vous aimez ce projet ! ⭐**

Made with ❤️ and ☕

</div>
