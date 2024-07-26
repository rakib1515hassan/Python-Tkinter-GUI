from tkinter import *
from PIL import ImageTk
from config import image_path
from utils import on_enter

def show_registration_window():
    # Create the registration window
    registration_window = Tk()
    registration_window.title("Registration Page")

    # Window Size Fix 990x660 and it open top 50px and left 50px
    registration_window.geometry('990x660+50+50')

    # First 0 means False value for the width and second 0 means False value for the height
    registration_window.resizable(0, 0)

    # Load the background image
    bgImage = ImageTk.PhotoImage(file=image_path)
    bgLabel = Label(registration_window, image=bgImage)
    bgLabel.place(x=0, y=0)

    heading = Label(
        registration_window, 
        text="USER REGISTRATION",
        font=('Microsoft Yahei UI Light', 23, 'bold'),
        bg='white',
        fg='firebrick1'
    )
    heading.place(x=605, y=120)

    usernameEntry = Entry(
        registration_window, 
        width=25, 
        font=('Microsoft Yahei UI Light', 11, 'bold'),
        bd=0,  # Border Remove
        fg='firebrick1'
    )
    usernameEntry.place(x=580, y=200)
    usernameEntry.insert(0, 'Username')  # 0 is the position of this `Username` text
    usernameEntry.bind('<FocusIn>', lambda event: on_enter(event, usernameEntry))

    registration_window.mainloop()
