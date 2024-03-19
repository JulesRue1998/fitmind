import streamlit as st
import pandas as pd

st.title('FitMind')

st.image("https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fthumbnails%2F025%2F220%2F125%2Fsmall_2x%2Fpicture-a-captivating-scene-of-a-tranquil-lake-at-sunset-ai-generative-photo.jpg&tbnid=KnSoW1OO4dAxcM&vet=12ahUKEwigxdCG4ICFAxUEtv0HHXVyBTIQMygAegQIARBM..i&imgrefurl=https%3A%2F%2Fwww.vecteezy.com%2Ffree-photos%2Fpicture&docid=wska7sM6RxRdCM&w=600&h=400&q=picture&client=safari&ved=2ahUKEwigxdCG4ICFAxUEtv0HHXVyBTIQMygAegQIARBM")

st.sidebar.title("Menu")
page = st.sidebar.radio("Navigation",["Fitness", "Mental Health"])

if page == "Fitness":
    st.title("Fitness")
    st.subheader("Beginners")
    st.write("If you're new to exercise or a particular exercise, start with 1 to 2 sets per exercise. Focus on learning proper form and gradually increasing the number of sets as you become more comfortable with the movements.")
    st.subheader("Intermediate")
    st.write("Intermediate: For those who have been exercising regularly and have some experience with the exercises, aim for 3 to 4 sets per exercise. This provides enough volume to challenge your muscles and promote strength and muscle growth.")
    st.subheader("Advanced")
    st.write("Advanced individuals who are looking to increase muscle size or strength may benefit from performing 4 to 5 sets per exercise. Higher volume workouts can help stimulate muscle hypertrophy and strength gains.")
    st.title("workouts")
    st.subheader("Squats")
    st.write("Stand with your feet shoulder-width apart, lower your body by bending your knees, and then return to the starting position.")
    st.write("Squats primarily target the legs and glutes.")
    st.subheader("Pushups")
elif page == "Mental Health":
    st.title("Mental Health")
    st.write("Hier finden Sie Informationen über unser Team und unsere Mission.")

