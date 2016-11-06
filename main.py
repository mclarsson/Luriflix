
""" Main module for application. """

import os

from storage import Storage
from scanner import Scanner
from interface import *
from movie import *

class Luriflix:

	def __init__(self):
		self.suffixes = Movie.suffixes
		self.property_titles = Movie.property_titles
		self.save_file = 'movies.json'

		self.files = []

		self.load()

		# Initiate UI
		self.ui = TextUI(self)

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


if __name__ == "__main__":
	l = Luriflix()