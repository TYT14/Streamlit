import streamlit as st
import pandas as pd
import requests


st.title("My Dashboard")

df = pd.read_csv('data.csv')

if st.checkbox("affichage le jeu de données"):
  st.write(df)

pro = df.Profession.unique()

user_selection = st.selectbox('Selexctionner une profession', pro)

st.slider("Sélectionner un âge", min_value=20, max_value=100, value=30, step=1)

if st.checkbox("Affichage le jeu de données"):
  st.write(df[(df.Profession == user_selection)])

# 1 Bouton upload .csv

if st.checkbox("Uploader un fichier svp") :
 uploaded_file = st.file_uploader("Choisir un fichier pour upload")
  
# 2 Selection d'un variable

# 3 Affichage d'un graphique

# 4 




