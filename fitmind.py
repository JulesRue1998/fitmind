import streamlit as st
import pandas as pd

st.title('FitMind')

st.subtitle('Fitness')

st.subtitle('Mental Health')


st.sidebar.title("Menu")

page = st.sidebar.radio("FitMind", ["Fitness", "Mental Health"])

# Abhängig von der ausgewählten Seite wird der entsprechende Inhalt angezeigt
if page == "Fitness":
    st.title("Willkommen auf der Startseite")
    st.write("Hier können Sie Informationen über unsere Anwendung finden.")
elif page == "Mental Health":
    st.title("Mental Health")
    st.write("Hier finden Sie Informationen über unser Team und unsere Mission.")
