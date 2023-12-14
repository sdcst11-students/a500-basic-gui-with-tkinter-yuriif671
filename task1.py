import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("400x150")

entryA = tk.Entry(window, borderwidth=3)
entryB = tk.Entry(window, borderwidth=3)
entryC = tk.Entry(window, borderwidth=3)

labelX = tk.Label(window,text="X")
labelEq = tk.Label(window,text="=")

entryA.grid(row=1, column = 1)
labelX.grid(row=1, column=2)
entryB.grid(row=1, column = 3)
labelEq.grid(row=1, column = 4)
entryC.grid(row=1, column=5)

window.mainloop()