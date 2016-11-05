
""" Module for saving and loading """ 

import json

class Storage:

	@staticmethod
	def save_as_JSON(data, file):
		""" Writes data to file """
		with open(file, 'w') as outfile:
			json.dump(data, outfile)

	@staticmethod
	def load_JSON(file):
		""" Load data from file.
		Returns:
			list: Loaded data.
		"""
		with open(file) as data_file:
			return json.load(data_file)