import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

st.sidebar.header("Menu")
page = st.sidebar.radio("Choose what you need",["FitMind - Introduction", "Fitness", "Mental Health", "Food & Recipes"])

if page == "FitMind - Introduction":
    st.title("FitMind")
    
elif page == "Fitness":
    st.title("Fitness")
    st.subheader("Choose your level")
    st.subheader("Beginners")
    st.write("If you're new to exercise or a particular exercise, start with 1 to 2 sets per exercise. Focus on learning proper form and gradually increasing the number of sets as you become more comfortable with the movements.")
    st.subheader("Intermediate")
    st.write("Intermediate: For those who have been exercising regularly and have some experience with the exercises, aim for 3 to 4 sets per exercise. This provides enough volume to challenge your muscles and promote strength and muscle growth.")
    st.subheader("Advanced")
    st.write("Advanced individuals who are looking to increase muscle size or strength may benefit from performing 4 to 5 sets per exercise. Higher volume workouts can help stimulate muscle hypertrophy and strength gains.")
   
    st.title("workouts")
    st.subheader("Choose your Workouts")

    st.subheader("Lunges")

    st.subheader("Squats")
    st.write("Instructions:")
    st.write(" 1. Stand with your feet wider than your Hips and feet pointed slightly out.")
    st.write(" 2. Begin bendin your knees until parallel to the floor with your back as straight as possible.")
    st.write(" 3. Push back up until you reach standing positions.")
    st.write(" 4. Repeat.")
    
    st.video('https://youtu.be/xqvCmoLULNY')

    st.subheader("Narrow Squats")

    st.subheader("Sumo Squats")

     if page == "Fitness":
        st.sidebar.subheader("Planned Programms")
        
        Planned_Programms = ["Arms", "Abs", "Legs", "Butt"]
        selected_subcategory = st.sidebar.selectbox("Choose a planned programm", Planned_Programms)
        
     if selected_subcategory == "Arms":
            st.write("Content for Cardio category")
     elif selected_subcategory == "Abs":
            st.write("Content for Strength Training category")
     elif selected_subcategory == "Legs":
            st.write("Content for Flexibility category")
     elif selected_subcategory == "Butt":
            st.write("Content for Endurance category")

elif page == "Mental Health":
    st.title("Mental Health")
    st.write("Hier finden Sie Informationen über unser Team und unsere Mission.")

elif page == "Food & Recipes":
    st.title("Food & Recipes")
