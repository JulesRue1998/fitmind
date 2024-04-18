import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import random
from streamlit_extras.colored_header import colored_header

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
    st.write("If you're new to exercise or a particular exercise, start with 1 to 2 sets with 10 repetitions per exercise. Focus on learning proper form and gradually increasing the number of sets as you become more comfortable with the movements.")
    st.subheader("Intermediate")
    st.write("Intermediate: For those who have been exercising regularly and have some experience with the exercises, aim for 3 to 4 sets with 10 repetitions per exercise. This provides enough volume to challenge your muscles and promote strength and muscle growth.")
    st.subheader("Advanced")
    st.write("Advanced individuals who are looking to increase muscle size or strength may benefit from performing 4 to 5 sets with 10 repetitions per exercise. Higher volume workouts can help stimulate muscle hypertrophy and strength gains.")
   
    st.divider()
    
    if page == "Fitness":
        st.sidebar.subheader("Workouts")
        
        Workouts = [" ", "Arms", "Back", "Core", "Glutes", "Legs"]
        selected_subcategory = st.sidebar.selectbox("Choose a specific area", Workouts)
                
    if selected_subcategory == " ":
        st.subheader(" ")
        st.write(" ")
        
    elif selected_subcategory == "Arms":
        st.subheader("Arm Training")
        st.write("Content for Cardio category")
        
    elif selected_subcategory == "Back":
        st.subheader("Back Training")
    
    elif selected_subcategory == "Core":
        st.subheader("Core Training")
        st.write("Content for Core-Strength Training category")
        st.divider()
        
        st.subheader("Ab Rollouts")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        st.divider()
       
        st.subheader("Boat pose")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Sit on the floor with your legs extended in front of you. Keep your spine tall and your hands resting on the floor beside your hips for support.")
            st.write("2. As you exhale, lean back slightly and lift your feet off the ground. Your torso and legs should form a V shape.")
            st.write("3. Balance on your glutes while keeping your spine straight. Avoid rounding your back; instead, imagine lengthening through the crown of your head.")
            st.write("4. Extend your arms straight out in front of you, parallel to the floor, with your palms facing each other. Alternatively, you can hold onto the backs of your thighs for additional support, especially if you're a beginner.")
            st.write("5. Take deep breaths in and out as you hold the pose. Aim to maintain steady, even breaths to help you stay focused and relaxed.")
            st.write("6. Hold the pose for as long as you feel comfortable, aiming for 10-30 seconds to start. As you become more experienced, you can gradually increase the duration of your hold.")
            st.write("7. To release the pose, exhale as you lower your feet back to the floor, returning to a seated position with your legs extended.")
            st.write("8. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/VN-6jygZ094')
            st.write("Video Source: https://youtu.be/VN-6jygZ094")
        st.divider()
        
        st.subheader("Crunches")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie down on the floor with your knees bent and your feet planted hip-width apart.")
            st.write("2. Place your hands crossing over your chest OR with your elbows out wide with your hands behind your head, with your fingers grazing your ears.")
            st.write("3. Relax your shoulders and keep your gaze neutral and tuck your chin slightly towards your chest.")
            st.write("4. Inhale, drawing your abdomen in towards your spine. Exhale and lift your head, neck and shoulder blades off the floor, curling inwards.")
            st.write("5. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/nt9jwky07jc')
            st.write("Video Source: ")

        st.subheader("Variation: Bicycle Crunches")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie down on the floor with your knees bent and your feet planted hip-width apart.")
            st.write("2. Place your hands gently on your head with your elbows out wide, with your fingers grazing your ears.")
            st.write("3. Lift one leg off the ground and straighten it outwards, raising the opposite knee upwards towards your chest.")
            st.write("4. Lift your chest upwards and turn your torso—opposite elbow to opposite knee.")
            st.write("5. Lower back to a neutral position with your knees raised. Switch to the other side—opposite elbow and opposite knee")
            st.write("6. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/cbKIDZ_XyjY')
            st.write("Video Source: https://youtu.be/cbKIDZ_XyjY")
          
        st.subheader("Variation: Reverse Crunches")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lie down on the floor with your knees bent and your feet planted hip-width apart.")
            st.write("2. Place your hands on the floor by your side.")
            st.write("3. Inhale, contract your abs towards your spine.")
            st.write("4. Exhale and lift your feet off the floor and raise your knees upwards and inwards towards your chest, keeping your knees at a 90 degree angle. Your hips should tilt inwards to crunch your abs.")
            st.write("5. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/XY8KzdDcMFg')
            st.write("Video Source: https://youtu.be/XY8KzdDcMFg")

        st.subheader("Variation: Standing Oblique Crunches")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Stand with your knees slightly bent, your feet hip-width apart, and your hands behind your head.")
            st.write("2. Shift your weight to the left leg, crunch to the right side, and bring your right knee up toward your elbow.")
            st.write("3. Lower your right leg and return to the starting position.")
            st.write("4. Switch sides.")
            st.write("5. Repeat exercise")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/j12PC1m6va4')
            st.write("Video Source: https://youtu.be/j12PC1m6va4")
        st.divider()
        
        st.subheader("Flutter Kicks")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lay on your back, extending your legs at a 45-degree angle. Your arms should be down at your sides and your legs off the ground.")
            st.write("2. Lift your head, shoulders, and neck slightly off the ground.")
            st.write("3. Start kicking your legs up and down, alternating as you go. Flutter your legs at a pace you can maintain whilst also keeping your core still.")
            st.write("4. Flutter as long as possible.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/ZB1SwBRVLCc')
            st.write("Video Source: https://youtu.be/ZB1SwBRVLCc")
        st.divider()
        
        st.subheader("Lying Leg Raises")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lay supine in a relaxed position with your legs straight and your hands underneath your low back for support.")
            st.write("2. Keep your legs straight and raise them towards your forehead while contracting your abdominals and exhaling.")
            st.write("3. Once your abs are fully contracted and your legs are slightly above parallel, slowly lower your legs back to the starting position.")
            st.write("4. Repeat exercise.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/Wp4BlxcFTkE')
            st.write("Video Source: https://youtu.be/Wp4BlxcFTkE")
        st.divider()
        
        st.subheader("Mountain Climbers")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Get into a plank position, making sure to distribute your weight evenly between your hands and your toes.")
            st.write("2. Check your form—your hands should be about shoulder-width apart, back flat, abs engaged, and head in alignment.")
            st.write("3. Pull your right knee into your chest as far as you can.")
            st.write("4. Switch legs, pulling one knee out and bringing the other knee in.")
            st.write("5. Keep your hips down and run your knees in and out as far and as fast as you can. Alternate inhaling and exhaling with each leg change.")
            st.write("6. Repeat as long as possible.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/kLh-uczlPLg')
            st.write("Video Source: https://youtu.be/kLh-uczlPLg")
        st.divider()
        
        st.subheader("Planks")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Start in a tabletop position on your hands and knees, then lower down to your forearms with your elbows stacked beneath your shoulders.")
            st.write("2. Step your feet back until your body makes a line from shoulders to heels.")
            st.write("3. Squeeze your core and think about pulling your belly button towards your sternum to engage the abs.")
            st.write("4. Hold the position for as long as possible.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/q4rDeHYMcIg')
            st.write("Video Source: https://youtu.be/q4rDeHYMcIg")
        st.divider()

        st.subheader("Variation: Side Planks")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/0Rl5ZQwmS-o')
            st.write("Video Source: ")
        st.divider()
        
        st.subheader("Russian Twists")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Sit on the floor or mat with your knees bent and feet flat on the ground.")
            st.write("2. Sitting up, angle your upper body 45 degrees backward. Keep your back neutral and your shoulders in their natural position in order to maintain good posture and avoid strain.")
            st.write("3. Gently lift your feet a few inches off the ground, being sure to keep your back neutral and at a 45-degree angle throughout.")
            st.write("4. Rotate your arms to one side of your body, and then rotate them to the opposite side.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/VfWoNC-NMII')
            st.write("Video Source: https://youtu.be/VfWoNC-NMII")
        st.divider()
        
        st.subheader("Scissor Kicks")
        with st.expander(":information_source: Read Instructions"):
            st.write("1. Lay on your with your hands on your side.")
            st.write("2. Pick your feet up off the ground 6-8 inches.")
            st.write("3. Bring your right foot over your left foot and then alternate your left foot over your right foot.")
            st.write("4. Alternate back and forth so that it looks like a scissor motion.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://youtu.be/91NZ7XKG1UA')
            st.write("Video Source: https://youtu.be/91NZ7XKG1UA")
        st.divider()
        
        st.subheader("Seated Knee Tucks")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.write("Video Source: ")
        st.divider()
        
        st.subheader("Seated Leg Tugs")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.write("Video Source: ")
        st.divider()
        
        st.subheader("Sit-ups")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.write("Video Source: ")

        st.subheader("Variation: Jackknife Sit-ups")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.write("Video Source: ")
        st.divider()
        
        st.subheader("Toe Touches")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.write("Video Source: ")
        st.divider()
        
        st.subheader("V-ups")
        with st.expander(":information_source: Read Instructions"):
            st.write("")
        with st.expander(":video_camera: Watch Video"):
            st.write("Video Source: ")
        st.divider()
        
        
    elif selected_subcategory == "Glutes":
        st.subheader("Glute Training")
        col1, col2 = st.columns(2)
        with col1:
           st.subheader("Benefits")
           st.write("Glute exercises, are beneficial for several reason: they strenghten the glutes, improve posture and enhance athletic performances. They also enhance and shape your body to your liking.")
           
        with col2:
           st.subheader("Used Muscles")
           st.image("glutes_muscles_480x480.jpeg")
           st.write("Image source: https://asitisnutrition.com/blogs/health/7-exercises-to-achieve-strong-butt-improve-your-posture")
        st.divider()

        st.subheader("Bridge")
        st.write("")
        st.divider()

        st.subheader("Clamshells")
        st.write("")
        st.divider()

        st.subheader("Donkey Kicks")
        st.write("")
        st.divider()

        st.subheader("Fire Hydrants")
        st.write("")
        st.divider()

        st.subheader("Glute Bridges")
        st.write("")
        st.divider()

        st.subheader("Hip Thrusts")
        st.write("")
        st.divider()

        st.subheader("Lunges")
        st.write("")

        st.subheader("Variation: Reverse Lunges")
        st.write("")

        st.subheader("Variation: Lateral Lunges")
        st.write("")

        st.subheader("Variation: Walking Lunges")
        st.write("")
        st.divider()

        st.subheader("Quadruped Leg Lifts")
        st.write("")
        st.divider()

        st.subheader("Quadruped Hip Extensions")
        st.write("")
        st.divider()

        st.subheader("Side Leg Raises")
        st.write("")
        st.divider()

        st.subheader("Single-Leg Glute Bridges")
        st.write("")
        st.divider()

        st.subheader("Standing Leg Abduction")
        st.write("")
        st.divider()
        
        st.subheader("Standing Kickbacks")
        st.write("")
        st.divider()
        
        st.subheader("Squats")
        with st.expander(":information_source: Read Instructions"):
            st.write(" 1. Stand with your feet wider than your Hips and feet pointed slightly out.")
            st.write(" 2. Begin bendin your knees until parallel to the floor with your back as straight as possible.")
            st.write(" 3. Push back up until you reach standing positions.")
            st.write(" 4. Repeat.")
        with st.expander(":video_camera: Watch Video"):
            st.video('https://www.youtube.com/watch?v=xqvCmoLULNY')
            st.write("Video Source: https://www.youtube.com/watch?v=xqvCmoLULNY")
        
        st.subheader("Variation: Bulgarian Split Squats")
        st.write("")
        
        st.subheader("Variation: Plie Squats")
        st.write("")
        
        st.subheader("Variation: Sumo Squats")
        st.divider()
        
        st.subheader("Wall Sit")
        st.write("")

        st.subheader("Variation: Wall Sit with Leg Lifts")
        st.write("")
        st.divider()
        
    elif selected_subcategory == "Legs":
        st.subheader("Leg Training")
        col1, col2 = st.columns(2)
        with col1:
           st.subheader("Benefits")
           st.write("leg exercises offer benefits like increased muscle strength, better Bone Health, improved cardiovascular health and reduce the risk of chronic diseases")
           
        with col2:
           st.subheader("used Muscles")
           st.image("beinmuskeln.jpg")
           st.write("Image source: https://www.muskelpower.de/beinmuskeln/")
        st.divider()

        st.subheader("Alternating Stance Jumps")
        st.write("")
        st.divider()

        st.subheader("Boxer Shuffle")
        st.write("")
        st.divider()

        st.subheader("Butt Kicks")
        st.write("")
        st.divider()

        st.subheader("Flutter Kicks")
        st.write("")
        st.divider()

        st.subheader("Half Squat Walk")
        st.write("")
        st.divider()

        st.subheader("High Kicks")
        st.write("")
        st.divider()

        st.subheader("Jumping Jack")
        st.write("")
        st.divider()

        st.subheader("Knee Side Leg Lifts")
        st.write("")
        st.divider()

        st.subheader("Lateral Hops")
        st.write("")
        st.divider()

        st.subheader("Lying Leg Circles")
        st.write("")
        st.divider()

        st.subheader("Marching Hip Raises")
        st.write("")
        st.divider()

        st.subheader("Pulsing Side Lying Leg Raises")
        st.write("")
        st.divider()

        st.subheader("Rainbow Leg Lifts")
        st.write("")
        st.divider()

        st.subheader("Side And Cross Crunches")
        st.write("")
        st.divider()

        st.subheader("Side Knee Raises")
        st.write("")
        st.divider()

        st.subheader("Side Lying Bottom Leg Lifts")
        st.write("")
        st.divider()

        st.subheader("Side Lying Leg Raises")
        st.write("")
        st.divider()

        st.subheader("Single Leg V-Ups")
        st.write("")
        st.divider()

        st.subheader("Straight Leg Circles")
        st.write("")
        st.divider()

        st.subheader("Walking High Knees")
        st.write("")
        st.divider()
    
        
    st.sidebar.subheader("Planned Programms")
    second_subcategory = st.sidebar.selectbox("Choose a second subcategory", [" ", "Summerbody", "Get That Booty", "VERY HARD ABS", "Upper Body", "Lower Body"])
   
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

    elif second_subcategory == "Upper Body":
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

    elif second_subcategory == "Lower Body":
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
    third_subcategory = st.sidebar.selectbox("Choose a randomized workout", ["  ", "Arms", "Back", "Core", "Glutes", "Legs"])
    
    if third_subcategory == " ":
        st.subheader(" ")
        st.write(" ")

    
    elif third_subcategory == "Arms":
        st.subheader("Randomized Arm Workout")

        tab1, tab2, tab3 = st.tabs(["Beginner", "Intermediate", "Advanced"])

        with tab1:
           st.header("Beginner Training")
        
        with tab2:
           st.header("Intermediate Training")
        
        with tab3:
           st.header("Advanced Training")
            

    elif third_subcategory == "Back":
        st.subheader("Randomized Back Workout")

        tab1, tab2, tab3 = st.tabs(["Beginner", "Intermediate", "Advanced"])

        with tab1:
           st.header("Beginner Training")
        
        with tab2:
           st.header("Intermediate Training")
        
        with tab3:
           st.header("Advanced Training")

        
    elif third_subcategory == "Core":
        core_fitness_übungen = [
            "Ab Rollouts",
            "Bicycle Crunches",
            "Boat pose",
            "Crunches",
            "Flutter Kicks",
            "Hanging Leg Raises",
            "Jackknife Sit-ups",
            "Leg Raises",
            "Mountain Climbers",
            "Plank for 30 Seconds",
            "Reverse Crunches",
            "Russian Twists",
            "Scissor Kicks",
            "Seated Knee Tucks",
            "Seated Leg Tugs",
            "Side Planks",
            "Sit-ups",
            "Standing Oblique Crunches",
            "Toe Touches",
            "V-ups"
        ]

        
        st.subheader("Randomized Core Workout")

        tab1, tab2, tab3 = st.tabs(["Beginner", "Intermediate", "Advanced"])

        with tab1:
            st.header("Beginner Training")
            st.write("Here are 5 randomized exercises for your core. Do 1-2 sets with each 10 repetitions. Take a break of 60 Seconds in between the exercises.")
            zufällige_übungen_beginner = random.sample(core_fitness_übungen, 5)
            for übung in zufällige_übungen_beginner:
                st.write(übung)

        with tab2:
            st.header("Intermediate Training")
            st.write("Here are 8 randomized exercises for your core. Do 3-4 sets with each 10 repetitions. Take a break of 45 Seconds in between the exercises.")
            zufällige_übungen_intermediate = random.sample(core_fitness_übungen, 8)
            for übung in zufällige_übungen_intermediate:
                st.write(übung)
        
        with tab3:
            st.header("Advanced Training")
            st.write("Here are 11 randomized exercises for your core. Do 4-5 sets with each 10 repetitions. Take a break of 30 Seconds in between the exercises.")
            zufällige_übungen_advanced = random.sample(core_fitness_übungen, 11)
            for übung in zufällige_übungen_advanced:
                st.write(übung)

    elif third_subcategory == "Glutes":
        glutes_fitness_übungen = [
            "Bridge",
            "Clamshells",
            "Donkey Kicks",
            "Donkey Kicks",
            "Fire Hydrants",
            "Glute Bridges",
            "Hip Thrusts",
            "Forward Lunges",
            "Reverse Lunges",
            "Lateral Lunges",
            "Walking Lunges",
            "Quadruped Leg Lifts",
            "Quadruped Hip Extensions",
            "Side Leg Raises",
            "Single-Leg Glute Bridges",
            "Standard Squats",
            "Bulgarian Split Squats",
            "Sumo Squats",
            "Plie Squats",
            "Standing Leg Abduction",
            "Standing Kickbacks",
            "Wall Sit"
        ]


        st.subheader("Randomized Glutes Workout")

        tab1, tab2, tab3 = st.tabs(["Beginner", "Intermediate", "Advanced"])

        with tab1:
            st.header("Beginner Training")
            st.write("Here are 5 randomized exercises for your butt. Do 1-2 sets with each 10 repetitions. Take a break of 60 Seconds in between the exercises.")
            zufällige_übungen_beginner = random.sample(glutes_fitness_übungen, 5)
            for übung in zufällige_übungen_beginner:
                st.write(übung)
        with tab2:
            st.header("Intermediate Training")
            st.write("Here are 8 randomized exercises for your butt. Do 3-4 sets with each 10 repetitions. Take a break of 45 Seconds in between the exercises.")
            zufällige_übungen_intermediate = random.sample(glutes_fitness_übungen, 8)
            for übung in zufällige_übungen_intermediate:
                st.write(übung)

        with tab3:
            st.header("Advanced Training")
            st.write("Here are 11 randomized exercises for your glutes. Do 4-5 sets with each 10 repetitions. Take a break of 30 Seconds in between the exercises.")
            zufällige_übungen_advanced = random.sample(glutes_fitness_übungen, 11)
            for übung in zufällige_übungen_advanced:
                st.write(übung)


    elif third_subcategory == "Legs":
        st.subheader("Randomized Leg Workout")
        legs_fitness_übungen = [
            "Alternating Stance Jumps",
            "Boxer Shuffle",
            "Butt Kicks",
            "Flutter Kicks",
            "Half Squat walk",
            "High Kicks",
            "30 Jumping Jacks",
            "Knee Side Leg Lifts",
            "Lateral Hops",
            "Lying Leg Circles",
            "Marching Hip Raises",
            "Pulsing Side Lying Leg Raises",
            "Rainbow Leg Lifts",
            "Side And Cross Crunches",
            "Side Knee Raises",
            "Side Lying Bottom Leg Lifts",
            "Side Lying Leg Raises",
            "Single Leg V-Ups",
            "Straight Leg Circles",
            "Walking High Knees",
        ]
                
        tab1, tab2, tab3 = st.tabs(["Beginner", "Intermediate", "Advanced"])

        with tab1:
            st.header("Beginner Training")
            st.write("Here are 5 randomized exercises for your legs. Do 1-2 sets with each 10 repetitions. Take a break of 60 Seconds in between the exercises.")
            zufällige_übungen_beginner = random.sample(legs_fitness_übungen, 5)
            for übung in zufällige_übungen_beginner:
                st.write(übung)
        # Show a spinner during a process
         with st.spinner(text='In progress'):
         time.sleep(3)
         st.success('Done')

        # Show and update progress bar
         bar = st.progress(50)
         time.sleep(3)
         bar.progress(100)
        
        with tab2:
            st.header("Intermediate Training")
            st.write("Here are 8 randomized exercises for your legs. Do 3-4 sets with each 10 repetitions. Take a break of 45 Seconds in between the exercises.")
            zufällige_übungen_intermediate = random.sample(legs_fitness_übungen, 8)
            for übung in zufällige_übungen_intermediate:
                st.write(übung)
                
        with tab3:
            st.header("Advanced Training")
            st.write("Here are 11 randomized exercises for your legs. Do 4-5 sets with each 10 repetitions. Take a break of 30 Seconds in between the exercises.")
            zufällige_übungen_advanced = random.sample(legs_fitness_übungen, 11)
            for übung in zufällige_übungen_advanced:
                st.write(übung)

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
