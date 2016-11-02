
""" Main module for application. """

from scanner import Scanner
from interface import *
from movie import *

class Luriflix:

	def __init__(self):
		self.scanner = Scanner()
		self.file_type = Movie()

		self.files = []

		self.update

		# Initiate UI
		self.ui = TextUI(self)

	def update(self):
		""" Updates list of files. """

		suffixes = self.file_type.suffixes
		self.files = self.scanner.scan(suffixes)

if __name__ == "__main__":
	l = Luriflix()