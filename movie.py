
""" Module with different file types. """

class Movie:
	suffixes = ['.mkv', '.mp4']
	filters = ['File', 'Title']
	titles = ['File', 'Title', 'Size']

	def __init__(self, attributes):
		self.attributes = attributes