import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from PIL import Image

st.sidebar.title("Menu")
page = st.sidebar.radio("Choose what you need",["FitMind - Introduction", "Fitness", "Mental Health", "Food & Recipes"])

if page == "FitMind - Introduction":
    st.title("FitMind")
    
elif page == "Fitness":
    st.title("Fitness")
    
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
    st.write("Stand with your feet wider than your Hips and feet pointed slightly out.")
    st.write("Begin bendin your knees until parallel to the floor with your back as straight as possible.")
    st.write("Push back up until you reach standing positions.")
    st.write("Repeat.")
    st.video('https://youtu.be/xqvCmoLULNY')

    st.subheader("Narrow Squats")

    st.subheader("Sumo Squats")
    
elif page == "Mental Health":
    st.title("Mental Health")
    st.write("Hier finden Sie Informationen über unser Team und unsere Mission.")

elif page == "Food & Recipes":
    st.title("Food & Recipes")

