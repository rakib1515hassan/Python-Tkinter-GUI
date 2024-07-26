import tkinter
from tkinter import messagebox


def login():
    username = "rakib"
    password = "123456ra"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")


window = tkinter.Tk()
window.title("Login form")
# window.geometry('340x440')
window.geometry('620x440')

# window.configure(bg='#333333')
window.configure(bg='#F6F5F5')

frame = tkinter.Frame(bg='#333333', padx=20, pady=20)   ## Frame is a tkinter container like a html div

##? Creating widgets
login_label = tkinter.Label(
        frame, 
        text ="Login", 
        font = ("Arial", 30), ## Font Family and Font Size
        bg = "#333333",       ## Background Color
        fg = "#FF3399",       ## Foreground Colore (Text Color)
    )

username_label = tkinter.Label(
        frame, 
        text = "Username",
        font = ("Arial", 16),
        bg = "#333333", 
        fg = "#FFFFFF", 
    )

username_entry = tkinter.Entry(
        frame, 
        font = ("Arial", 16)
    )

password_entry = tkinter.Entry(
        frame, 
        show = "*", 
        font = ("Arial", 16)
    )

password_label = tkinter.Label(
        frame, 
        text = "Password", 
        font = ("Arial", 16),
        bg = '#333333', 
        fg = "#FFFFFF", 
    )

login_button = tkinter.Button(
        frame, 
        text = "Login", 
        font = ("Arial", 16),  
        bg = "#FF3399", 
        fg = "#FFFFFF", 
        command = login,

        activebackground="blue", 
        activeforeground="white",
        cursor="hand2",
    )



##? Placing widgets on the screen 
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()