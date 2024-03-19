import streamlit as st
import pandas as pd

st.title('FitMind')

st.sidebar.title("Menu")

page = st.sidebar.radio("Navigation",["Fitness", "Mental Health"])

if page == "Fitness":
    st.title("Fitness")
    st.write("Hier können Sie Informationen über unsere Anwendung finden.")
    st.subheader("Squats")
    st.write("Stand with your feet shoulder-width apart, lower your body by bending your knees, and then return to the starting position.")
    st.write("Squats primarily target the legs and glutes.")
    st.subheader("Pushups")
elif page == "Mental Health":
    st.title("Mental Health")
    st.write("Hier finden Sie Informationen über unser Team und unsere Mission.")

