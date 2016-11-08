
""" Module with different file types. """

class Movie:
	titles = ['File', 'Title', 'Size']
	filters = ['File', 'Title']
	suffixes = ['.mkv', '.mp4']

	def __init__(self, attributes):
		self.attributes = attributes