# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Measuring Risk Tolerance - Crypto or Stocks?

---

**Disclaimer:** I am not a financial advisor, and I am not offering or providing any financial advice to anyone. This is simply a data science project that analyzes keywords unique to the posts in the r/wallstreetbets and r/SatoshiStreetBets subreddits to predict whether an individual identifies more closely with stocks or cryptocurrency.

---

### Overview

This project will cover the following:
- Problem Statement
- Data Dictionary
- Executive Summary
- Conclusion
- Data Sources

---

### Problem Statement

In the past year, retail investors have flocked to the stock and cryptocurrency markets in the hopes of netting a handsome return on their investments. While they were present long before the COVID-19 pandemic, their participation and impact on the markets have grown in recent months. From playing an active role in short-squeezing GME's stock to creating hype around dogecoin, retail investors have engaged in numerous types of trading activity with a wide-ranging level of risk.

Investments and trades made in the stock and crypto markets both assume some level of risk. Given the wildly volatile nature of cryptocurrency, I consider cryptocurrencies to have a higher risk profile than stocks for the purpose of this project.

The r/wallstreetbets subreddit is a community of 9.4 million members who seek to make money by investing and trading in the stock market. The r/SatoshiStreetBets subreddit is the cryptocurrency equivalent of r/wallstreetbets with a smaller community of 347K members. While r/wallstreetbets mostly focuses on the stock market and r/SatoshiStreetBets mainly engages with the cryptocurrency market, conversations in both subreddits do occasionally overlap with each other.

For this project, my goal is two-fold: (1) I aim to build a classification model that can predict if a post came from r/wallstreetbets or r/SatoshiStreetBets with a minimum accuracy of 50% and an ideal accuracy of 80% or higher and (2) I plan to identify words unique to each subreddit so that I can utilize these words to determine if an individual retail investor might have a risk profile more tolerant to stocks or cryptocurrency.

As a data scientist consulting Reddit to provide cautionary warnings on its r/wallstreetbets and r/SatoshiStreetBets subreddits, I hope to determine an investment type (i.e. stock or crypto) that may be more suitable to the individual retail investor based on the keywords with which they identify.

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

### Executive Summary

The goals of this project were two-fold: (1) the first was to process natural language scraped from Pushshift's web API in order to construct a classification model that could predict which of two subreddits a post came from with at least an 80% accuracy score and (2) the second was to determine an investment type (i.e. stock or crypto) that may be more suitable to the individual retail investor based on the keywords with which the individual identifies. Through the iterative process of model tuning, I was able to build a logistic regression model with the desirable accuracy and found the words with the most predictive power for classification. In addition, I performed sentiment analysis to understand the range of positive and negative emotions that are tied to the words used in each subreddit. Based on my findings, it appears that there are words unique to members of r/wallstreetbets and r/SatoshiStreetBets that may inform the individual to side with a particular investment type (i.e. stock or crypto).

---

### Conclusion

In conclusion, the set of words below will provide direction in determining whether r/wallstreetbets or r/SatoshiStreetBets is more suitable for the individual retail investor.

The 10 most commonly seen words in r/wallstreetbets are:
- gme
- amc
- stock
- moon
- like
- apes
- just
- wsb
- buy
- short

The 10 most commonly seen words in r/SatoshiStreetBets are:
- ada
- crypto
- coin
- buy
- bitcoin
- moon
- btc
- cardano
- moonshot
- just

Out of the top 100 most common words seen in r/wallstreetbets and r/SatoshiStreetBets, there are 59 words that are unique to each.

For r/wallstreetbets, the unique words include:
- 'account', 'amc', 'ape', 'apes', 'app', 'bruce', 'calls', 'cciv', 'dd', 'diamond', 'does', 'earnings', 'fellow', 'funds', 'game', 'gamestop', 'getting', 'gme', 'gonna', 'hands', 'hedge', 'holding', 'invest', 'lucid', 'march', 'melvin', 'meme', 'options', 'past', 'retarded', 'retards', 'robinhood', 'say', 'says', 'sec', 'sell', 'share', 'shares', 'shit', 'sign', 'sos', 'squeeze', 'stimulus', 'stock', 'stocks', 'stonk', 'stop', 'street', 'strong', 'tendies', 'tesla', 'video', 'wall', 'wallstreetbets', 'want', 'weekend', 'worth', 'wsb', 'yesterday'

For r/SatoshiStreetBets, the unique words include:
- '10', '100', 'ada', 'bitcoin', 'blockchain', 'bnb', 'bsc', 'btc', 'btt', 'cap', 'cardano', 'coin', 'coins', 'crash', 'cro', 'crypto', 'days', 'did', 'dip', 'doge', 'dogecoin', 'elon', 'eth', 'exchange', 'free', 'gains', 'great', 'high', 'join', 'kucoin', 'listed', 'look', 'looking', 'low', 'moonshot', 'musk', 'nano', 'network', 'news', 'nft', 'pi', 'pivx', 'potential', 'project', 'pump', 'ready', 'staking', 'start', 'stellar', 'student', 'supply', 'term', 'thoughts', 'token', 'usd', 'value', 'vet', 'xlm', 'xrp'

For each individual, I would recommend reviewing the sets of words above to understand risk tolerance and the investment type (i.e. stock or crypto) that may be a better fit.

**Note:** The logistic regression model I used for the predictions provides 690 words with the highest predictive power in determining the classification of a post. For practical purposes, I will not list these 690 words.

---

### Data Sources

The data was collected using Pushshift's API. The links to the data have been provided below.

- [r/wallstreetbets](https://api.pushshift.io/reddit/search/submission?subreddit=wallstreetbets): This is the Pushshift web API for the r/wallstreetbets subreddit.
- [r/SatoshiStreetBets](https://api.pushshift.io/reddit/search/submission?subreddit=SatoshiStreetBets): This is the Pushshift web API for the r/SatoshiStreetBets subreddit.

---
