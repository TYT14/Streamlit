import streamlit as st
import pandas as pd
import requests




st.title("My Dashboard")



# 1 Bouton upload .csv

if st.checkbox("Uploader un fichier svp") :
 uploaded_file = st.file_uploader("Choisir un fichier pour upload")
 if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file,sep=';')
    st.write(dataframe)

# 2 selection d'une variable avec df.columns & st.selectbox
columns = dataframe.columns
user_selection = st.selectbox('Selectionner une variable', columns)

# 3 Affichage de la varable sous forme de graphique
columns_selected = dataframe[user_selection]
fig, ax = plt.subplots()
ax.hist(columns_selected, bins=20)

st.pyplots(fig)


