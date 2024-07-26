from tkinter import *
from PIL import ImageTk
from config import image_path
from auth.utils import on_enter, on_leave

def show_login_window():
    # Create the login window
    login_window = Tk()
    login_window.title("Login Page")

    # Window Size Fix 990x660 and it open top 50px and left 50px
    login_window.geometry('990x660+50+50')

    # First 0 means False value for the width and second 0 means False value for the height
    login_window.resizable(0, 0)

    # Load the background image
    bgImage = ImageTk.PhotoImage(file=image_path+'/bg.jpg')
    bgLabel = Label(login_window, image=bgImage)
    bgLabel.place(x=0, y=0)

    heading = Label(
        login_window, 
        text="USER LOGIN",
        font=('Microsoft Yahei UI Light', 23, 'bold'),
        bg='white',
        fg='firebrick1'
    )
    heading.place(x=605, y=120)


    ##? Username Inpute
    usernameEntry = Entry(
        login_window, 
        width=25, 
        font=('Microsoft Yahei UI Light', 11, 'bold'),
        bd=0,  # Border Remove
        fg='firebrick1'
    )
    usernameEntry.place(x=580, y=200)
    usernameEntry.insert(0, 'Username')  # 0 is the position of this `Username` text
    # usernameEntry.bind('<FocusIn>', lambda event: on_enter(event, usernameEntry, 'Username'))

    usernameEntry.bind('<FocusIn>', lambda event: on_enter(event, usernameEntry, 'Username'))
    usernameEntry.bind('<FocusOut>', lambda event: on_leave(event, usernameEntry, 'Username'))
    

    frame1 = Frame(
        login_window,
        width=250,
        height=2,
        bg='firebrick1'
    )
    frame1.place(x=580, y=222)



    ##? Password Inpute
    passwordEntry = Entry(
        login_window, 
        width=25, 
        font=('Microsoft Yahei UI Light', 11, 'bold'),
        bd=0,  # Border Remove
        fg='firebrick1'
    )
    passwordEntry.place(x=580, y=260)
    passwordEntry.insert(0, 'Password')  # 0 is the position of this `Password` text
    # passwordEntry.bind('<FocusIn>', lambda event: on_enter(event, passwordEntry, 'Password'))

    passwordEntry.bind('<FocusIn>', lambda event: on_enter(event, passwordEntry, 'Password'))
    passwordEntry.bind('<FocusOut>', lambda event: on_leave(event, passwordEntry, 'Password'))
    

    frame2 = Frame(
        login_window,
        width=250,
        height=2,
        bg='firebrick1'
    )
    frame2.place(x=580, y=284)




    login_window.mainloop()
