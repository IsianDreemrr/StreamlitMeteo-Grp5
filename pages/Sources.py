import streamlit as st
import datetime
from datetime import date
import pandas as pd
from functions import *


st.set_page_config(
    page_icon=':file_folder:'
)

# Noms dans la sidebar
st.sidebar.markdown("Ahmed Amine BOUTHALEB")
st.sidebar.markdown("Fatima OUDAHMANE")
st.sidebar.markdown("Ayse YILDRIM")
st.sidebar.markdown("Florian ALVAREZ RODRIGUEZ")


st.title("Météorologie - Groupe 5")
st.header("Sources")
st.write("---")

text_side = """
Ici, vous trouverez des détails sur nos sources de données,
et donc le dataset utilisé pour nos prédictions.
"""
st.write(text_side)


st.write("---")
st.subheader("Données sources")
st.write("""Ici, les données avant nettoyage.""")

if st.button("Données du dataset source"):
    df_full = get_données("data_source.csv")
    st.write(df_full)


st.write("---")
st.subheader("Données transformées")
st.write("""Ici, les données après nettoyage.\n 
Par souci de taille, nous n'utilisons que les données à partir de l'an 2000.""")


if st.button("Données du dataset après entrainement"):
    df_full = get_données("data_trained.csv")
    st.write(df_full)


st.write("---")
st.subheader("Téléchargements")

st.write("Les fichiers peuvent mettre du temps avant d'être disponibles. Veuillez patienter.")

st.download_button(
    label="Télécharger data_source.csv",
    data=(get_données("data_source.csv", True).to_csv().encode('utf-8')),
    file_name='data_source.csv',
    mime='text/csv',
)

st.download_button(
    label="Télécharger data_trained.csv",
    data=(get_données("data_trained.csv", True).to_csv().encode('utf-8')),
    file_name='data_trained.csv',
    mime='text/csv',
)





