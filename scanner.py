
import os

class Scanner:

	def __init__(self):
		pass

	def scan(self, suffixes):
		result = []
		for root, dirs, files in os.walk("/"):
			for file in files:
				if any(file.endswith(suffix) for suffix in suffixes):
					result.append(file)
		return result