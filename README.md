# StreamlitMeteo-Grp5

Ce projet de 48h, réalisé par le Groupe 5 (Florian, Ayse, Fatima, Ahmed Amine) a pour but de pouvoir
prédire une température à une localisation (poste de mesure) pour une date précise.

Pour cela, nous avons entraîné un modèle en LSTM à partir des données de data.gouv sur le sujet.
Lien des sources : https://meteo.data.gouv.fr/datasets/6569b51ae64326786e4e8e1a

Le notebook concernant le nettoyage des données, l'entraînement du modèle, ainsi que nos graphiques d'explications
des données, est le "Projet Météo.ipynb" présent dans ce même dossier.

# Commandes pour l'installation et le lancement de la Web App : 

## (-> Dans le dossier du projet) :  

### Créer un environnement virtuel
- python -m venv .venv 

### Accéder à l'environnement virtuel
- .venv\Scripts\Activate.ps1 

### Installer les requirements
- pip install streamlit 
- pip install joblib
- pip install sklearn

### Lancer la web App en localhost
- streamlit run Accueil.py 