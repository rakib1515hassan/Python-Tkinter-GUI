from tkinter import *

# def on_enter(self):
#     if usernameEntry.get()=='Username':
#         usernameEntry.delete(0, END)

# def on_enter(event, entry):
#     if entry.get() == 'Username':
#         entry.delete(0, END)


# def on_enter(event, entry, placeholder):
#     if entry.get() == placeholder:
#         entry.delete(0, END)


def on_enter(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, END)
        entry.config(fg='black')

def on_leave(event, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='firebrick1')
