import streamlit as st
import webbrowser

def funct():
    st.title('Book an Uber or Order from Uber Eats...')
    st.image('Data/Uber.png',use_column_width=500)
    if st.button('Book an Uber'):
        webbrowser.open('https://www.uber.com/')
    st.image('Data/Uber_Eats.png', use_column_width=500)
    if st.button('Order from Uber Eats'):
        webbrowser.open('https://www.ubereats.com/')





