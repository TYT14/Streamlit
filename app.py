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
 if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
