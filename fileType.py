
""" Module with different file types. """

from abc import ABCMeta, abstractmethod

class FileType:
	__metaclass__ = ABCMeta

	@abstractmethod
	def suffixes(self): 
		""" Which suffixes mathes the file type.

		Returns:
			list: Suffixes.
		"""
		return []

class Movie(FileType):

	def suffixes(self):
		return ['_movie.txt', '.mkv', '.mp4', '.avi'] # _movie.txt for development