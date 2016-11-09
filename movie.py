
""" Module with different file types. """

class Movie:
	titles = ['File', 'Title', 'Size']
	filters = ['Title', 'File']
	suffixes = ['.mkv', '.mp4']

	def __init__(self, attributes):
		self.attributes = attributes