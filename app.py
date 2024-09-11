import streamlit as st
import pandas as pd

st.title("My Dashboard")

df = pd.read_csv('data.csv')

if st.checkbox("affichage le jeu de données"):
  st.write(df)

pro = df.Profession.unique()

st.selectbox('Selexctionner une profession', pro)

st.write(df)
