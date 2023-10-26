import streamlit as st
import pandas as pd
import numpy as np

# Function to recommend the room based on user preferences
def recommend_room(user_temperature_preference, user_noise_preference):
    # Load data for each room from separate CSV files
    rooms = {}
    room_numbers = [1, 2, 3, 4, 5, 6]  # Room numbers or IDs

    for room_number in room_numbers:
        filename = f'Room_{room_number}_Data.csv'  # Replace with your actual file naming convention
        data = pd.read_csv(filename)
        rooms[room_number] = data

    # Calculate distances for each room
    room_distances = {}
    for room_number, data in rooms.items():
        room_distances[room_number] = np.sqrt((data['Temperature (Fahrenheit)'] - user_temperature_preference) ** 2 +
                                            (data['Noise Level (Decibels)'] - user_noise_preference) ** 2)

    # Find the room with the smallest distance (most suitable room)
    best_room_number = min(room_distances, key=lambda k: room_distances[k].iloc[0])
    best_room_data = rooms[best_room_number]

    return best_room_number, best_room_data

# Streamlit UI
st.title("Study Room Recommendation App")
st.sidebar.header("User Preferences")

# Input fields for user preferences
user_temperature_preference = st.sidebar.slider("Preferred Temperature (Fahrenheit)", min_value=65.0, max_value=75.0, value=72.5, step=0.1)
user_noise_preference = st.sidebar.slider("Preferred Noise Level (Decibels)", min_value=35, max_value=60, value=40, step=1)

# Button to trigger the recommendation
if st.sidebar.button("Recommend Room"):
    best_room_number, best_room_data = recommend_room(user_temperature_preference, user_noise_preference)

    # Display the recommendation
    st.subheader("Recommended Room:")
    st.write("Room Number:", best_room_number)
    st.write("Temperature (Fahrenheit):", best_room_data['Temperature (Fahrenheit)'].iloc[0])
    st.write("Noise Level (Decibels):", best_room_data['Noise Level (Decibels)'].iloc[0])
