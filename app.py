import gradio as gr
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('plots', exist_ok=True)

# Chargement du modèle, scaler et noms des features
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('feature_names.pkl', 'rb') as f:
    feature_names = pickle.load(f)


# Fonction 1 : Graphique d'importance des features
def plot_feature_importance():
    """Crée un graphique d'importance des features"""
    importance = model.feature_importances_
    indices = np.argsort(importance)[::-1]
    
    plt.figure(figsize=(10, 6))
    plt.title("Importance des Features", fontsize=16, fontweight='bold')
    plt.bar(range(len(importance)), importance[indices], color='steelblue', alpha=0.8)
    plt.xticks(range(len(importance)), [feature_names[i] for i in indices], rotation=45, ha='right')
    plt.ylabel("Importance", fontsize=12)
    plt.xlabel("Features", fontsize=12)
    plt.tight_layout()
    
    filepath = 'plots/feature_importance.png'
    plt.savefig(filepath, dpi=100, bbox_inches='tight')
    plt.close()
    
    return filepath

# Fonction 2 : Résumé des inputs
def plot_input_summary(square_feet, bedrooms, bathrooms, age_years, lot_size, garage_spaces, neighborhood_score):
    """Crée un graphique récapitulatif des inputs"""
    features = ['Surface (sq ft)', 'Chambres', 'Salles de bain', 'Âge (ans)', 
                'Terrain (sq ft)', 'Garage', 'Score quartier']
    values = [square_feet, bedrooms, bathrooms, age_years, lot_size, garage_spaces, neighborhood_score]
    
    plt.figure(figsize=(10, 6))
    plt.title("Résumé des Caractéristiques de la Maison", fontsize=16, fontweight='bold')
    colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(features)))
    bars = plt.barh(features, values, color=colors, alpha=0.8)
    plt.xlabel("Valeur", fontsize=12)
    plt.tight_layout()
    
    filepath = 'plots/input_summary.png'
    plt.savefig(filepath, dpi=100, bbox_inches='tight')
    plt.close()
    
    return filepath

# Fonction 3 : Prédiction avec intervalle de confiance
def plot_prediction_confidence(predicted_price, confidence_interval):
    """Crée un graphique de prédiction avec intervalle de confiance"""
    lower_bound, upper_bound = confidence_interval
    
    plt.figure(figsize=(10, 6))
    plt.title("Prédiction du Prix avec Intervalle de Confiance (95%)", fontsize=16, fontweight='bold')
    
    # Barre principale
    plt.barh(['Prix estimé'], [predicted_price], color='green', alpha=0.7, height=0.4)
    
    # Intervalle de confiance
    plt.barh(['Prix estimé'], [upper_bound - lower_bound], left=lower_bound, 
             color='lightgreen', alpha=0.3, height=0.4, label='Intervalle de confiance 95%')
    
    # Ligne de prédiction
    plt.axvline(predicted_price, color='darkgreen', linestyle='--', linewidth=2, label='Prédiction')
    
    plt.xlabel("Prix ($)", fontsize=12)
    plt.xlim(lower_bound - 50000, upper_bound + 50000)
    plt.legend()
    plt.tight_layout()
    
    filepath = 'plots/prediction_confidence.png'
    plt.savefig(filepath, dpi=100, bbox_inches='tight')
    plt.close()
    
    return filepath

# Fonction principale de prédiction
def predict_price(square_feet, bedrooms, bathrooms, age_years, lot_size, garage_spaces, neighborhood_score):
    """Prédit le prix d'une maison et génère les visualisations"""
    
    # Préparer les données d'entrée
    input_data = pd.DataFrame([[square_feet, bedrooms, bathrooms, age_years, 
                                lot_size, garage_spaces, neighborhood_score]], 
                              columns=feature_names)
    
    # Normaliser les données
    input_scaled = scaler.transform(input_data)
    
    # Prédiction
    predicted_price = model.predict(input_scaled)[0]
    
    # Calcul de l'intervalle de confiance (95%)
    # Utiliser les prédictions de tous les arbres
    tree_predictions = np.array([tree.predict(input_scaled)[0] for tree in model.estimators_])
    std_dev = np.std(tree_predictions)
    confidence_interval = (predicted_price - 1.96 * std_dev, predicted_price + 1.96 * std_dev)
    
    # Générer les graphiques
    plot1 = plot_feature_importance()
    plot2 = plot_input_summary(square_feet, bedrooms, bathrooms, age_years, 
                               lot_size, garage_spaces, neighborhood_score)
    plot3 = plot_prediction_confidence(predicted_price, confidence_interval)
    
    # Résultat formaté
    result = f"""
    Prix estimé : ${predicted_price:,.2f}
    
    Intervalle de confiance (95%) :
    - Minimum : ${confidence_interval[0]:,.2f}
    - Maximum : ${confidence_interval[1]:,.2f}
    
    """
    
    return result, plot1, plot2, plot3

# Interface Gradio
with gr.Blocks(title="Prédiction des Prix Immobiliers", theme=gr.themes.Soft()) as demo:
    
    gr.Markdown("# Prédiction des Prix Immobiliers")
    gr.Markdown("### Entrez les caractéristiques de la maison pour obtenir une estimation du prix")
    
    with gr.Row():
        with gr.Column():
            square_feet = gr.Slider(800, 4000, value=2000, step=50, label="Surface (pieds carrés)")
            bedrooms = gr.Slider(1, 5, value=3, step=1, label="Nombre de chambres")
            bathrooms = gr.Slider(1, 3, value=2, step=1, label="Nombre de salles de bain")
            age_years = gr.Slider(0, 50, value=10, step=1, label="Âge de la maison (années)")
        
        with gr.Column():
            lot_size = gr.Slider(2000, 10000, value=5000, step=100, label="Taille du terrain (pieds carrés)")
            garage_spaces = gr.Slider(0, 3, value=2, step=1, label="Places de garage")
            neighborhood_score = gr.Slider(1, 10, value=7, step=1, label="Score du quartier (1-10)")
    
    predict_btn = gr.Button("Prédire le Prix", variant="primary", size="lg")
    
    gr.Markdown("---")
    
    # Outputs
    result_text = gr.Markdown(label="Résultat")
    
    with gr.Row():
        plot1_output = gr.Image(label="Importance des Features", type="filepath")
        plot2_output = gr.Image(label="Résumé des Caractéristiques", type="filepath")
    
    plot3_output = gr.Image(label="Prédiction avec Intervalle de Confiance", type="filepath")
    
    # Lier le bouton à la fonction
    predict_btn.click(
        fn=predict_price,
        inputs=[square_feet, bedrooms, bathrooms, age_years, lot_size, garage_spaces, neighborhood_score],
        outputs=[result_text, plot1_output, plot2_output, plot3_output]
    )

# Lancer l'application
if __name__ == "__main__":
    demo.launch()
