from tkinter import *


class Cipher:

	def __init__(self, root, puzzle):

		self.root = root
		self.puzzle = puzzle

		row = 0
		col = 0
		code = puzzle.get_puzzle()
		legend = puzzle.legend
		answer_key = puzzle.answer_key
		self.answer_key = answer_key

		header = Frame(root).pack()
		# TOOLBAR
		'''
		toolbar = Frame(root)
		toolButton = Button(toolbar, text='New Game', command=self.new).pack(side=LEFT, padx=2, pady=2)
		toolbar.pack(side=TOP, fill=X)
		'''

		# HEADER
		title = Label(header, text='QUOTE CIPHER', font=("Helvetica", 18, "bold")).pack()

		legend_row = Frame(header)
		legend_row.pack()

		legend_col_count = 0

		for key, val in legend.items():
			legend_key = Label(legend_row,text=str(key)+':', font=("Helvetica", 12, "bold"))
			legend_key.grid(row=0, column=legend_col_count)
			legend_col_count+=1
			legend_val = Label(legend_row,text=val, font=("Helvetica", 12))
			legend_val.grid(row=0, column=legend_col_count, padx=(0, 10))
			legend_col_count+=1

		self.result = Label(header, text='', font=("Helvetica", 12))
		self.result.pack()

		self.checker = {key: [] for key in answer_key}

		# CONTAINER
		container = Frame(root, width=1200, height=1800)
		self.container = container
		container.pack()
		row_container = Frame(container)
		row_container.pack()

		labels = []
		boxes = []

		for word in code:
			labels_row = []
			boxes_row = []
			for k in range(len(word)):
				last = len(word)-1
				if type(word[k]) == int:
					label = Label(row_container,text=word[k])
					box = Entry(row_container, width=3)
					correct_letter = answer_key[word[k]]
					self.checker[word[k]].append(box)
					if word[k] in legend:
						box.insert(END, legend[word[k]])
					label.grid(row=row, column=col)
					box.grid(row=row+1, column=col)
				else:
					box = Label(row_container, text=word[k])
					box.grid(row=row+1, column=col)
				if k==last:
					col+=1	
				col+=1
			if col >= 16:
				col_count, row_count = row_container.grid_size()
				for col in range(0, col_count):
					row_container.grid_columnconfigure(col, minsize=20)
				row+=2
				col=0
				row_container = Frame(container)
				row_container.pack()
			labels.append(labels_row)
			boxes.append(boxes_row)

		author = Label(container, text=puzzle.quoteAuthor)


		buttonCheck = Button(root, text="Check", command=self.check)
		buttonCheck.pack(padx=10, pady=10)
		newGameButton = Button(root, text='New Game', command=self.new)
		newGameButton.pack(padx=10, pady=10)

		root.mainloop()

	def new(self):
		self.clear_widgets()
		self.puzzle.new()
		self.__init__(self.root, self.puzzle)

	def exit(self):
		print('Exiting...')

	def settings(self):
		print('go to settings')

	def check(self):
		success = True
		container_rows = [row for row in self.container.winfo_children()]
		for container_row in container_rows:
			entries = [entry for entry in container_row.winfo_children() if entry.winfo_class() == 'Entry']
			for entry in entries:
				correct_val = self.get_correct_val(entry)
				letter = entry.get()
				if str(letter) != str(correct_val):
					success = False
					entry.config({"background": "red"})
					entry.delete(0, END)
					self.result.config(text='Oops, try again', fg='red')
				else:
					entry.config({"background": "white"})
		if success == True:
			self.result.config(text='Success!', fg='green')

	def get_correct_val(self, entry):
		for key, entries in self.checker.items():
			if entry in entries:
				return self.answer_key[key]

	def clear_widgets(self):
		widget_list = self.all_children()
		for item in widget_list:
		    item.pack_forget()

	def all_children(self) :
	    _list = self.root.winfo_children()

	    for item in _list :
	        if item.winfo_children() :
	            _list.extend(item.winfo_children())

	    return _list
