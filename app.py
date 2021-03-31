from tkinter import *
from puzzle.puzzle import Puzzle
from gui.gui import Cipher

root = Tk()
root.title('Quote Cipher Game')
'''
rooticon = PhotoImage(file='static/icon.ico')
root.tk.call('wm', 'iconphoto', root._w, rooticon)
'''
root.iconbitmap('static/icon.ico')
root.state("zoomed")
cipher = Puzzle()
gui = Cipher(root, cipher)