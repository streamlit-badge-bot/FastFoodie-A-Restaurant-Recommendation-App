import streamlit as st
from Pages import Home, bts_eda, Uber, Recommender
import reload


st. sidebar.image('Data/App_icon.png',use_column_width=500)
st.sidebar.title("All about the App...")

option = st.sidebar.radio(
    'Navigate through various Features of the App!',
    ('Home.', 'Our List of Restaurants.','Restuarants We Recommend.','Book a Cab or Order Food with Uber.')
)

if option == 'Home.':
    Home.home()

if option == 'Our List of Restaurants.':
    bts_eda.eda()

if option == 'Restuarants We Recommend.':
    Recommender.eda()

if option == 'Book a Cab or Order Food with Uber.':
    Uber.funct()
