# Utiliser l'image de base Python 3.11 slim 
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt en premier
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier les fichiers nécessaires
COPY train_model.py .
COPY app.py .
COPY models/ models/
COPY data/ data/

# Créer le dossier plots pour les visualisations
RUN mkdir -p plots

# Exposer le port 7860 pour Gradio
EXPOSE 7860

# Configurer les variables d'environnement Gradio
ENV GRADIO_SERVER_NAME=0.0.0.0
ENV GRADIO_SERVER_PORT=7860

# Commande de démarrage de l'application
CMD ["python", "app.py"]
