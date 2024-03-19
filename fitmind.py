import streamlit as st
import pandas as pd

st.title('FitMind')

st.subtitle('Fitness')

st.subtitle('Mental Health')


st.sidebar.title("Menu")

page = st.sidebar.radio("FitMind", ["Fitness", "Mental Health"])


