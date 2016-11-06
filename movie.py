
""" Module with different file types. """

class Movie:
	suffixes = ['.mkv', '.mp4']
	property_titles = ['Source', 'File', 'Title', 'Size']

	def __init__(self, properties):
		self.properties = properties