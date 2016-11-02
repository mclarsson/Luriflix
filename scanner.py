
import os

""" This module is responsible for scanning the computer. """

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

		for root, dirs, files in os.walk("/"):
			for file in files:
				if any(file.endswith(suffix) and file != suffix for suffix in suffixes):
					result.append(file)

		return result