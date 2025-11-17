import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score
import pickle
import os

# Création du dossier models s'il n'existe pas
os.makedirs('models', exist_ok=True)

# Seed pour la reproductibilité
np.random.seed(42)

# Génération de 1000 maisons avec 7 caractéristiques
n_samples = 1000

data = {
    'square_feet': np.random.randint(800, 4000, n_samples),
    'bedrooms': np.random.randint(1, 6, n_samples),
    'bathrooms': np.random.randint(1, 4, n_samples),
    'age_years': np.random.randint(0, 50, n_samples),
    'lot_size': np.random.randint(2000, 10000, n_samples),
    'garage_spaces': np.random.randint(0, 4, n_samples),
    'neighborhood_score': np.random.randint(1, 11, n_samples)
}

# Création du DataFrame
df = pd.DataFrame(data)

# Génération des prix selon la formule du TP
# Prix = surface * 150 + chambres * 20000 + salles_de_bain * 15000 - âge * 2000 + autres facteurs + bruit
df['price'] = (
    df['square_feet'] * 150 +
    df['bedrooms'] * 20000 +
    df['bathrooms'] * 15000 -
    df['age_years'] * 2000 +
    df['lot_size'] * 10 +
    df['garage_spaces'] * 5000 +
    df['neighborhood_score'] * 3000 +
    np.random.normal(0, 10000, n_samples)  
)

# Sauvegarde des données dans le dossier data
os.makedirs('data', exist_ok=True)
df.to_csv('data/house_data.csv', index=False)

# Séparation des features (X) et de la cible (y)
X = df.drop('price', axis=1)
y = df['price']

# Sauvegarde des noms des features
feature_names = list(X.columns)

# Division en ensembles d'entraînement (80%) et de test (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Normalisation des features avec StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Création et entraînement du modèle Random Forest Regressor
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train_scaled, y_train)

# Prédictions sur l'ensemble de test
y_pred = model.predict(X_test_scaled)

# Évaluation des performances
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE (Mean Absolute Error) : ${mae:,.2f}")
print(f"R2 Score : {r2:.4f}")

# Sauvegarde du modèle, du scaler et des noms des features
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('models/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

with open('models/feature_names.pkl', 'wb') as f:
    pickle.dump(feature_names, f)


