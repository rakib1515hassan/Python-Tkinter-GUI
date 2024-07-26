from tkinter import *

# def on_enter(self):
#     if usernameEntry.get()=='Username':
#         usernameEntry.delete(0, END)

def on_enter(event, entry):
    if entry.get() == 'Username':
        entry.delete(0, END)