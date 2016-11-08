
""" This module is responsible for scanning the computer. """

import os

kilobyte = 1024.0
""" int: How many bytes to a kilobyte """

megabyte = 1048576.0
""" int: How many bytes to a megabyte """

gigabyte = 1073741824.0
""" int: How many bytes to a gigabyte """

terabyte = 1099511627776.0
""" int: How many bytes to a terabyte """


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

					# Size is in gigabyte
					GB = os.stat(root + "\\" + file).st_size / gigabyte

					result.append({
						'Source': root,
						'File': file, 
						'Size': GB
					})

		return result