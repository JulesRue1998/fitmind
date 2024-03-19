import streamlit as st
import pandas as pd

st.title('FitMind')

st.subheader('Fitness')

st.subheader('Mental Health')


st.sidebar.title("Menu")

page = st.sidebar.radio("FitMind", ["Fitness", "Mental Health"])

if page == "Fitness":
    st.title("Fitness")
    st.write("Hier können Sie Informationen über unsere Anwendung finden.")
elif page == "Mental Health":
    st.title("Mental Health")
    st.write("Hier finden Sie Informationen über unser Team und unsere Mission.")

