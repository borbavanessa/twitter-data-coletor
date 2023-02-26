# Tutorial: https://towardsdatascience.com/an-extensive-guide-to-collecting-tweets-from-twitter-api-v2-for-academic-research-using-python-3-518fcb71df2a

from services.twitter_api import TwitterApi


def data_coletor():
		twitter_api = TwitterApi()
		
		#Show tweet original
		twitter_api.get_main_tweet()

    #Get comments, replies from original tweet
		twitter_api.get_all_content()

if __name__ == "__main__":
		data_coletor()