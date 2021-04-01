import pandas as pd
import pickle
import streamlit as st
from PIL import Image


st.set_page_config(
# page_icon='NONE',
initial_sidebar_state='expanded'
)

st.title('Measuring Risk Tolerance: Crypto or Stocks?')

st.write('**Disclaimer:** I am not a financial advisor. I am in no way providing any financial advice to anyone in any shape or form. This app should be used solely for personal amusement.')

st.write('Use the sidebar to select a page to view.')

page = st.sidebar.selectbox(
'Page',
('About', 'Visualize the data', 'Make a prediction')
)

if page == 'About':
    st.subheader('About this project')
    st.write('''
    This is a Streamlit app that showcases my logistic regression model. The model utilizes natural language processing on two subreddits to predict if a post came from r/wallstreetbets or r/SatoshiStreetBets. The predictions from the model can be used to explore risk tolerance in individuals by identifying words unique to each subreddit. Individuals who write text that resembles the posts from r/wallstreetbets may be more interested in stocks, whereas those who write text that resembles the posts from r/SatoshiStreetBets may be more interested in cryptocurrency.

    You can get in touch with me on these websites:
    - LinkedIn: https://www.linkedin.com/in/seung-woo-choi/
    - Portfolio: https://choiseun.github.io/

    '''
    )    
    
elif page == 'Visualize the data':
    # header
    st.subheader('Visualize the data')
    st.write('''Let's look at some colorful visuals.

    Below you can find...

    '''
    )
    
    visual_1 = Image.open('./images/wsb_word_cloud.png')
    st.image(visual_1, caption='Words Unique to r/wallstreetbets')
    st.write('''
    
    ''')
             
    visual_2 = Image.open('./images/ssb_word_cloud.png')
    st.image(visual_2, caption='Words Unique to r/SatoshiStreetBets')
    st.write('''
    
    ''')
    
    visual_3 = Image.open('./images/shared_word_cloud.png')
    st.image(visual_3, caption='Words Common to Both Subreddits')
    st.write('''
    
    ''')
    
elif page == 'Make a prediction':
    st.subheader('Stocks or Cryptocurrency? Which type of asset are you more interested in?')

    st.write('''
    Enter some text to make a prediction! The model is trained on subreddit posts.

    The text might visually cut off, but you can write up to 500 characters.
    '''
    )
    
    st.write('''
             
             
             ''')
    
    # Pickle path
    with open('./datasets/production_model.pkl', 'rb') as pickle_in:
        model = pickle.load(pickle_in)

    # Text input
    your_text = st.text_input(
    label='Please enter some text:',
    value='bitcoin keeps mooning! do you think elon will pump dogecoin or should I keep buying ada?',
    max_chars=500
    )

    # Prediction
    predicted_subreddit = model.predict([your_text])[0]

    # Labels
    my_label = 'None'
    my_asset = 'None'
    if predicted_subreddit == 0:
        my_label = 'r/SatoshiStreetBets'
        my_asset = 'cryptocurrency'
    elif predicted_subreddit == 1:
        my_label = 'r/wallstreetbets'
        my_asset = 'stocks'

    # Results
    st.write('''
    
    ''')
    st.subheader('Results:')
    st.write(f'The input resembles text you may find on **{my_label}**. You may be more interested in **{my_asset}**.')
    
# Referenced: https://git.generalassemb.ly/DSIR-Lancelot/streamlit_lesson/blob/master/solution-code/app.py