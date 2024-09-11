import streamlit as st
import pandas as pd
import requests
import seaborn as sns


st.title("My Dashboard")



# 1 Bouton upload .csv

if st.checkbox("Uploader un fichier svp") :
 uploaded_file = st.file_uploader("Choisir un fichier pour upload")
 if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

# 2 selection d'une variable avec df.columns & st.selectbox
columns = dataframe.columns
user_selection = st.selectbox('Selectionner une variable', columns)

# 3 Affichage de la varable sous forme de graphique
st.write(dataframe)


