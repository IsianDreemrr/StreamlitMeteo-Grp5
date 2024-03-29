import joblib
import datetime
from datetime import date
import pandas as pd
import sklearn
import os
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
import pickle

import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.linear_model import Ridge
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.ensemble import _gb_losses


from os import listdir
from os.path import isfile, join

# Prédire avec le modèle par défaut
def predict(data):
    clf = joblib.load("./models/model.keras")
    return clf.predict(data)

# Prédire avec un modèle en particulier
def predict_with(data, model="model.keras"):
    clf = joblib.load("./models/"+model)
    return clf.predict(data)

# Récupération d'un dataframe 
def get_données(dataset="data_trained.csv", full=False):
    df = pd.read_csv('./data/'+dataset, sep=";")
    if (dataset == "data_source.csv" and full==False):
        return df.head(10000)
    else: return df


# Récupération d'un dataframe 
def get_list_postes(dataset="data_trained.csv"):
    df = pd.read_csv('./data/'+dataset)
    return df['NOM_USUEL'].unique()

def get_NUM_POSTE(nom_usuel, dataset="data_trained.csv"):
    df = pd.read_csv('./data/'+dataset)
    return (df.loc[df['NOM_USUEL'] == nom_usuel, 'NUM_POSTE']).head(1).iloc[0]


def get_LAT(nom_usuel, dataset="data_trained.csv"):
    df = pd.read_csv('./data/'+dataset)
    return (df.loc[df['NOM_USUEL'] == nom_usuel, 'LAT']).head(1).iloc[0]

def get_LON(nom_usuel, dataset="data_trained.csv"):
    df = pd.read_csv('./data/'+dataset)
    return (df.loc[df['NOM_USUEL'] == nom_usuel, 'LON']).head(1).iloc[0]

def get_ALTI(nom_usuel, dataset="data_trained.csv"):
    df = pd.read_csv('./data/'+dataset)
    return (df.loc[df['NOM_USUEL'] == nom_usuel, 'ALTI']).head(1).iloc[0]

