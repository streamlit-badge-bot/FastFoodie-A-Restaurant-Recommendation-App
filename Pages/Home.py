import streamlit as st
from PIL import Image

def home():
    image = Image.open('Data/Food.png')
    st.image(image, use_column_width=True)
    st.success("The app to get you to the closest and the most highly rated places to eat :yum:because guys, hunger is also an emergency! :ambulance: ")
    st.markdown("- Based on data from TripAdvisor, the app covers restaurants form 20 cities across New York, New Jersey, California, Texas and Washington to recommend the 10 most highly rated restaurants in each state. ")
