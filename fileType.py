
from abc import ABCMeta, abstractmethod

class FileType:
	__metaclass__ = ABCMeta

	@abstractmethod
	def suffixes(self): 
		# Which suffixes describes the type.
		return []

class Movie(FileType):

	def suffixes(self):
		return ['_movie.txt', '.mkv', '.mp4', '.avi'] # _movie.txt for development