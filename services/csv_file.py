import csv
from dateutil.parser import parse
from decouple import config


class CsvFile(object):
		USER_FIELDS = ['id', 'name', 'username', 'description']
		DATA_FIELDS = ['in_reply_to_user_id', 'conversation_id', 'source', 'author_id', 'id', 'text',
									 'public_metrics.retweet_count', 'public_metrics.reply_count', 'public_metrics.like_count',
									 'public_metrics.quote_count', 'created_at', 'referenced_tweets.type', 'referenced_tweets.id',
									 'reply_settings']
		
		def __init__(self):
				self.path = config('PATH_FILES')
				self.file_data_info = 'tweets.csv'
				self.file_user_info = 'user_tweets.csv'
				self.file_errors = 'errors_coletor.txt'
				
				self.headers()
				
		def headers(self):
				self.header_data_info()
				self.header_user_info()
		
		def header_data_info(self):
				self.__header_file(self.file_data_info, fields_list=self.DATA_FIELDS)
		
		def header_user_info(self):
				self.__header_file(self.file_user_info, fields_list=self.USER_FIELDS)

		def append_data_info(self, json_response):
				self.__get_data_info(json_response['data'])
				self.__get_user_info(json_response['includes']['users'])
				self.__get_errors(json_response['errors'])


		def __get_data_info(self, info_lst):
				try:
						# A counter variable
						counter = 0
						
						# Open OR create the target CSV file
						csvFile = open(self.path + self.file_data_info, "a", newline="", encoding='utf-8')
						csvWriter = csv.writer(csvFile)
						
						for info in info_lst:
								field_values = []
								for field in self.DATA_FIELDS:
												if '.' in field:
														sub_fields = field.split('.')
														if self.__field_exist(sub_fields[0], info):
																if 'referenced_tweets' in field:
																		field_values.append(info[sub_fields[0]][0][sub_fields[1]] if sub_fields[1] in info[sub_fields[0]][0] else 'not_info')
																else:
																		field_values.append(info[sub_fields[0]][sub_fields[1]] if sub_fields[1] in info[sub_fields[0]] else 'not_info')
												elif self.__field_exist(field, info):
														field_values.append(info[field] if field in info else '')
								
								csvWriter.writerow(field_values)
								counter += 1
						
						# When done, close the CSV file
						csvFile.close()
						
						# Print the number of tweets for this iteration
						print("# of Tweets added from this response['data']: %s", str(counter))
				except Exception as e:
						print("[__get_data_info] Error: %s" % str(e))
		
		def __get_user_info(self, info_lst):
				try:
						# A counter variable
						counter = 0
						
						# Open OR create the target CSV file
						csvFile = open(self.path + self.file_user_info, "a", newline="", encoding='utf-8')
						csvWriter = csv.writer(csvFile)
						
						for info in info_lst:
								field_values = []
								for field in self.USER_FIELDS:
										if field in info:
												field_values.append(info[field] if field in info else '')
								
								csvWriter.writerow(field_values)
								counter += 1
						
						# When done, close the CSV file
						csvFile.close()
						
						# Print the number of tweets for this iteration
						print("# of Tweets added from this response['user_infor']: %s", str(counter))
				except Exception as e:
						print("[__get_user_info] Error: %s" % str(e))
		
		def __get_errors(self, info):
				try:
						with open(self.path + self.file_errors, 'a') as f:
								for error_info in info:
										f.write(str(error_info))
				except Exception as e:
						print("[__get_user_info] Error: %s" % str(e))
		
		def __header_file(self, filename, fields_list):
				file = open(self.path + filename, "a", newline="", encoding='utf-8')
				file_writer = csv.writer(file)
				file_writer.writerow(fields_list)
				file.close()
				
		@staticmethod
		def __field_exist(field, info):
				return field in info
