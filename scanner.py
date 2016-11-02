
import os

""" This module is responsible for scanning the computer. """

origin_dir = os.path.dirname(os.path.abspath(__file__)) # Start the scan where this file is
""" str: where to start the scan """

class Scanner:

	@staticmethod
	def scan(suffixes):
		""" Traverses the entire system and returns matching files.
		Args:
			suffixes (list): What suffixes to match.

		Returns:
			list: Matching files.
		"""

		result = []

		for root, dirs, files in os.walk(origin_dir):
			for file in files:
				if any(file.endswith(suffix) and file != suffix for suffix in suffixes):
					print(os.stat(root).st_size)
					result.append(file)

		return result