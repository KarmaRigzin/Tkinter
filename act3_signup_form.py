from tkinter import *

root = Tk()
root.title("Sign Up Form")
root.configure(bg= "sky blue")
root.geometry("400x350")

var1 = IntVar()

sign_title = Label(root,text ="Sign Up Form").grid(row =1,column = 2)

name_label =Label(root, text="Name:").grid(row=2, column=1)
name_entry = Entry(root, width =15).grid(row=2, column=2)

p_label = Label(root, text="Password:").grid(row=3, column=1)
password_entry = Entry(root, show="*").grid(row=3, column=2)

# create radio buttons for Gender
gen = Label(root, text="Gender:").grid(row=4, column=1)

r1= Radiobutton(root, text="Male", variable=var1, value="male").grid(row=4, column=2)
r2 =Radiobutton(root, text="Female", variable=var1, value="female").grid(row=4, column=3)

# create a text box for Bio
tb = Label(root, text="Share your bio here...").grid(row=5, column=2)
bio_textbox = Text(root, height=5, width=40).grid(row=6, column=1, columnspan=3)

# create a check button for the agreement to terms
var2 = IntVar()
cb =Checkbutton(root, text="I agree to the terms and privacy policy", variable=var2).grid(row=7, column=1, columnspan=3)

# sign up button
sign_up = Button(root, text="Sign Up").grid(row=8, column=2, columnspan=3)

root.mainloop()
