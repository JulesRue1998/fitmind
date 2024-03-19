import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime


st.sidebar.title("Menu")
page = st.sidebar.radio("Choose what you need",["FitMind - Introduction", "Fitness", "Mental Health", "Food & Recipes"])

if page == "FitMind - Introduction":
    st.title("FitMind")

elif page == "Fitness":
    st.title("Fitness")
    
    st.title("workouts")
    st.subheader("Beginners")
    st.write("If you're new to exercise or a particular exercise, start with 1 to 2 sets per exercise. Focus on learning proper form and gradually increasing the number of sets as you become more comfortable with the movements.")
    st.subheader("Intermediate")
    st.write("Intermediate: For those who have been exercising regularly and have some experience with the exercises, aim for 3 to 4 sets per exercise. This provides enough volume to challenge your muscles and promote strength and muscle growth.")
    st.subheader("Advanced")
    st.write("Advanced individuals who are looking to increase muscle size or strength may benefit from performing 4 to 5 sets per exercise. Higher volume workouts can help stimulate muscle hypertrophy and strength gains.")

    st.subheader("Choose your Workouts")

    st.subheader("Squats")
    st.video('https://youtu.be/xqvCmoLULNY')
    
elif page == "Mental Health":
    st.title("Mental Health")
    st.write("Hier finden Sie Informationen über unser Team und unsere Mission.")

elif page == "Food & Recipes":




