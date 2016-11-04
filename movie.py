
""" Module with different file types. """

class Movie:
	suffixes = ['.mkv', '.mp4']
	property_titles = ['File', 'Title'] # Titles for information display

	def __init__(self, name):
		self.name = name
		self.title = name.replace(".mp4", "").replace("_", " ")
		self.properties = [self.name, self.title]