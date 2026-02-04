# 🤝 Guide de Contribution

Merci de votre intérêt pour contribuer au Projet Éducation Python !

## 📋 Table des Matières

- [Code de Conduite](#code-de-conduite)
- [Comment Contribuer](#comment-contribuer)
- [Structure du Projet](#structure-du-projet)
- [Standards de Code](#standards-de-code)
- [Process de Pull Request](#process-de-pull-request)
- [Reporting Bugs](#reporting-bugs)
- [Proposer des Fonctionnalités](#proposer-des-fonctionnalités)

---

## 📜 Code de Conduite

Soyez respectueux, professionnel et bienveillant envers tous les contributeurs.

---

## 🚀 Comment Contribuer

### 1. Fork le Projet

```bash
git clone https://github.com/votre-username/ProjetEducationPython.git
cd ProjetEducationPython
```

### 2. Créer une Branche

```bash
git checkout -b feature/ma-nouvelle-fonctionnalite
```

Conventions de noms de branches :
- `feature/` - Nouvelle fonctionnalité
- `fix/` - Correction de bug
- `docs/` - Documentation
- `refactor/` - Refactoring
- `test/` - Ajout de tests

### 3. Faire vos Modifications

Respectez la structure du projet :

```
backend/
  modules/
    core/       ← Fonctionnalités de base
    features/   ← Nouvelles fonctionnalités
  data/         ← Données
  api/          ← Routes API

frontend/
  src/
    components/ ← Composants React
    pages/      ← Pages
    services/   ← Appels API
```

### 4. Tester

```bash
# Backend
cd backend
python -m pytest

# Frontend (quand disponible)
cd frontend
npm test
```

### 5. Commit

Utilisez des messages de commit clairs :

```bash
git commit -m "feat: Ajout du système de badges premium"
git commit -m "fix: Correction du calcul d'XP"
git commit -m "docs: Mise à jour du README"
```

Convention :
- `feat:` - Nouvelle fonctionnalité
- `fix:` - Correction de bug
- `docs:` - Documentation
- `style:` - Formatage
- `refactor:` - Refactoring
- `test:` - Tests
- `chore:` - Maintenance

### 6. Push et Pull Request

```bash
git push origin feature/ma-nouvelle-fonctionnalite
```

Puis créez une Pull Request sur GitHub.

---

## 🏗️ Structure du Projet

### Backend (Python)

```python
# modules/core/ - Modules de base
# Ne modifiez que si nécessaire, testez intensivement

# modules/features/ - Nouvelles fonctionnalités
# Ajoutez vos nouvelles fonctionnalités ici

# Exemple de nouveau module :
# backend/modules/features/ma_feature.py

def menu_ma_feature():
    """Menu principal de ma fonctionnalité"""
    print("Ma nouvelle fonctionnalité !")
    # Implémentation...
```

### Frontend (React)

```jsx
// src/components/ - Composants réutilisables
// Créez des composants petits et réutilisables

// Exemple :
// src/components/MaFeature/MaFeature.jsx

import React from 'react';

export default function MaFeature() {
  return (
    <div className="ma-feature">
      {/* Votre composant */}
    </div>
  );
}
```

---

## 📏 Standards de Code

### Python (Backend)

```python
# Suivez PEP 8
# Utilisez des docstrings

def ma_fonction(param1, param2):
    """
    Description courte de la fonction
    
    Args:
        param1: Description du paramètre 1
        param2: Description du paramètre 2
    
    Returns:
        Description du retour
    """
    # Implémentation
    return resultat

# Nommage :
# - snake_case pour variables et fonctions
# - PascalCase pour classes
# - UPPER_CASE pour constantes

# Imports organisés :
# 1. Bibliothèques standard
# 2. Bibliothèques tierces
# 3. Modules locaux
```

### JavaScript/React (Frontend)

```jsx
// Suivez Airbnb Style Guide
// Utilisez JSDoc

/**
 * Description du composant
 * @param {Object} props - Props du composant
 * @returns {JSX.Element}
 */
export default function MonComposant({ prop1, prop2 }) {
  // Hooks en premier
  const [state, setState] = useState(null);
  
  // Handlers
  const handleClick = () => {
    // ...
  };
  
  // Render
  return (
    <div className="mon-composant">
      {/* JSX */}
    </div>
  );
}

// Nommage :
// - camelCase pour variables et fonctions
// - PascalCase pour composants
// - UPPER_CASE pour constantes
```

---

## 🔍 Process de Pull Request

1. **Décrivez vos changements**
   - Titre clair et descriptif
   - Description détaillée
   - Screenshots si applicable

2. **Vérifiez**
   - [ ] Le code compile/run sans erreur
   - [ ] Les tests passent
   - [ ] La documentation est à jour
   - [ ] Le code est formaté correctement

3. **Référencez les Issues**
   ```
   Fixes #123
   Closes #456
   ```

4. **Attendez la Review**
   - Soyez patient
   - Répondez aux commentaires
   - Faites les modifications demandées

---

## 🐛 Reporting Bugs

Utilisez le template d'Issue :

```markdown
**Description du Bug**
Description claire et concise

**Pour Reproduire**
1. Allez à '...'
2. Cliquez sur '...'
3. Scrollez jusqu'à '...'
4. Voir l'erreur

**Comportement Attendu**
Ce qui devrait se passer

**Screenshots**
Si applicable

**Environnement**
- OS: [e.g. Windows 11]
- Python: [e.g. 3.10]
- Node: [e.g. 18.0]

**Logs**
```
Collez les logs ici
```
```

---

## 💡 Proposer des Fonctionnalités

1. **Vérifiez** si la fonctionnalité n'existe pas déjà
2. **Ouvrez une Issue** avec le label `enhancement`
3. **Décrivez** :
   - Le problème que ça résout
   - La solution proposée
   - Des alternatives considérées
   - Des mockups/wireframes si applicable

---

## ✅ Checklist du Contributeur

Avant de soumettre votre PR :

### Code
- [ ] Le code suit les standards du projet
- [ ] Les fonctions ont des docstrings
- [ ] Le code est commenté si nécessaire
- [ ] Pas de code mort/commenté

### Tests
- [ ] Les tests existants passent
- [ ] De nouveaux tests sont ajoutés si nécessaire
- [ ] La couverture de code est maintenue

### Documentation
- [ ] README mis à jour si nécessaire
- [ ] Docstrings ajoutées/mises à jour
- [ ] CHANGELOG.md mis à jour

### Git
- [ ] Commits atomic et bien nommés
- [ ] Branche à jour avec main
- [ ] Pas de fichiers inutiles (logs, cache, etc.)

---

## 📞 Questions ?

- Ouvrez une [Discussion](https://github.com/votre-username/ProjetEducationPython/discussions)
- Rejoignez notre [Discord](lien-discord) (si applicable)
- Envoyez un email à contact@example.com

---

## 🙏 Merci !

Votre contribution rend ce projet meilleur pour tout le monde.

**Happy Coding! 🚀**
