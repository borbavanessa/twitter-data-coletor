# Twitter Data Coletor

## Goals

Collection of tweets in the excerpt of the report Trans women prisoners face prejudice, abandonment and violence on the program Fantástico on Rede Globo.

The video, shared on the official profile of the Fantástico program, on Twitter, presents the exact moment when the doctor Drauzio Varella hugs Suzy de Oliveira dos Santos and says the phrase: Loneliness, right, my daughter?

The purpose of the research is to analyze the senses triggered from the repercussion of the excerpt of the report that presents the hug and phrase said by Drauzio to Suzy.

The report had wide repercussions and developments during its repercussion, manifestation of meanings around the episode. 

Collect tweets from the program Fantático, Show da Vida, presented by Drausio Varella. Available in [showdavida](https://twitter.com/showdavida/status/1234563236848119810?t=wurW-25yjDl_I5Ee1ajIkQ&s=09).

## Strategy

On March 2, 2020, the official profile of the Fantástico program on Twitter published an excerpt from the report in which the doctor says the phrase “Loneliness, right my daughter?” and hugs Suzy. 

The publication had 964.7 thousand views, 29.5 thousand likes, 3,888 retweets and 2,300 tweets with comments. Of the 2,300 available tweets, 2,035 tweets were collected via the Twitter API in December 2021. 

The difference between the total number of data and the amount collected is due to the following errors reported by the platform: user not found (when the user deletes or inactivates the account) or suspended account (user banned by the platform).

## Observations

- Credits: Source code adapted from the example provided by Andrew Edward, available at [An Extensive Guide to collecting tweets from Twitter API v2 for academic research using Python 3](https://towardsdatascience.com/an-extensive-guide-to-collecting-tweets-from-twitter-api-v2-for-academic-research-using-python-3-518fcb71df2a) for the use case of this master's degree research work.

- Important: to reproduce this code, it is necessary to register as a software developer on the Twitter platform, signing a data confidentiality agreement upon presentation of the reasons for data collection and acceptance by the company Twitter. Approving this registration allows you to receive security credentials to access data using a Twitter API.

## How to run
1. Install Python:
`sudo apt install python3.9`

2. Install package manager Python:
`sudo apt install python3-pip`

3. Install all packages requires by this project:
`pip install --no-cache-dir --upgrade -r requirements.txt`

4. In your computer, it create .env file in root directory with environment variables with Twitter credentials:
```
#### Link to Twitter initial content
LINK_SHOW='YOUR_HTTP_URL_WITH_VIDEO'
TWEET_DV_ID='YOUR_ID_TWITTER_CONTENT'

#### Settings your period for data collect
INI_DATE_DATA_COLLECT='2020-03-02T00:00:00.000Z'
END_DATE_DATA_COLLECT='2020-03-30T23:59:00.000Z'

#### Twitter Credentials
EMAIL='YOUR_EMAIL_REGISTER_IN_TWITTER'
PASSWD_EMAIL='YOUR_PASSWORD_REGISTER_IN_TWITTER'


### Twitter App Name
APP_NAME='YOUR APP NAME REGISTER IN TWITTER'
API_KEY='YOUR KEY REGISTER IN TWITTER'
API_KEY_SECRET='YOUR SECRET KEY REGISTER IN TWITTER'
BEARER_TOKEN='YOR BEARER TOKEN REGISTER IN TWITTER'


### Directory save files objects
PATH_FILES=YOUR_DIRECTORY_TO_SAVE_DATA_COLECTED_IN_CSV_FILE_FORMAT

```

5. Run application
`python3.9 main.py`
