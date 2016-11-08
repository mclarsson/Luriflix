
""" Module with interfaces. """

from terminaltables import AsciiTable
from Tkinter import *

class TextUI:
	""" Terminal UI for application. Mainly for development """

	def __init__(self, lfx):

		# List of all files
		self.complete_list = lfx.files

		# List of files found through search
		self.filtered_list = []

		# Currently active list of files
		self.current_list = self.complete_list

		# Main operation loop
		while True:

			command = raw_input(' >> ').split()
			
			operation = command[0]
			arguments = command[1:]

			if operation == "q":
				# Exit program
				return None

			elif operation == "ls":
				# Show list of application files
				self.print_list(self.current_list, list(lfx.titles)) # Duplicate titles with list()

			elif operation == "save":
				# Save
				lfx.save()

			elif operation == "scan":
				# Scan directory 
				lfx.scan(arguments[0])
				self.complete_list = lfx.files

			elif operation == "edit":
				# Edits property of file (example: edit 1 Title Lord Of The Rings)
				index = int(arguments[0]) - 1
				attr = arguments[1]
				value = " ".join(arguments[2:])
				lfx.files[index].attributes[attr] = value

			elif operation == "play":
				# Open movie
				index = int(arguments[0]) - 1
				file = self.current_list[index].attributes['Source'] + "\\" + self.current_list[index].attributes['File']
				lfx.run(file)

			elif operation == "search":
				self.filtered_list = lfx.filter(arguments)
				self.current_list = self.filtered_list
				self.print_list(self.current_list, lfx.titles)

			elif operation == "csearch":
				# Cancel search and reset list
				self.current_list = self.complete_list
				

	def print_list(self, files, titles):

		if len(files) > 0:

			titles.insert(0, '#')
			table_data = [titles] # first list in table is headers

			index = 1
			for file in files:
				row = [index]
				for title in titles[1:]:
					if title in file.attributes:
						row.append(file.attributes[title])
					else:
						row.append("")

				table_data.append(row)
				index += 1

			table = AsciiTable(table_data)
			print table.table

class MovieCover:
	width = 136
	height = 171
	margin = 20
	padding = 20
	hovered = -1

class GUI:
	def __init__(self, lfx):

		self.lfx = lfx

		# List of all files
		self.complete_list = lfx.files

		# List of files found through search
		self.filtered_list = []

		# Currently active list of files
		self.current_list = self.complete_list

		# GUI stuff
		
		# Main window
		self.top = Tk()
		self.top.minsize(width = 1024, height = 768)
		self.top.grid_columnconfigure(0, weight=1)
		self.top.grid_rowconfigure(1, weight=1)
		self.top.wm_title("Lurifliks")

		# Search field
		self.search_field = Entry(self.top, borderwidth = 0, foreground = "#222", background = "#eee")
		self.search_field.grid(column = 0, row = 0, sticky = 'we', columnspan = 2, ipadx = 10, ipady = 10, padx = (10, 0))
		self.search_field.bind("<KeyRelease>", self.search_key_released)

		# List of files
		self.file_list = Canvas(self.top, borderwidth = 0, background = "#fff")
		self.file_list.grid(column = 0, row = 1, sticky = 'wens')
		#self.file_list.bind("<Motion>", self.hover_file_list)

		# Scrollbar
		self.scrollbar = Scrollbar(self.top)
		self.scrollbar.config(command = self.file_list.yview)
		self.file_list.config(yscrollcommand = self.scrollbar.set)
		self.scrollbar.grid(column = 1, row = 1, sticky = 'sn')

		# Initiate
		self.print_covers()
		self.top.mainloop()

	def search_key_released(self, key):
		""" Called when a key is pressed in the search field """ 
		query = self.search_field.get()
		self.filtered_list = self.lfx.filter(query.split())

		if not self.search_field.get():
			# Print all if search field is empty
			self.current_list = self.complete_list
		else:
			self.current_list = self.filtered_list

		self.print_covers()

	def print_covers(self):
		""" Print current list of files. """

		width = MovieCover.width
		height = MovieCover.height
		margin = MovieCover.margin
		padding = MovieCover.padding

		total_width = margin * 2 + padding * 2 + width
		total_heigth = margin * 2 + padding * 2  + height

		self.file_list.delete("all")

		for i in range(len(self.current_list)):
			file = self.current_list[i]

			x1 = (total_width * (i % 4)) + margin + padding
			y1 = (i / 4) * total_heigth + margin + padding

			x2 = x1 + width
			y2 = y1 + height

			self.file_list.create_rectangle(x1, y1, x2, y2, fill = "#e0e0e0")
			self.file_list.create_text(x1 + ((x2 - x1) / 2), y2 + (margin / 2), text = file.attributes['Title'])

		self.file_list.configure(scrollregion = self.file_list.bbox("all"))

	def hover_file_list(self, event):
		scrolled = self.scrollbar.get()[0]
		canvas_height = self.file_list.bbox("all")[3]
		
		y = event.y + scrolled * canvas_height

		index = int(y) / (width + margin)
		
		self.print_covers()
