import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

st.sidebar.header("Menu")
page = st.sidebar.radio("Choose what you need",["FitMind - Introduction", "Fitness", "Mental Health", "Food & Recipes"])

if page == "FitMind - Introduction":
    st.title("Welcome to FitMind!")
    st.markdown("""
    FitMind is a health app that combines fitness and mental wellbeing to help users lead a balanced and healthy life.
    """)
    st.write("FitMind helps you to achieve your fitness goals and improve your mental well-being at the same time.")

elif page == "Fitness":
    st.title("Fitness")
    st.subheader("Choose your level")
    st.subheader("Beginners")
    st.write("If you're new to exercise or a particular exercise, start with 1 to 2 sets per exercise. Focus on learning proper form and gradually increasing the number of sets as you become more comfortable with the movements.")
    st.subheader("Intermediate")
    st.write("Intermediate: For those who have been exercising regularly and have some experience with the exercises, aim for 3 to 4 sets per exercise. This provides enough volume to challenge your muscles and promote strength and muscle growth.")
    st.subheader("Advanced")
    st.write("Advanced individuals who are looking to increase muscle size or strength may benefit from performing 4 to 5 sets per exercise. Higher volume workouts can help stimulate muscle hypertrophy and strength gains.")
   
    st.divider()
    
    if page == "Fitness":
        st.sidebar.subheader("Workouts")
        
        Workouts = [" ", "Arms", "Abs", "Legs", "Butt"]
        selected_subcategory = st.sidebar.selectbox("Choose a specific area", Workouts)
                
    if selected_subcategory == " ":
        st.subheader(" ")
        st.write(" ")
        
    elif selected_subcategory == "Arms":
        st.subheader("Arms")
        st.write("Content for Cardio category")
    
    elif selected_subcategory == "Abs":
        st.subheader("Abs")
        st.write("Content for Strength Training category")
        
    elif selected_subcategory == "Legs":
        st.subheader("Legs")
        st.write("Content for Flexibility category")
        
    elif selected_subcategory == "Butt":
        st.subheader("Butt")
        st.write("Content for Endurance category")
        st.subheader("Squats")
        st.write("Instructions:")
        st.write(" 1. Stand with your feet wider than your Hips and feet pointed slightly out.")
        st.write(" 2. Begin bendin your knees until parallel to the floor with your back as straight as possible.")
        st.write(" 3. Push back up until you reach standing positions.")
        st.write(" 4. Repeat.")
        st.video('https://youtu.be/xqvCmoLULNY')

        st.subheader("Lunges")
    
        st.subheader("Narrow Squats")
    
        st.subheader("Sumo Squats")
        
    st.sidebar.subheader("Planned Programms")
    second_subcategory = st.sidebar.selectbox("Choose a second subcategory", [" ", "Summerbody", "Get That Booty", "VERY HARD ABS"])
   
    if second_subcategory == " ":
        st.subheader(" ")
        st.write(" ")
    
    elif second_subcategory == "Summerbody":
        st.subheader("Summerbody")
        st.write("Summerbody")
        
    elif second_subcategory == "Get That Booty":
        st.subheader("Get That Booty")
        st.write("Get That Booty")
        
    elif second_subcategory == "VERY HARD ABS":
        st.subheader("ABS ABS ABS")

    st.sidebar.subheader("Fitness Tracker")
    third_subcategory = st.sidebar.selectbox("Choose a third subcategory", ["  ", "Suboption 1", "Suboption 2"])
    
    if third_subcategory == " ":
        st.write(" ")
        
    elif third_subcategory == "Suboption 1":
        st.write("Content for Suboption 1")
        
    elif third_subcategory == "Suboption 2":
        st.write("Content for Suboption 2")


elif page == "Mental Health":
    st.title("Mental Health")
    st.write("Hier finden Sie Informationen über unser Team und unsere Mission.")

elif page == "Food & Recipes":
    st.title("Food & Recipes")
