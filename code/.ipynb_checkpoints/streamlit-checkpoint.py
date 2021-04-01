import pickle
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
page_icon='BOOK',
initial_sidebar_state='expanded'
)

st.title('Crypto or Stocks?')

st.write('Use the sidebar to select a page to view.')

page = st.sidebar.selectbox(
'Page',
('About', 'EDA', 'Make a prediction')
)

if page == 'About':
    st.subheader('About this project')
    st.write('''
    This is a Streamlit app that hosts my r/wallstreetbets vs. r/SatoshiStreetBets model.

    The best model I found was Logistic Regression.

    You can get in touch with me on these websites...

    '''
    )

elif page == 'EDA':
    # header
    st.subheader('Exploratory Data Analysis')
    st.write('''The model is trained on subreddit posts.

    Below you can find...

    '''
    )

elif page == 'Make a prediction':
    st.subheader('Which subreddit suits you better?')

    st.write('''
    Enter some text to make a prediction!

    The text might visually cut off, but you can write up to 1,000 characters.
    '''
    )

# Pickle path
with open('../datasets/production_model.pkl', 'rb') as pickle_in:
    model = pickle.load(pickle_in)

your_text = st.text_input(
label='Please enter some text:',
value='bitcoin keeps mooning! do you think elon will pump dogecoin or should I keep buying ada?',
max_chars=1000
)
predicted_subreddit = model.predict([your_text])[0]

st.subheader('Results:')
st.write(f'You identify more closely with {predicted_subreddit.title()}')
