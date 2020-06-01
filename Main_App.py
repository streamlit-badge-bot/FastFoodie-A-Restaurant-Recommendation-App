import streamlit as st
from Pages import Home, bts_eda, Uber, Recommender


st. sidebar.image('Data/App_icon.png',use_column_width=500)
st.sidebar.title("All about the App...")

option = st.sidebar.radio(
    'Navigate through various Features of the App!',
    ('Home.', 'Our List of Restaurants.','Restuarants We Recommend.','Uber & Uber Eats.')
)

if option == 'Home.':
    Home.home()

if option == 'Our List of Restaurants.':
    bts_eda.eda()

if option == 'Restuarants We Recommend.':
    Recommender.eda()

if option == 'Uber & Uber Eats':
    Uber.funct()

st.sidebar.text("")
st.sidebar.title("")
st. sidebar.image('Data/TripAdvisor-logo.png',use_column_width=500)