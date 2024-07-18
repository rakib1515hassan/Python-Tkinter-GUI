# from tkinter import *
from tkinter import Tk, Menu, Label, Button, Entry, Checkbutton, IntVar, W, Radiobutton, Listbox
from tkinter.ttk import Combobox

root = Tk()

## =============== (Menu Bar) =================
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
## ============================================

root.title("Python | Tkinter")


##? First Name 
label1 = Label(root, text="First Name:", width=10).grid(row=0)
input1 = Entry(root, width=30).grid(row=0, column=1)

##? Last Name
label2 = Label(root, text="Last Name:", width=10).grid(row=2)
input2 = Entry(root, width=30).grid(row=2, column=1)

##? Sports (Check Button)
label3 = Label(root, text="Sports:", width=10).grid(row=3)

input3 = IntVar()
Checkbutton(root, text='Cricket', variable=input3, width=15).grid(row=3, column=1, sticky=W)

input4 = IntVar()
Checkbutton(root, text='Football', variable=input4, width=15).grid(row=3, column=2, sticky=W)

##? Gender (Radio Button)
label4 = Label(root, text="Gander:", width=10).grid(row=4)
input5 = IntVar()
Radiobutton(root, text='Male',  variable=input5, value=1).grid(row=4, column=1, sticky=W)
Radiobutton(root, text='Female', variable=input5, value=2).grid(row=4, column=2, sticky=W)


##? Gender (List Box)
label5 = Label(root, text="Language:", width=10).grid(row=5)
Lb = Listbox(root)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.grid(row=5, column=1)


##? City (Selected Item)
label6 = Label(root, text="Selected Item: ", width=10).grid(row=6)
combo_box = Combobox(root, values=[
                                    "Dhaka", 
                                    "Rajshahi", 
                                    "Sylhet", 
                                    "Mymensingh",
                                    "Barisal",
                                    "Rangpur",
                                    "Khulna",
                                ]).grid(row=6, column=1)



button = Button(root, text='Cancel', width=15, bg='red', fg='white', command=root.destroy).grid(row=7, column=0)
button = Button(root, text='Submit', width=15, bg='green', fg='white').grid(row=7, column=1)

root.mainloop()