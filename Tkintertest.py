from tkinter import *
import random

# Configure tkinter window
window = Tk()
window.title("Random number generator")
window.configure(background="white")

# Defining num for random number generation between 1-100
num = random.randint(1,100)

# Defining function buttonClick
def buttonClick():
    myLabel = Label(window, text=num, width=50, height=5, font=("Arial", 12))
    myLabel.pack()

# Creating button for generating Random number
PhysButton = Button(window, text="Generate random number", command=buttonClick, width=50, height=10, font=("Arial", 12))
PhysButton.pack()

window.mainloop()