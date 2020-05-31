import streamlit as st
from bokeh.models.widgets import Div

def funct():
    st.title('Book an Uber or Order from Uber Eats...')
    st.image('Data/Uber.png',use_column_width=500)
    if st.button('Book an Uber'):
        js = "window.open('https://www.uber.com/')"  # New tab or window
        js = "window.location.href = 'https://www.uber.com/'"  # Current tab
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

    st.image('Data/Uber_Eats.png', use_column_width=500)
    if st.button('Order from Uber Eats'):
        js = "window.open('https://www.ubereats.com/')"  # New tab or window
        js = "window.location.href = 'https://www.ubereats.com/'"  # Current tab
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)


