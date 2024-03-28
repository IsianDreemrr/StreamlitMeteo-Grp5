import streamlit as st
import datetime
from datetime import date
import pandas as pd
from functions import *


st.set_page_config(
    page_icon=':file_folder:'
)


st.title("Météorologie - Groupe 5")
st.write("---")

text_side = """
Ici, vous trouverez des détails sur nos sources de données,
et donc le dataset utilisé pour nos prédictions.
"""

st.write(text_side)


# Noms dans la sidebar
st.sidebar.markdown("Ahmed Amine BOUTHALEB")
st.sidebar.markdown("Fatima OUDAHMANE")
st.sidebar.markdown("Ayse YILDRIM")
st.sidebar.markdown("Florian ALVAREZ RODRIGUEZ")
