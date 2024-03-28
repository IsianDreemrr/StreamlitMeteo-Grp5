import streamlit as st
import datetime
from datetime import date
import pandas as pd
from functions import *


st.set_page_config(
    page_icon=':file_folder:'
)


st.title("Météorologie - Groupe 5")
st.subheader("Sources")
st.write("---")

text_side = """
Ici, vous trouverez des détails sur nos sources de données,
et donc le dataset utilisé pour nos prédictions.
"""
st.write(text_side)


st.write("---")

if st.button("Données du dataset source"):
    df_full = get_données("data_source.csv")
    st.write(df_full)


if st.button("Données du dataset après entrainement"):
    df_full = get_données("data_trained.csv")
    st.write(df_full)



# Noms dans la sidebar
st.sidebar.markdown("Ahmed Amine BOUTHALEB")
st.sidebar.markdown("Fatima OUDAHMANE")
st.sidebar.markdown("Ayse YILDRIM")
st.sidebar.markdown("Florian ALVAREZ RODRIGUEZ")
