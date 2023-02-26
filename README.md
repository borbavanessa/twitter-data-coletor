# Twitter Data Coletor

## Goals:

- Collect tweets from the program Fantático, Show da Vida, presented by Drausio Varella. Available in [showdavida](https://twitter.com/showdavida/status/1234563236848119810?t=wurW-25yjDl_I5Ee1ajIkQ&s=09)

- Analyze the different feelings and meanings around the hashtag that occurred in the episode.

- Strategy: collect all comments related to the publication of the article in its entirety on the social network Twitter. Total tweets analyzed: x in the period from x to x.

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
