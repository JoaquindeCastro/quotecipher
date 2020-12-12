from tkinter import *

root = Tk()

form = Frame(root)
form.pack()

label_name = Label(form, text="Name:")
label_password = Label(form, text="Password:")

input_name = Entry(form)
input_password = Entry(form)

label_name.grid(row=0,  sticky=E)
label_password.grid(row=1,  sticky=E)

input_name.grid(row=0,column=1)
input_password.grid(row=1,column=1)

root.mainloop()