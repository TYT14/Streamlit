import streamlit as st
import pandas as pd
import requests


st.title("My Dashboard")



# 1 Bouton upload .csv

if st.checkbox("Uploader un fichier svp") :
 uploaded_file = st.file_uploader("Choisir un fichier pour upload")
 if uploaded_file is not None:
    # To read file as bytes:
    

    
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file,sep=';')
    st.write(dataframe)

# 2 selection d'une variable avec df.columns & st.selectbox
user_selection = st.selectbox('Selectionner une profession', df.columns)

