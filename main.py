
""" Main module for application. """

from scanner import Scanner
from interface import *
from fileType import *

class Luriflix:

	def __init__(self):
		self.scanner = Scanner()
		self.file_type = Movie()

		# Initiate UI
		self.ui = TextUI(self)

	def scan(self, suffixes = []):
		""" Calls to scan for specific files.
		Args:
			suffixes (list): What suffixes to match.

		Returns:
			list: Matching files.
		"""

		# Use the filetypes suffixes if none were sent as parameter
		if len(suffixes) == 0:
			suffixes = self.file_type.suffixes()

		return self.scanner.scan(suffixes)

if __name__ == "__main__":
	l = Luriflix()