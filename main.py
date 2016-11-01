
from scanner import Scanner
from cli import CLI
from fileType import *

class Luriflix:

	def __init__(self):
		self.scanner = Scanner()
		self.file_type = Movie()

		# Initiate UI
		self.ui = CLI(self)

	def scan(self, suffixes = []):
		if len(suffixes) == 0:
			suffixes = self.file_type.suffixes()
			
		return self.scanner.scan(suffixes)

if __name__ == "__main__":
	l = Luriflix()