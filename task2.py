import tkinter as tk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("700x210")

#dog pic
dogPhoto = tk.PhotoImage(file="dog.png")
dogLabel = tk.Label(window, image = dogPhoto)

#labels
mainLabel = tk.Label(window, text="Client Database", font=('lol', 15))

nameLabel = tk.Label(window, text="Name")
typeLabel = tk.Label(window, text="Type")
breedLabel = tk.Label(window, text="Breed")
ownerLabel = tk.Label(window, text="Owner")
birthLabel = tk.Label(window, text="Birthdate")

#entry fields
searchField = tk.Entry(window, borderwidth=3)

nameField = tk.Entry(window, borderwidth=3)
typeField = tk.Entry(window, borderwidth=3)
breedField = tk.Entry(window, borderwidth=3)
ownerField = tk.Entry(window, borderwidth=3)
birthField = tk.Entry(window, borderwidth=3)

#buttons
searchButton = tk.Button(window, text='Search by Name')

previousButton = tk.Button(window, text='< Previous')
saveButton = tk.Button(window, text = 'Save Entry')
nextButton = tk.Button(window, text='Next >')

#grid
dogLabel.grid(row=1, column=1, rowspan=2)
mainLabel.grid(row=2, column=3)

searchButton.place(x= 470, y = 0)
searchField.place(x= 570, y = 0)

nameLabel.grid(row=3, column=1, pady=(25, 5))
typeLabel.grid(row=3, column=2, pady=(25, 5))
breedLabel.grid(row=3, column=3, pady=(25, 5))
ownerLabel.grid(row=3, column=4, pady=(25, 5))
birthLabel.grid(row=3, column=5, pady=(25, 5), padx=(30,0))

nameField.grid(row=4, column=1, )
typeField.grid(row=4, column=2, )
breedField.grid(row=4, column=3,)
ownerField.grid(row=4, column=4,)
birthField.grid(row=4, column=5, padx=(30, 0)) 

previousButton.grid(row=5, column=1)
saveButton.grid(row=5, column=3)
nextButton.grid(row=5, column=5)

window.mainloop()