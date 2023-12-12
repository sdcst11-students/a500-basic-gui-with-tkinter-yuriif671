#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

"""
We are reusing much of the same code from example2.py.
We are just going to use a different method of arranging the window
than using .pack(). 
"""

window = tk.Tk()
window.title("Packing Widgets example")
# this makes your window a fixed size; it cannot be resize in the (x,y) directions
window.resizable(False,False)
"""
.geometry is not used, because we want the window to grow to the
size of all the widgets combined and it should not be constrained
by the dimensions of the window
"""

label1 = tk.Label(window,text="Text that does\nnothing is a label", bg="#ee0000")

dogphoto = PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto, borderwidth=3, relief=SUNKEN)

lable3 = tk.Label(window, text="Note that an image can be in a label or a button!", borderwidth=4, relief=SUNKEN)

button1 = tk.Button(window,text="A button\nis clickable")

entry1 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)

combo = ttk.Combobox(window,values=["1","2","3"])

# Using .grid() instead of .pack()
"""

tkinter.grid() gives us some greater control over how the widgets are arranged in
your window.  grid() uses rows and columns to determine where widgets are placed.
You specify which row the widget is in, and in which column it is started in.
However, you can also allow a widget to span several columns using columnspan as an
option.  The grid() resizes all of the columns to make sure that their widgets fit,
so not every column will be the same size. You can also make a widget span multiple rows
using rowspan.
"""
label1.grid(row = 1, column = 1)
label2.grid(row = 1, column = 2, rowspan = 2)
lable3.grid(row = 2, column = 1)

# entry1 is centered on the 2 columns that have been created
entry1.grid(row=3, column = 1, columnspan=2)

window.mainloop()