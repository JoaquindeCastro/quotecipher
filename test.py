from tkinter import *
from puzzle.puzzle import Puzzle
from gui.gui import Cipher

root = Tk()
root.title('Quote Cipher Game')
cipher = Puzzle()
print(cipher.quote)

gui = Cipher(root, cipher)