from tkinter import *
from config import image_path

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

def toggle_password_visibility(passwordEntry, eyeButton, openEyeImage, closeEyeImage, placeholder):
    if passwordEntry.get() != placeholder:
        if passwordEntry.cget('show') == '*':
            passwordEntry.config(show='')
            eyeButton.config(image=openEyeImage)
        else:
            passwordEntry.config(show='*')
            eyeButton.config(image=closeEyeImage)

def mask_password(event, entry, placeholder):
    if entry.get() != placeholder:
        entry.config(show='*')
    
