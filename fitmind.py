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

import streamlit as st
import pandas as pd

# Load or create DataFrame to store water intake data
try:
    water_data = pd.read_csv("water_intake.csv")
except FileNotFoundError:
    water_data = pd.DataFrame(columns=['Date', 'Glasses of Water'])

# Function to display water intake form
def display_water_intake_form():
    st.title('Water Intake Tracking')
    st.write('💧 Use this form to track your daily water intake 💧')
    date = st.date_input('Date', pd.Timestamp.now().date())
    glasses = st.slider('Glasses of Water', min_value=0, max_value=20, value=8)
    
    if st.button('Track Water Intake'):
        water_data.loc[len(water_data)] = [date, glasses]
        st.success('Water intake tracked successfully!')

# Function to display water intake history
def display_water_intake_history():
    st.title('Water Intake History')
    if water_data.empty:
        st.write('No water intake data available.')
    else:
        st.write(water_data)

# Function to increment water intake tracker
def increment_water_tracker():
    if st.button('💧'):
        water_data.loc[len(water_data)] = [pd.Timestamp.now().date(), 1]
        st.success('Water intake tracked successfully!')

# Main code
st.sidebar.title('Menu')
menu_option = st.sidebar.radio('Select option', ['Track Water Intake', 'View Water Intake History'])

if menu_option == 'Track Water Intake':
    display_water_intake_form()
elif menu_option == 'View Water Intake History':
    display_water_intake_history()

increment_water_tracker()


elif page == "Food & Recipes":
    st.title("Food & Recipes")




