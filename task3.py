import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("400x160")

dogPhoto = tk.PhotoImage(file="dog.png")
dogLabel = tk.Label(window, image = dogPhoto)

pochaccoLabel = tk.Label(window, text="Pochacco!")

descriptionLabel = tk.Label(window, text="A cuddly little puppy! this is from the same \ncreators who brought youKerope and Kero Kero", bg='cyan', width=45, height=3, font=('Bruh', 12))

dogLabel.place(x=125, y=0)
pochaccoLabel.place(x=200, y=40)
descriptionLabel.place(x=0, y=100)

window.mainloop()