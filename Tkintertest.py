from tkinter import *
import random

# Configure tkinter window
window = Tk()
window.title("My app window")
window.configure(background="white")

# Defining num for random number generation between 1-100
num = random.randint(1,100)

# Defining function buttonClick
def buttonClick():
    myLabel = Label(window, text=num)
    myLabel.pack()

# Creating button for generating Random number
PhysButton = Button(window, text="Generate random number", command=buttonClick)
PhysButton.pack()

window.mainloop()