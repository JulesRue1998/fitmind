import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Set page title and favicon
st.set_page_config(page_title="FitMind App", page_icon=":brain:")

# Sidebar layout
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose what you need", ["FitMind - Introduction", "Fitness Tracker", "Mental Health"])

# FitMind Introduction
if page == "FitMind - Introduction":
    st.title("FitMind - Holistische Gesundheits-App")
    st.markdown("""
    FitMind ist eine ganzheitliche Gesundheits-App, die Fitness und mentales Wohlbefinden kombiniert, um Benutzern zu helfen, ein ausgewogenes und gesundes Leben zu führen.
    """)
    st.image("selfcare.jpg", use_column_width=True)
    st.subheader("Willkommen bei FitMind!")
    st.write("FitMind unterstützt dich dabei, deine Fitnessziele zu erreichen und gleichzeitig dein mentales Wohlbefinden zu verbessern.")

if page == "FitMind - Introduction":
    st.title("FitMind")
    st.snow()

# Fitness Tracker
elif page == "Fitness Tracker":
    st.title("Fitness Tracker")
    st.subheader("Tracke deine Fitness und erhalte Empfehlungen")

    # Input Widgets
    age = st.slider("Alter", 18, 100, 25)
    weight = st.number_input("Gewicht (kg)", min_value=20.0, max_value=500.0, value=70.0, step=0.1)
    height = st.number_input("Größe (cm)", min_value=100, max_value=300, value=170, step=1)
    activity_level = st.selectbox("Aktivitätslevel", ["Sedentär", "Leicht aktiv", "Mäßig aktiv", "Sehr aktiv", "Extrem aktiv"])

    # Calculate BMI
    bmi = weight / ((height/100) ** 2)
    st.write(f"Ihr BMI beträgt: {bmi:.2f}")

    # BMI Classification
    bmi_data = pd.DataFrame({
        'Kategorie': ['Untergewicht', 'Normalgewicht', 'Übergewicht', 'Adipositas'],
        'BMI-Bereich': ['< 18.5', '18.5 - 24.9', '25.0 - 29.9', '≥ 30.0'],
        'Empfehlung': ['Zunehmen', 'Normalgewicht halten', 'Abnehmen', 'Stark abnehmen']
    })
    st.write("BMI-Klassifikation:")
    st.dataframe(bmi_data)

    # BMI Chart
    plt.figure(figsize=(8, 6))
    plt.bar(bmi_data['Kategorie'], bmi_data['BMI-Bereich'])
    plt.xlabel('Kategorie')
    plt.ylabel('BMI-Bereich')
    st.pyplot()

# Mental Health
elif page == "Mental Health":
    st.title("Mental Health")
    st.subheader("Überprüfe deine Stimmung und Stresslevel")

    # Mood and Stress Level Input Widgets
    mood = st.slider("Stimmung", 0, 10, 5)
    stress_level = st.slider("Stresslevel", 0, 10, 5)

    # Mood and Stress Level Chart
    mood_data = pd.DataFrame({
        'Datum': pd.date_range(start='2024-01-01', periods=30),
        'Stimmung': np.random.randint(0, 11, size=30),
        'Stresslevel': np.random.randint(0, 11, size=30)
    })
    st.write("Verlauf der Stimmung und des Stresslevels:")
    plt.figure(figsize=(10, 6))
    plt.plot(mood_data['Datum'], mood_data['Stimmung'], label='Stimmung')
    plt.plot(mood_data['Datum'], mood_data['Stresslevel'], label='Stresslevel')
    plt.xlabel('Datum')
    plt.ylabel('Wert')
    plt.legend()
    st.pyplot()

# Footer
st.sidebar.markdown("---")
st.sidebar.subheader("Über uns")
st.sidebar.info("Diese App wurde von Julia und Cherilyn entwickelt.")

st.sidebar.subheader("Kontakt")
st.sidebar.text("Bei Fragen oder Anregungen kontaktieren Sie uns unter:")
st.sidebar.text("fitmind@example.com")
