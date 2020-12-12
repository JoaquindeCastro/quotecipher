			labels[k].grid(row=row, column=col, padx=(0,20))
			boxes[k].grid(row=row+1, column=col, padx=(0,20))

	row_label_container = Frame(container)
	row_label_container.pack()
	row_box_container = Frame(container)
	row_box_container.pack()
	for k in range(len(word)):
		if type(word[k]) == int:
			label = Label(row_label_container,text=word[k])
			box = Entry(row_box_container, width=5)
			label.grid(row=row, column=col, padx=0)
			box.grid(row=row+1, column=col, padx=0)
			last = len(word)-1
		else:
			box = Label(row_label_container, text=word[k])
			box.grid(row=row+1, column=col)
		if k==last:
			col+=1	
		col+=1
	if col >= 10:
		row+=2
		col=0


		# START MENU 
		menu = Menu(header)
		root.config(menu=menu)

		fileMenu = Menu(menu, tearoff=0)
		menu.add_cascade(label='File', menu=fileMenu)
		fileMenu.add_command(label='New', command=self.new)
		fileMenu.add_command(label='Open', command=self.new)
		fileMenu.add_separator()
		fileMenu.add_command(label='Exit', command=self.exit)

		settingsMenu = Menu(menu, tearoff=0)
		menu.add_cascade(label='Settings', menu=settingsMenu)
		settingsMenu.add_command(label='Settings', command=self.settings)
		# END MENU