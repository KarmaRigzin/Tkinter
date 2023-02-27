from tkinter import *

root = Tk()

name_label = Label(root, text = "Login Form")
name_label.grid(row = 1, column = 3)

name_label = Label(root, text = "Name: ")
name_label.grid(row = 2, column = 2)
name_entry = Entry(root, width =15)
name_entry.grid(row = 2,column = 3)

dob_label = Label(root, text = "DOB: ")
dob_label.grid(row = 3, column = 2)
dob_entry = Entry(root, width =15)
dob_entry.grid(row = 3,column = 3)

email_label = Label(root, text = "Email Address: ")
email_label.grid(row = 4, column = 2)
email_entry = Entry(root, width =15)
email_entry.grid(row = 4,column = 3)

phone_label = Label(root, text = "Phone Number: ")
phone_label.grid(row = 5, column = 2)
phone_entry = Entry(root, width =15)
phone_entry.grid(row = 5,column = 3)

password_label = Label(root, text = "Password: ")
password_label.grid(row = 6, column = 2)
password_entry = Entry(root, width =15, show ="*")
password_entry.grid(row = 6,column = 3)

but = Button(root, text="Login")
but.grid(row=7,column=1, columnspan=2)

butt = Button(root, text="Sign Up")
butt.grid(row=7,column=3, columnspan=2)

root.mainloop()
