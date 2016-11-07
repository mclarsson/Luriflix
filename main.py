
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

		# Which properties to filter
		self.filters = Movie.filters

		# Where to save current state
		self.save_file = 'movies.json'

		self.files = []

		self.load()

	def update(self, files):
		""" Updates list of files. """
		for file in files:
			self.files.append(Movie(file))

	def scan(self, directory):
		files = Scanner.scan(self.suffixes, directory)
		self.update(files)

	def load(self):
		""" Loads files into system """
		files = []
		json = Storage.load_JSON(self.save_file)
		for properties in json:
			self.files.append(Movie(properties))

	def save(self):
		""" Saves current state """
		json = []
		for file in self.files:
			json.append(file.properties)

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
			for identifier in self.filters:
				for query in queries:
					if query in file.attributes[identifier] and file not in filtered:
						filtered.append(file)

		return filtered

if __name__ == "__main__":
	lfx = Luriflix()
	tui = TextUI(lfx)