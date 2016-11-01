
from scanner import Scanner
from cli import CLI

class Luriflix:

	def __init__(self):
		self.scanner = Scanner()
		self.ui = CLI()

if __name__ == "__main__":
	l = Luriflix()