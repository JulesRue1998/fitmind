import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import random

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
    second_subcategory = st.sidebar.selectbox("Choose a second subcategory", [" ", "Summerbody", "Get That Booty", "VERY HARD ABS", "Oberkörper", "Unterkörper"])
   
    if second_subcategory == " ":
        st.subheader(" ")
        st.write(" ")
    
    elif second_subcategory == "Summerbody":
        st.subheader("Summerbody")
        st.write("Summerbody")
        

        tab1, tab2, tab3 = st.tabs(["Beginner", "intermediate", "Advanced"])
        
        with tab1:
           st.header("Beginner Training")
           st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        
        with tab2:
           st.header("Intermediate Training")
           st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        
        with tab3:
           st.header("Advanced Training")
           st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    
        
    elif second_subcategory == "Get That Booty":
        st.subheader("Get That Booty")
        st.write("Get That Booty")
        
        tab1, tab2, tab3 = st.tabs(["Beginner", "intermediate", "Advanced"])
        
        with tab1:
           st.header("Beginner Training")
           st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        
        with tab2:
           st.header("Intermediate Training")
           st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        
        with tab3:
           st.header("Advanced Training")
           st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
        
    elif second_subcategory == "VERY HARD ABS":
        st.subheader("ABS ABS ABS")
        
        tab1, tab2, tab3 = st.tabs(["Beginner", "intermediate", "Advanced"])
        
        with tab1:
           st.header("Beginner Training")
           st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
                    
        with tab2:
           st.header("Intermediate Training")
           st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        
        with tab3:
           st.header("Advanced Training")
           st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    elif second_subcategory == "Oberkörper":
        st.subheader("Arme, Rücken, Brust")

        tab1, tab2, tab3 = st.tabs(["Beginner", "intermediate", "Advanced"])
        
        with tab1:
           st.header("Beginner Training")
           st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        
        with tab2:
           st.header("Intermediate Training")
           st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        
        with tab3:
           st.header("Advanced Training")
           st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    elif second_subcategory == "Unterkörper":
        st.subheader("Bauch, Beine, Po")

        tab1, tab2, tab3 = st.tabs(["Beginner", "Intermediate", "Advanced"])

        with tab1:
           st.header("Beginner Training")
           st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        
        with tab2:
           st.header("Intermediate Training")
           st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        
        with tab3:
           st.header("Advanced Training")
           st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    st.sidebar.subheader("Randomized workout")
    third_subcategory = st.sidebar.selectbox("Choose a randomized workout", ["  ", "Arms", "Abs", "Back", "Butt", "Legs"])
    
    if third_subcategory == " ":
        st.subheader(" ")
        st.write(" ")

    
    elif third_subcategory == "Arms":
        st.subheader("Randomized Arm Workout")

        tab1, tab2, tab3 = st.tabs(["Beginner", "Intermediate", "Advanced"])

        with tab1:
           st.header("Beginner Training")
           st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        
        with tab2:
           st.header("Intermediate Training")
           st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        
        with tab3:
           st.header("Advanced Training")
           st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
            

        
    elif third_subcategory == "Abs":
        st.subheader("Randomized Abs Workout")

        tab1, tab2, tab3 = st.tabs(["Beginner", "Intermediate", "Advanced"])

        with tab1:
           st.header("Beginner Training")
           st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        
        with tab2:
           st.header("Intermediate Training")
           st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        
        with tab3:
           st.header("Advanced Training")
           st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
            

    elif third_subcategory == "Back":
        st.subheader("Randomized Back Workout")

        tab1, tab2, tab3 = st.tabs(["Beginner", "Intermediate", "Advanced"])

        with tab1:
           st.header("Beginner Training")
           st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        
        with tab2:
           st.header("Intermediate Training")
           st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        
        with tab3:
           st.header("Advanced Training")
           st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


    elif third_subcategory == "Butt":
        butt_fitness_übungen = [
            "Squats",
            "Lunges",
            "Hip Thrusts",
            "Deadlifts",
            "Donkey Kicks",
            "Fire Hydrants"
        ]
        st.subheader("Randomized Butt Workout")

        tab1, tab2, tab3 = st.tabs(["Beginner", "Intermediate", "Advanced"])

        with tab1:
           st.header("Beginner Training")
           st.write("Hier könnten Anfängerübungen stehen, die spezifisch für den Hintern sind.")
           st.write("Zufällige Übungen für Anfänger:")
           zufällige_übungen_beginner = random.sample(butt_fitness_übungen, 3)
           for übung in zufällige_übungen_beginner:
           st.write(übung)
          
        elif third_subcategory == "Abs":
            st.subheader("Randomized Abs Workout")

        
        with tab2:
           st.header("Intermediate Training")
           st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        
        with tab3:
           st.header("Advanced Training")
           st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
            

    elif third_subcategory == "Legs":
        st.subheader("Randomized Leg Workout")

        tab1, tab2, tab3 = st.tabs(["Beginner", "Intermediate", "Advanced"])

        with tab1:
           st.header("Beginner Training")
           st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        
        with tab2:
           st.header("Intermediate Training")
           st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        
        with tab3:
           st.header("Advanced Training")
           st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    st.sidebar.subheader("Fitness Tracker")
    fourth_subcategory = st.sidebar.selectbox("Choose a Fitness Tracker", ["  ", "water intake", "Calorie tracker", "Workout tracker"])
    
    if fourth_subcategory == " ":
        st.write(" ")
        
    elif fourth_subcategory == "water intake":
        st.subheader("Track your water intake")
        if "water_intake" not in st.session_state:
            st.session_state.water_intake = 0
        
        # Display the water emoji
        water_emoji = "💧"
        st.write("if you drank a glass of water, press the button below!", water_emoji)
        
        # Add a button to increment the water intake counter when clicked
        if st.button("Drink a glass of water", water_emoji):
            st.session_state.water_intake += 1
            st.write("You drank a glass of water!")
            st.write("Total glasses of water drank today:", st.session_state.water_intake)


        
    elif fourth_subcategory == "Calorie traker":
        st.write("Content for Suboption 2")

    elif fourth_subcategory == "Workout tracker":
        st.subheader("Workout tracker")
        st.write("Define your Goals here. write down what you achieved")
        
        diary_data = pd.read_csv("diary.csv") if "diary.csv" in st.session_state else pd.DataFrame(columns=["Date", "Entry"])
            
        st.subheader("Diary")
        entry_date = st.date_input("Date", value=pd.Timestamp.now())
        entry_text = st.text_area("Enter your diary entry")
            
        if st.button("Save Entry"):
            diary_data = diary_data.append({"Date": entry_date, "Entry": entry_text}, ignore_index=True)
            diary_data.to_csv("diary.csv", index=False)
            st.success("Entry saved successfully!")
            
        if not diary_data.empty:
            st.subheader("Previous Entries")
            st.write(diary_data)
        else:
             st.info("No entries yet.")



elif page == "Mental Health":
    st.sidebar.subheader("Mental Health Subcategories")
    Mental_Health_Subcategories = [" ", "Stresslevel tracker ", "Mood tracker", "Sleep tracker"]
    selected_subcategory = st.sidebar.selectbox("Choose a tracker", Mental_Health_Subcategories)
  
    if selected_subcategory == " ":
        st.write(" ")
    
    elif selected_subcategory == "Stresslevel tracker":
        st.write("Track your Stresslevels")
    
    elif selected_subcategory == "Mood tracker":
        st.write("Track your mood")
    
    elif selected_subcategory == "Sleep tracker":
        st.write("track your sleeping hours")



elif page == "Food & Recipes":
    st.title("Food & Recipes")

    st.sidebar.subheader("Food & Recipes")
    food_subcategories = ["Breakfast", "Lunch", "Dinner", "Snacks"]
    selected_subcategory = st.sidebar.selectbox("Choose a subcategory", food_subcategories)
    
    if selected_subcategory == "Breakfast":
        st.write("Breakfast Recipes")
        
        st.sidebar.subheader("Breakfast Subcategories")
        breakfast_subcategories = ["Eggs", "Toast", "Müsli"]
        selected_breakfast_subcategory = st.sidebar.selectbox("Choose a breakfast", breakfast_subcategories)
        
        if selected_breakfast_subcategory == "Eggs":
            st.write("Egg Recipes")
            # Hier kannst du spezifische Rezepte für Eier anzeigen
            
        elif selected_breakfast_subcategory == "Toast":
            st.write("Toast Recipes")
            # Hier kannst du spezifische Rezepte für Haferflocken anzeigen
            
        elif selected_breakfast_subcategory == "Müsli":
            st.write("Müsli Recipes")
            # Hier kannst du spezifische Rezepte für Smoothies anzeigen
            
    elif selected_subcategory == "Lunch":
        st.write("Lunch Recipes")
        # Hier kannst du spezifische Rezepte für das Mittagessen anzeigen
        st.sidebar.subheader("Lunch Subcategories")
        Lunch_subcategories = ["Ceasar Salad", "Omurice", "Sandwiches"]
        selected_Lunch_subcategory = st.sidebar.selectbox("Choose a Lunch ", Lunch_subcategories)
        
        if selected_Lunch_subcategory == "Ceasar Salad":
            st.write("Ceasar Salad Recipes")
            # Hier kannst du spezifische Rezepte für Eier anzeigen
            
        elif selected_Lunch_subcategory == "Omurice":
            st.write("Omurice Recipes")
            # Hier kannst du spezifische Rezepte für Haferflocken anzeigen
            
        elif selected_Lunch_subcategory == "Sandwiches":
            st.write("Sandwiches Recipes")
            # Hier kannst du spezifische Rezepte für Smoothies anzeigen
        
    elif selected_subcategory == "Dinner":
        st.write("Dinner Recipes")
        # Hier kannst du spezifische Rezepte für das Abendessen anzeigen
        st.sidebar.subheader("Dinner Subcategories")
        Dinner_subcategories = ["Spaghetti", "Salmon", "Feta Pasta"]
        selected_Dinner_subcategory = st.sidebar.selectbox("Choose a Dinner", Dinner_subcategories)
        
        if selected_Dinner_subcategory == "Spaghetti":
            st.write("Spaghetti Recipes")
            # Hier kannst du spezifische Rezepte für Eier anzeigen
            
        elif selected_Dinner_subcategory == "Salmon":
            st.write("Salmon Recipes")
            # Hier kannst du spezifische Rezepte für Haferflocken anzeigen
            
        elif selected_Dinner_subcategory == "Feta Pasta":
            st.write("Feta Pasta Recipes")
            # Hier kannst du spezifische Rezepte für Smoothies anzeigen
        
    elif selected_subcategory == "Snacks":
        st.write("Snack Recipes")
        # Hier kannst du spezifische Rezepte für Snacks anzeigen
        st.sidebar.subheader("Snacks Subcategories")
        Snacks_subcategories = ["Brownies", "Oatmeal", "Smoothies"]
        selected_Snacks_subcategory = st.sidebar.selectbox("Choose a Snack", Snacks_subcategories)
        
        if selected_Snacks_subcategory == "Brownies":
            st.write("Brownies Recipes")
            # Hier kannst du spezifische Rezepte für Eier anzeigen
            
        elif selected_Snacks_subcategory == "Oatmeal":
            st.write("Oatmeal Recipes")
            # Hier kannst du spezifische Rezepte für Haferflocken anzeigen
            
        elif selected_Snacks_subcategory == "Smoothies":
            st.write("Smoothie Recipes")
            # Hier kannst du spezifische Rezepte für Smoothies anzeigen

# Footer
st.sidebar.markdown("---")
st.sidebar.subheader("About us")
st.sidebar.info("This app was developed by Julia and Cherilyn.")

st.sidebar.subheader("Contact")
st.sidebar.text("For questions or suggestions, contact us at")
st.sidebar.text("fitmindbyjc@gmail.com")
