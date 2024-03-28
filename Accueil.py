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
Bienvenue sur notre Web App!
Ici, vous pourrez retrouver des informations et prédictions météorologiques. 
Ces données sont basées sur les données officielles françaises trouvables sur https://meteo.data.gouv.fr/
"""

st.write(text_side)


# Noms dans la sidebar
st.sidebar.markdown("Ahmed Amine BOUTHALEB")
st.sidebar.markdown("Fatima OUDAHMANE")
st.sidebar.markdown("Ayse YILDRIM")
st.sidebar.markdown("Florian ALVAREZ RODRIGUEZ")
