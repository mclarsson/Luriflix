
""" Module with different file types. """

class Movie:
	suffixes = ['.mkv', '.mp4']
	property_titles = ['File', 'Title'] # Titles for information display



	def __init__(self, **properties):
		self.__dict__.update(properties)

		self.properties = properties