#!python3
"""
We start by importing a module, and also import all of the important
code from that module. 
"""

#This imports the tkinter file as tk
import tkinter as tk 

#This imports all the functions associated with the tkintter file as if they were in your local file
from tkinter import *


"""
We create an object using some of the built in functions from the
tkinter Tk class. We also use some of the object methods to set
some of the properties of the window.
"""
window = tk.Tk()
window.title("Hi!")
window.geometry("200x400")

"""
A window actually has an infinite running while loop while
it checks to see if any of the features of the window (buttons,
text entry, etc) are being mainpulated.  These features are also
called WIDGETS, and we'll see how they can be added in the next few
files.

In the rest of today's examples, we'll see how the different widgets
can be added to the window.  There are 3 main ways to do so:
pack() - them to make them fit in as small an area as possible
grid() - organize them into columns and rows (like a grid)
place() - will put widgets at specific coordinates in the window
"""
window.mainloop()
