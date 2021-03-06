
""" Main module for application. """

import os

from storage import Storage
from scanner import Scanner
from interface import *
from movie import *

class Luriflix:

	def __init__(self):
		# Which file endings will match when scanning
		self.suffixes = Movie.suffixes

		# Titles that show up when showing list of files
		self.titles = Movie.titles

		# Which attributes to filter
		self.filters = Movie.filters

		# Where to save current state
		self.save_file = 'movies.json'

		self.files = []

		# Load files from save_file
		self.load()

	def update(self, files):
		""" Updates list of files. """
		for file in files:
			self.files.append(Movie(file))

	def scan(self, directory):
		""" Scans directory for new files """
		files = Scanner.scan(self.suffixes, directory)
		self.update(files)

	def load(self):
		""" Loads files into system """
		files = []
		json = Storage.load_JSON(self.save_file)
		for attributes in json:
			self.files.append(Movie(attributes))

	def save(self):
		""" Saves current state """
		json = []
		for file in self.files:
			json.append(file.attributes)

		Storage.save_as_JSON(json, self.save_file)

	def run(self, file):
		""" Starts file """
		os.startfile(file)

	def filter(self, queries):
		""" Filters the list of files.
		Args:
			queries (list): What to match agains
		Returns:
			list: Filtered list.
		"""
		filtered = []

		for file in self.files:
			for attr in self.filters:
				for query in queries:
					if attr in file.attributes and query.lower() in file.attributes[attr].lower() and file not in filtered:
						filtered.append(file)

		return filtered

if __name__ == "__main__":
	lfx = Luriflix()
	gui = GUI(lfx)