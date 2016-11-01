
import os

class Scanner:

	def __init__(self):
		pass

	def scan(self, suffixes = [".txt"]):
		for root, dirs, files in os.walk("/"):
			for file in files:
				if any(file.endswith(suffix) for suffix in suffixes):
					print(file)