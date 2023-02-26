import requests
import json
import time
from decouple import config
from services.csv_file import CsvFile


class TwitterApi(object):
		
		def __init__(self, _verbose=True):
				self.verbose = _verbose
				self.bearer_token = config('BEARER_TOKEN')
				self.headers = self.__create_headers()
		
		def bearer_oauth(self, r):
				r.headers["Authorization"] = f"Bearer {self.bearer_token}"
				r.headers["User-Agent"] = "v2TweetLookupPython"
				
				return r
		
		def get_main_tweet(self):
				url = self.__build_url_main_tweet()
				try:
						response = requests.request("GET", url, auth=self.bearer_oauth)
						if response.status_code != 200:
								self.__debug("Request returned an error: {} {}".format(response.status_code, response.text))
				
						print(json.dumps(response.json(), indent=4, sort_keys=True))
				except Exception as e:
						print("Error to get main Tweet. Detail: %s", str(e))
						
		def get_all_content(self):
				keyword = "conversation_id:{}".format(config('TWEET_DV_ID'))
				ini_date = config('INI_DATE_DATA_COLLECT')
				end_date = config('END_DATE_DATA_COLLECT')
				
				# The `max_results` query parameter would be between 10 and 500
				max_results = 500
				
				# Total number of tweets we collected from the loop
				total_tweets = 0
				
				## Create file headers
				file_public_metrics = CsvFile()
				
				# Inputs
				flag = True
				next_token = None
				
				# Check if flag is true
				while flag:
						self.__debug("-------------------")
						self.__debug("Token: {}".format(next_token))
						search_url, query_params = self.__build_url('all', keyword, ini_date, end_date, max_results)
						json_response = self.__search(search_url, query_params, next_token)
						
						if len(json_response) > 0:
								result_count = json_response['meta']['result_count']
								
								if 'next_token' in json_response['meta']:
										# Save the token to use for next call
										next_token = json_response['meta']['next_token']
										self.__debug("Next Token: {}".format(next_token))
										if result_count is not None and result_count > 0 and next_token is not None:
												file_public_metrics.append_data_info(json_response)
												total_tweets += result_count
												self.__debug("Total # of Tweets added: {}".format(total_tweets))
												self.__debug("-------------------")
												time.sleep(5)
								# If no next token exists
								else:
										if result_count is not None and result_count > 0:
												self.__debug("-------------------")
												file_public_metrics.append_data_info(json_response)
												total_tweets += result_count
												self.__debug("Total # of Tweets added: {}".format(total_tweets))
												self.__debug("-------------------")
												time.sleep(5)
										
										# Since this is the final request, turn flag to false to move to the next time period.
										flag = False
										next_token = None
								time.sleep(5)
				self.__debug("Total number of results: {}".format(total_tweets))
		
		def __build_url(self, end_point, keyword, start_date, end_date, max_results):
				search_url = "https://api.twitter.com/2/tweets/search/" + str(end_point)
				
				# change params based on the endpoint you are using
				query_params = {'query': keyword,
												'start_time': start_date,
												'end_time': end_date,
												'max_results': max_results,
												'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
												'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,'
																				'public_metrics,referenced_tweets,reply_settings,source',
												'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
												# 'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
												'next_token': {}}
				
				return search_url, query_params
		
		def __search(self, search_url, query_params, next_token):
				ret = {}
				try:
						query_params['next_token'] = next_token  # params object received from create_url function
						
						response = requests.request("GET", search_url, headers=self.headers, params=query_params)
						
						if response.status_code != 200:
								raise Exception(response.status_code, response.text)
						
						ret = response.json()
				except Exception as e:
						print("Failed request for URL %s. Error Detail: %s" % (str(search_url), str(e)))
				
				return ret
		
		def __create_headers(self):
				headers = {"Authorization": "Bearer {}".format(self.bearer_token), "User-Agent": "v2TweetLookupPython"}
				return headers

		def __build_url_main_tweet(self):
				tweet_fields = "tweet.fields=id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang," \
											 "public_metrics,referenced_tweets,reply_settings,source"
				user_fields = "user.fields=id,name,username,created_at,description,public_metrics,verified"

				ids = "ids={}".format(config('TWEET_DV_ID'))

				return "https://api.twitter.com/2/tweets?{}&{}&{}".format(ids, tweet_fields, user_fields)
		
		def __debug(self, text):
				if self.verbose:
					print(text)
