#!python3
"""
We start by importing a module, and also import all of the important
code from that module. I'm not sure why they do it this way, but 
that's the way it is.
"""
import tkinter as tk 
from tkinter import *
# the ttk command is required to get extra widgets, including the combobox
from tkinter import ttk


"""
We create an object using some of the built in functions from the
tkinter Tk class. We also use some of the object methods to set
some of the properties of the window.
"""
window = tk.Tk()
window.title("Packing Widgets example")
# Note, in this example, we removed the geometry to set the window size
# because packing the widgets tries to make the window as small as possible

"""
A window actually has an infinite running while loop while
it checks to see if any of the features of the window (buttons,
text entry, etc) are being mainpulated.  These features are also
called WIDGETS, and we'll see how they can be added in the next few
files.
"""

#creates a text label widget and stores it into the object "label1"
#Label options can be found at http://effbot.org/tkinterbook/label.htm
label1 = tk.Label(window,text="Text that does\nnothing is a label", bg="#ee0000")

#creates a text label widget that contains an image
# note: PhotoImage is part of the tk module, so without using
# from tkinter import *, we would have had to do: tk.PhotoImage(file="dog.ong")
dogphoto = PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto)

lable3 = tk.Label(window, text="Note that an image can be in a label or a button!")

#creates a button: see https://www.tutorialspoint.com/python/tk_button.htm for list of options
button1 = tk.Button(window,text="A button\nis clickable")

#creates an input box for text entry.  Config options can be found at https://effbot.org/tkinterbook/entry.htm
#Note, we will spend more time working with retrievin and working with information in a later lesson
entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=10)

combo = ttk.Combobox(window,values=["1","2","3"])

#checkbutton options can be found at http://effbot.org/tkinterbook/checkbutton.htm
check1 = tk.Checkbutton(window)


# Once the widgets have been defined, the order that they will appear in the window is 
# set by the order that they are packed.  Try moving them around and see what happens:
# There are options available when using tkinter.pack()
# tkinter.pack() options can be found at https://www.tutorialspoint.com/python/tk_pack.htm
label1.pack()
label2.pack()
lable3.pack()
button1.pack()
entry1.pack()
combo.pack()
check1.pack()

#--------------------------------------------------------------------------
# A Frame can be used to help organize how you want your widgets placed:
# A Frame acts like a single widget, into which you can put other widgets
# We can now position multiple frames in a row by adjusting the "side"
# when we pack() it.
nF = Frame()

#note that we use nF in the widget method here
fLabel1 = Label(nF,text="hi!", background="#ffaaff")
fLabel2 = Label(nF,text="another widget!", background="#aaffff")

nF.pack()
fLabel1.pack(side=LEFT)
fLabel2.pack(side=LEFT)
"""
Note some of the difficulty in trying to arrange your widgets1
Some alternatve good control over your widgets can also be achieved using the
geometry manager to place them into a grid or using the coordinates
(example3.py and exampl4.py
"""

window.mainloop()