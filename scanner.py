
""" This module is responsible for scanning the computer. """

import os

origin_dir = os.path.dirname(os.path.abspath(__file__)) # Start the scan where this file is
""" str: where to start the scan """

kilobyte = 1024.0
megabyte = 1048576.0
gigabyte = 1073741824.0
terabyte = 1099511627776.0

class Scanner:

	@staticmethod
	def scan(suffixes, directory):
		""" Traverses the entire system and returns matching files.
		Args:
			suffixes (list): What suffixes to match.

		Returns:
			list: Matching files.
		"""
		# TODO: scannar inte allt under development

		result = []
		for root, dirs, files in os.walk(directory):
			for file in files:
				if any(file.endswith(suffix) and file != suffix for suffix in suffixes):
					GB = os.stat(root + "\\" + file).st_size / gigabyte

					result.append({
						'Source': root,
						'File': file, 
						'Size': GB
					})

		return result