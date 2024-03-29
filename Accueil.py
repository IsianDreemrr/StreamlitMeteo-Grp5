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
st.write("---")

text_side = """
Bienvenue sur notre Web App!
Ici, vous pourrez retrouver des informations et prédictions météorologiques. 
Ces données sont basées sur les données officielles françaises trouvables sur https://meteo.data.gouv.fr/
"""
st.write(text_side)


st.write("---")
st.header("Estimation")
st.subheader("Estimez la température à une date précise")
st.write("---")

# NUM_POSTE,NOM_USUEL,LAT,LON,ALTI,AAAAMMJJ,RR,QRR,TN,QTN,TX,QTX,TM,TNTXM,QTNTXM,TAMPLI,QTAMPLI
# 1014002,ARBENT,46.278167,5.669,534,2004-03-17,0.0,1.0,6.234074634685917,1.000349276574126,24.7,1.0,10.853922639491019,11.349192305859557,1.0002541174975779,10.1921687289208,1.0002541174975779


form_date_input = st.date_input("Date de la prévision", value="default_value_today", format="YYYY-MM-DD")
# ------------
form_poste_input = st.selectbox("Localisation",get_list_postes())
index_poste = [index for index, value in enumerate(get_list_postes()) if value == form_poste_input]
# index_posteID = [index for index, value in enumerate(get_list_postesID()) if value == form_poste_input]
# form_poste = index_poste[0]
# form_posteID = index_posteID[form_poste]
st.write("Numéro de poste : "+str(get_NUM_POSTE(form_poste_input)))
st.write("Latitude : "+str(get_LAT(form_poste_input)))
st.write("Longitude : "+str(get_LON(form_poste_input)))
st.write("Altitude : "+str(get_ALTI(form_poste_input)))

# ------------


data = {
    'NUM_POSTE': [get_NUM_POSTE(form_poste_input)],
    'LAT': [get_LAT(form_poste_input)],
    'LON': [get_LON(form_poste_input)],
    'ALTI': [get_ALTI(form_poste_input)],
    }

if st.button("Estimer la température"):


    retour = predict_with(pd.DataFrame(data))
    # st.markdown(retour)
    if retour:
        st.markdown("La température estimée est de "+str(retour)+"C°")


