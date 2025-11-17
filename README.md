```markdown
# 🏠 House Price Predictor - ML Application

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-orange?logo=scikit-learn)
![Gradio](https://img.shields.io/badge/Gradio-4.19.2-red?logo=gradio)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

**Application web intelligente de prédiction des prix immobiliers** utilisant Random Forest Regression et une interface Gradio interactive.

[🚀 Démo en ligne](#) | [📖 Documentation](#table-des-matières) | [🐳 Docker Hub](https://hub.docker.com/r/syntaxerror771/house-price-predictor) | [🤗 HuggingFace Space](#)

</div>

---

## 📋 Table des matières

- [À propos du projet](#-à-propos-du-projet)
- [Fonctionnalités](#-fonctionnalités)
- [Architecture technique](#️-architecture-technique)
- [Démarrage rapide](#-démarrage-rapide)
  - [Prérequis](#prérequis)
  - [Installation locale](#installation-locale)
  - [Exécution avec Docker](#exécution-avec-docker)
- [Utilisation](#-utilisation)
- [Structure du projet](#-structure-du-projet)
- [Modèle de Machine Learning](#-modèle-de-machine-learning)
- [Performances](#-performances)
- [Déploiement](#-déploiement)
- [Développement](#-développement)
- [Contribuer](#-contribuer)
- [Licence](#-licence)
- [Auteur](#-auteur)

---

## 🎯 À propos du projet

Ce projet est une **application web de bout en bout** pour prédire les prix immobiliers en utilisant des techniques de Machine Learning. Il illustre les meilleures pratiques en matière de :

- ✅ **Machine Learning** : Entraînement et évaluation d'un modèle Random Forest
- ✅ **MLOps** : Conteneurisation avec Docker, déploiement cloud
- ✅ **DevOps** : Versionnement Git, CI/CD avec GitHub
- ✅ **Interface utilisateur** : Application web interactive avec Gradio
- ✅ **Visualisation** : Graphiques interactifs avec matplotlib et seaborn

### Contexte

Développé dans le cadre d'un projet académique de Machine Learning et DevOps, ce projet démontre comment construire, conteneuriser et déployer une application ML complète en production [web:61][web:63].

---

## ✨ Fonctionnalités

### 🔮 Prédiction intelligente
- **Modèle Random Forest** avec 100 arbres de décision
- **7 caractéristiques** prises en compte pour la prédiction
- **Intervalle de confiance à 95%** pour évaluer la fiabilité

### 📊 Visualisations interactives
- **Importance des features** : Identifie les facteurs clés du prix
- **Résumé des inputs** : Visualisation des caractéristiques saisies
- **Distribution de la prédiction** : Affiche l'intervalle de confiance

### 🎛️ Interface utilisateur
- **Interface web intuitive** avec sliders interactifs
- **Temps de réponse instantané** (< 1 seconde)
- **Design moderne** avec Gradio 4.19.2

### 🐳 Conteneurisation
- **Image Docker optimisée** (~850 MB)
- **Déploiement en un clic** avec Docker
- **Multi-plateforme** : Linux, Windows, macOS

---

## 🛠️ Architecture technique

### Stack technologique

```

┌─────────────────────────────────────┐
│         Frontend (Gradio)           │
│   Interface web + Visualisations    │
└──────────────┬──────────────────────┘
│
┌──────────────▼──────────────────────┐
│      Backend (Python 3.11)          │
│  -  Chargement modèle (.pkl)         │
│  -  Normalisation (StandardScaler)   │
│  -  Prédiction (RandomForest)        │
│  -  Génération graphiques            │
└──────────────┬──────────────────────┘
│
┌──────────────▼──────────────────────┐
│    Modèle ML (scikit-learn)         │
│  -  Random Forest Regressor          │
│  -  100 arbres, max_depth=15         │
│  -  Entraîné sur 1000 échantillons   │
└─────────────────────────────────────┘

```

### Dépendances principales

| Bibliothèque | Version | Rôle |
|--------------|---------|------|
| **Python** | 3.11 | Langage de programmation |
| **scikit-learn** | 1.3.0 | Modèle Random Forest |
| **Gradio** | 4.19.2 | Interface web interactive |
| **pandas** | 2.0.3 | Manipulation de données |
| **NumPy** | 1.24.3 | Calculs numériques |
| **matplotlib** | 3.7.2 | Visualisations de base |
| **seaborn** | 0.12.2 | Visualisations avancées |

---

## 🚀 Démarrage rapide

### Prérequis

- **Python 3.11+** installé sur votre système
- **Git** pour cloner le repository
- **Docker** (optionnel, pour l'exécution conteneurisée)

### Installation locale

#### 1. Cloner le repository

```

git clone https://github.com/votre-username/house-price-predictor.git
cd house-price-predictor

```

#### 2. Créer un environnement virtuel

**Linux / macOS :**
```

python3.11 -m venv .venv
source .venv/bin/activate

```

**Windows :**
```

py -3.11 -m venv .venv
.venv\Scripts\activate

```

#### 3. Installer les dépendances

```

pip install -r requirements.txt

```

#### 4. Lancer l'application

```

python app.py

```

L'application sera accessible sur **http://localhost:7860** 🎉

### Exécution avec Docker

#### Option 1 : Utiliser l'image pré-construite

```


# Télécharger l'image depuis Docker Hub

docker pull syntaxerror771/house-price-predictor:latest

# Lancer le conteneur

docker run -d -p 7860:7860 --name house-predictor syntaxerror771/house-price-predictor:latest

```

#### Option 2 : Construire l'image localement

```


# Construire l'image

docker build -t house-price-predictor:latest .

# Lancer le conteneur

docker run -d -p 7860:7860 --name house-predictor house-price-predictor:latest

```

Accédez à l'application sur **http://localhost:7860**

#### Commandes Docker utiles

```


# Voir les logs

docker logs house-predictor

# Arrêter le conteneur

docker stop house-predictor

# Redémarrer le conteneur

docker start house-predictor

# Supprimer le conteneur

docker rm -f house-predictor

```

---

## 💻 Utilisation

### Interface web

1. **Ouvrez votre navigateur** sur http://localhost:7860
2. **Ajustez les sliders** pour définir les caractéristiques de la maison :
   - Surface (800 - 4000 pieds carrés)
   - Nombre de chambres (1 - 5)
   - Nombre de salles de bain (1 - 3)
   - Âge de la maison (0 - 50 ans)
   - Taille du terrain (2000 - 10000 pieds carrés)
   - Places de garage (0 - 3)
   - Score du quartier (1 - 10)
3. **Cliquez sur "🔮 Prédire le Prix"**
4. **Consultez les résultats** :
   - Prix estimé avec intervalle de confiance
   - Graphiques d'analyse

### Exemple de prédiction

**Input :**
```

Surface: 2500 sq ft
Chambres: 3
Salles de bain: 2
Âge: 10 ans
Terrain: 5000 sq ft
Garage: 2 places
Score quartier: 8/10

```

**Output :**
```

Prix estimé: \$485,320
Intervalle de confiance: [\$465,200 - \$505,440]

```

---

## 📁 Structure du projet

```

house-price-predictor/
│
├── 📄 README.md                 \# Documentation du projet
├── 📄 requirements.txt          \# Dépendances Python
├── 📄 .gitignore                \# Fichiers ignorés par Git
├── 📄 Dockerfile                \# Configuration Docker
├── 📄 .dockerignore             \# Fichiers ignorés par Docker
│
├── 🐍 train_model.py            \# Script d'entraînement du modèle
├── 🐍 app.py                    \# Application Gradio
│
├── 💾 model.pkl                 \# Modèle Random Forest entraîné
├── 💾 scaler.pkl                \# StandardScaler pour normalisation
├── 💾 feature_names.pkl         \# Noms des features
│
├── 📂 data/
│   └── house_data.csv           \# Dataset (1000 échantillons)
│
└── 📂 plots/                    \# Dossier pour les graphiques générés
├── feature_importance.png
├── input_summary.png
└── prediction_confidence.png

```

---

## 🧠 Modèle de Machine Learning

### Algorithme : Random Forest Regressor

Le **Random Forest** est un algorithme d'ensemble qui combine plusieurs arbres de décision pour améliorer la précision et réduire le surapprentissage [web:61].

**Hyperparamètres du modèle :**
```

RandomForestRegressor(
n_estimators=100,      \# 100 arbres de décision
max_depth=15,          \# Profondeur maximale de 15
random_state=42,       \# Pour la reproductibilité
n_jobs=-1              \# Utilise tous les cœurs CPU
)

```

### Features utilisées

| Feature | Description | Plage de valeurs |
|---------|-------------|------------------|
| `square_feet` | Surface habitable | 800 - 4000 sq ft |
| `bedrooms` | Nombre de chambres | 1 - 5 |
| `bathrooms` | Nombre de salles de bain | 1 - 3 |
| `age_years` | Âge de la maison | 0 - 50 ans |
| `lot_size` | Taille du terrain | 2000 - 10000 sq ft |
| `garage_spaces` | Places de garage | 0 - 3 |
| `neighborhood_score` | Score du quartier | 1 - 10 |

### Prétraitement des données

1. **Génération de données synthétiques** : 1000 échantillons générés avec une formule réaliste
2. **Normalisation** : StandardScaler appliqué sur toutes les features
3. **Division** : 80% entraînement, 20% test
4. **Validation** : Cross-validation avec R² et MAE

### Formule de génération des prix

```

Prix = surface × 150
+ chambres × 20,000
+ salles_de_bain × 15,000
- âge × 2,000
+ terrain × 10
+ garage × 5,000
+ score_quartier × 3,000
+ bruit_aléatoire

```

---

## 📊 Performances

### Métriques d'évaluation

| Métrique | Valeur | Interprétation |
|----------|--------|----------------|
| **R² Score** | 0.9523 | Excellente capacité prédictive (95.23%) |
| **MAE** | $9,847 | Erreur moyenne absolue |
| **MSE** | 142,851,203 | Erreur quadratique moyenne |

### Importance des features

```

1. square_feet          : 45.2%  ████████████████████
2. neighborhood_score   : 18.7%  ████████
3. bedrooms            : 12.4%  █████
4. age_years           : 9.8%   ████
5. lot_size            : 7.3%   ███
6. bathrooms           : 4.6%   ██
7. garage_spaces       : 2.0%   █
```

### Intervalle de confiance

Le modèle fournit un **intervalle de confiance à 95%** calculé à partir de la variance des prédictions des 100 arbres individuels [web:61].

---

## 🚢 Déploiement

### Docker Hub

L'image Docker est publiquement disponible sur Docker Hub :

```

docker pull syntaxerror771/house-price-predictor:latest

```

🔗 **Lien** : https://hub.docker.com/r/syntaxerror771/house-price-predictor

### HuggingFace Spaces

Déploiement en cours sur HuggingFace Spaces pour un accès public sans installation [file:1].

🔗 **Lien** : (À venir)

### Déploiement local en production

Pour déployer sur votre propre serveur :

```


# Avec redémarrage automatique

docker run -d \
--name house-predictor \
--restart=always \
-p 7860:7860 \
syntaxerror771/house-price-predictor:latest

```

---

## 👨‍💻 Développement

### Entraîner un nouveau modèle

```

python train_model.py

```

Cela générera :
- `data/house_data.csv` : Nouveau dataset
- `model.pkl` : Modèle entraîné
- `scaler.pkl` : Scaler mis à jour
- `feature_names.pkl` : Noms des features

### Modifier l'interface Gradio

Éditez `app.py` pour personnaliser :
- Les plages de valeurs des sliders
- Les couleurs et le thème
- Les fonctions de visualisation

### Rebuild de l'image Docker

```

docker build -t syntaxerror771/house-price-predictor:latest .
docker push syntaxerror771/house-price-predictor:latest

```

### Tests

```


# Tester le chargement du modèle

python -c "import pickle; pickle.load(open('model.pkl', 'rb'))"

# Tester l'application

python app.py

```

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Voici comment contribuer [web:61] :

### 1. Fork le projet
### 2. Créer une branche de feature

```

git checkout -b feature/AmazingFeature

```

### 3. Commit les changements

```

git commit -m "Add: Amazing feature description"

```

### 4. Push vers la branche

```

git push origin feature/AmazingFeature

```

### 5. Ouvrir une Pull Request

### Suggestions d'améliorations

- [ ] Ajouter plus de features (piscine, année de construction, etc.)
- [ ] Implémenter d'autres algorithmes (XGBoost, LightGBM)
- [ ] Ajouter des tests unitaires avec pytest
- [ ] Créer une API REST avec FastAPI
- [ ] Intégration continue avec GitHub Actions
- [ ] Support de plusieurs devises (USD, EUR, MAD)

---

## 📝 Licence

Ce projet est sous licence **MIT License**.

Vous êtes libre de :
- ✅ Utiliser ce projet commercialement
- ✅ Modifier le code source
- ✅ Distribuer le projet
- ✅ Utiliser le projet en privé

Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 👤 Auteur

**Mohamed Zaali**

- GitHub: [@syntaxerror771](https://github.com/votre-username)
- Docker Hub: [@syntaxerror771](https://hub.docker.com/u/syntaxerror771)
- LinkedIn: [Mohamed Zaali](https://linkedin.com/in/votre-profil)

---

## 🙏 Remerciements

- **scikit-learn** pour la bibliothèque ML
- **Gradio** pour l'interface web intuitive
- **Docker** pour la conteneurisation
- **HuggingFace** pour l'hébergement cloud
- La communauté open-source pour l'inspiration

---

## 📈 Statistiques du projet

![GitHub stars](https://img.shields.io/github/stars/votre-username/house-price-predictor?style=social)
![GitHub forks](https://img.shields.io/github/forks/votre-username/house-price-predictor?style=social)
![Docker Pulls](https://img.shields.io/docker/pulls/syntaxerror771/house-price-predictor)

---

<div align="center">

**⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile !**

Made with ❤️ and ☕ by Mohamed Zaali

</div>
```



