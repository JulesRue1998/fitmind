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

# Create a DataFrame to store health data
health_data = pd.DataFrame(columns=['Date', 'Sleep Hours', 'Exercise (minutes)', 'Calories Consumed'])

# Function to display the health tracking form
    def display_health_form():
    date = st.date_input('Date', datetime.today())
    sleep_hours = st.number_input('Sleep Hours', min_value=0, max_value=24, step=0.5)
    exercise_minutes = st.number_input('Exercise (minutes)', min_value=0, max_value=1440, step=5)
    calories_consumed = st.number_input('Calories Consumed', min_value=0, step=10)
    
    if st.button('Add Entry'):
        health_data.loc[len(health_data)] = [date, sleep_hours, exercise_minutes, calories_consumed]
        st.success('Health entry added successfully!')

# Function to display the health tracking calendar
    def display_health_calendar():
    st.title('Health Tracking Calendar')
    
    # Display the calendar interface
    selected_date = st.calendar_header("Pick a date")
    
    # Filter health data for the selected date
    selected_date = pd.Timestamp(selected_date)
    filtered_data = health_data[health_data['Date'].dt.date == selected_date.date()]
    
    if not filtered_data.empty:
        st.write(filtered_data)
    else:
        st.write('No health data available for selected date.')

# Main code
st.sidebar.title('Menu')
menu_option = st.sidebar.radio('Select option', ['Add Health Entry', 'View Calendar'])

if menu_option == 'Add Health Entry':
    display_health_form()
elif menu_option == 'View Calendar':
    display_health_calendar()

elif page == "Food & Recipes":
    st.title("Food & Recipes")




