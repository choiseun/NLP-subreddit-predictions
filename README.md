## Predicting the Subreddit of a Post Using NLP

**Disclaimer:** I am not a financial advisor. I am in no way providing any financial advice to anyone in any shape or form. This repository and its contents should be viewed simply as a data science project and nothing more.

---

### Technology & Skills

**Technology:** Streamlit, Heroku

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

**Python Libraries:** NLTK, requests, time, pandas, numpy, matplotlib, seaborn, scikit-learn, pickle, streamlit, PIL

**Technical Skills:** Binary classification, data collection, scraping web API, data cleaning, EDA, data visualization, machine learning, bias-variance tradeoff, sentiment analysis, natural language processing (NLP), count vectorizer, TF-IDF vectorizer, pre-processing data, modeling, confusion matrix, misclassification, precision, recall, f1-score, ROC AUC, pipeline, gridsearch, word clouds, pickling

**Models:** Logistic regression, decision tree classifier, bagging classifier, multinomial naive bayes, AdaBoost classifier, random forest classifier, support vector classifier

---

### Streamlit App

Check out my Streamlit app hosted on [Heroku](https://risk-tolerance.herokuapp.com/)!

---

### Overview

This project will cover the following:
- Problem Statement
- Executive Summary
- Conclusion
- Data Sources
- Data Dictionary

---

### Problem Statement

In the past year, retail investors have flocked to the stock and cryptocurrency markets in the hopes of netting a handsome return on their investments. While they were present long before the COVID-19 pandemic, their participation and impact on the markets have grown in recent months. From playing an active role in short-squeezing GME's stock to creating hype around dogecoin, retail investors have engaged in numerous types of trading activity with a wide-ranging level of risk.

Investments and trades made in the stock and crypto markets both assume some level of risk. Given the wildly volatile nature of cryptocurrency, I consider cryptocurrencies to have a higher risk profile than stocks for the purpose of this project.

The r/wallstreetbets subreddit is a community of 9.4 million members who seek to make money by investing and trading in the stock market. The r/SatoshiStreetBets subreddit is the cryptocurrency equivalent of r/wallstreetbets with a smaller community of 347K members. While r/wallstreetbets mostly focuses on the stock market and r/SatoshiStreetBets mainly engages with the cryptocurrency market, conversations in both subreddits do occasionally overlap with each other.

For this project, my goal is two-fold: (1) I aim to build a classification model that can predict if a post came from r/wallstreetbets or r/SatoshiStreetBets with a minimum accuracy of 50% and an ideal accuracy of 80% or higher and (2) I plan to identify words unique to each subreddit.

As a data scientist consulting Reddit to provide cautionary warnings on its r/wallstreetbets and r/SatoshiStreetBets subreddits, I hope to determine the keywords unique to each subreddit.

---

### Executive Summary

The goals of this project were two-fold: (1) the first was to process natural language scraped from Pushshift's web API in order to construct a classification model that could predict which of two subreddits a post came from with at least an 80% accuracy score and (2) the second was to determine the keywords that differentiate each subreddit. Through the iterative process of model tuning, I was able to build a logistic regression model with the desirable accuracy and found the words with the most predictive power for classification. In addition, I performed sentiment analysis to understand the range of positive and negative emotions that are tied to the words used in each subreddit. Based on my findings, it appears that there are words unique to r/wallstreetbets and r/SatoshiStreetBets that members prefer to use.

---

### Conclusion

In conclusion, the set of words below will provide direction in determining whether a post came from r/wallstreetbets or r/SatoshiStreetBets.

The 10 most commonly seen words in r/wallstreetbets are:
- gme
- amc
- moon
- stock
- apes
- buy
- just
- like
- wsb
- hold

The 10 most commonly seen words in r/SatoshiStreetBets are:
- ada
- crypto
- coin
- buy
- moon
- bitcoin
- cardano
- btc
- just
- doge

Out of the top 100 most common words seen in r/wallstreetbets and r/SatoshiStreetBets, there are 59 words that are unique to each.

For r/wallstreetbets, the unique words include:

![](https://github.com/choiseun/risk-tolerance/blob/master/images/wsb_word_cloud.png)

For r/SatoshiStreetBets, the unique words include:

![](https://github.com/choiseun/risk-tolerance/blob/master/images/ssb_word_cloud.png)

**Note:** The logistic regression model I used for the predictions provides hundreds of words with the highest predictive power in determining the classification of a post. For practical purposes, I will not list all of these words.

---

### Data Sources

The data was collected using Pushshift's API. The links to the data have been provided below.

- [r/wallstreetbets](https://api.pushshift.io/reddit/search/submission?subreddit=wallstreetbets): This is the Pushshift web API for the r/wallstreetbets subreddit.
- [r/SatoshiStreetBets](https://api.pushshift.io/reddit/search/submission?subreddit=SatoshiStreetBets): This is the Pushshift web API for the r/SatoshiStreetBets subreddit.

---

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|subreddit|object|cleaned_posts|The name of the subreddit|
|title|object|cleaned_posts|The contents of the post|
|post_char_length|int|cleaned_posts|The character length of the post|
|post_word_count|int|cleaned_posts|The word count of the post|
|sentiment_compound|float|cleaned_posts|The compound score from sentiment analysis|
|sentiment_negative|float|cleaned_posts|The negativity score from sentiment analysis|
|sentiment_neutral|float|cleaned_posts|The neutrality score from sentiment analysis|
|sentiment_positive|float|cleaned_posts|The positivity score from sentiment analysis|

---
