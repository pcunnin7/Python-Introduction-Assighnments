from tkinter import Tk, Label, Entry, Button, TOP, LEFT, RIGHT, END
from tkinter.messagebox import showinfo

# This function takes an Entry widget as a parameter
# It evaluates the expression in the widget and replaces
# the expression with the result of the evaluation
def evaluate(entry):
    result = eval(entry.get())
    entry.delete(0,END)
    entry.insert(END, result)

# Define the main function
def main():
    root = Tk()
    root.title('Basic calculator')

    Label(root, text="Enter an arithmetic expression:").pack(side=TOP)
    ent = Entry(root)
    ent.pack()

    Button(root, text="Evaluate", command=lambda: evaluate(ent)).pack(side=LEFT)
    Button(root, text="Clear", command=lambda: ent.delete(0, END)).pack(side=RIGHT)
    
    root.mainloop()

