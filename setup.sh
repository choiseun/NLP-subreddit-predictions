# Credits to Alec Edgecliffe-Johnson!
mkdir -p ~/.streamlit
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml

# Referenced for Heroku: https://towardsdatascience.com/from-streamlit-to-heroku-62a655b7319
# Referenced for Heroku: https://towardsdatascience.com/nlp-and-streamlit-on-heroku-5ebb56d6a57f