
""" Main module for application. """

from scanner import Scanner
from interface import *
from movie import *

class Luriflix:

	def __init__(self):
		self.suffixes = Movie.suffixes

		self.files = []

		self.update()

		# Initiate UI
		self.ui = TextUI(self)

	def update(self):
		""" Updates list of files. """
		files = Scanner.scan(self.suffixes)
		for file in files:
			self.files.append(Movie(file))



if __name__ == "__main__":
	l = Luriflix()