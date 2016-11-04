
""" Main module for application. """

from storage import Storage
from scanner import Scanner
from interface import *
from movie import *

class Luriflix:

	def __init__(self):
		self.suffixes = Movie.suffixes
		self.load_file = 'movies.json'

		self.files = []

		self.load()

		# Initiate UI
		self.ui = TextUI(self)

	def update(self, files):
		""" Updates list of files. """
		files = Scanner.scan(self.suffixes)
		for file in files:
			args = {'File' : file}
			self.files.append(Movie(**args))

	def load(self):
		""" Loads files into system """
		files = []
		json = Storage.load_JSON(self.load_file)
		for file in json:
			self.files.append(Movie(**file))

	def save(self):
		""" Saves current state """
		json = []
		for file in self.files:
			json.append(file.properties)

		Storage.save_as_JSON(json, self.load_file)

if __name__ == "__main__":
	l = Luriflix()