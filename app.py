import Streamlit as st
import pandas as pd

st.title("My Dashboard")

df = pd.read_csv('fr-en-evaluations_nationales_4eme_departement.csv')

st.write(df)
