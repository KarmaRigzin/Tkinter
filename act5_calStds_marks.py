from tkinter import *
from tkinter import ttk

def calculate_marks():

    eng = float(eng_entry.get())
    dzo = float(dzo_entry.get())
    hist = float(hist_entry.get())
    geo = float(geo_entry.get())
    eco = float(eco_entry.get())
    

    # Calculate the total marks, percentage, and remarks
    total_marks = eng + dzo + hist + geo + eco
    percentage = round((total_marks / 500) * 100, 2)

    if percentage >= 40:
        remarks = "Pass"
    else:
        remarks = "Fail"

    # Display the results
    result_label.config(text=f"Total Marks: {total_marks}\nPercentage: {percentage}%\nRemarks: {remarks}")

def display_details():
    # Create a new window
    dw = Toplevel(root)
    dw.title("Mark Details")

    name = name_entry.get()
    name_label = Label(dw, text=f"Students Marks Detail of {name}")
    name_label.pack()

    done_butt = Button(dw, text="Done", command=dw.destroy)
    done_butt.pack()

    # Create the Treeview widget
    treeview = ttk.Treeview(dw, columns=("subject", "marks"))
    treeview.heading("subject", text="Subjects")
    treeview.heading("marks", text="Marks")
    treeview.pack()

    # Insert the values into the Treeview
    treeview.insert("", "end", values=("English",eng_entry.get()))
    treeview.insert("", "end", values=("Dzongkha",dzo_entry.get()))
    treeview.insert("", "end", values=("History",hist_entry.get()))
    treeview.insert("", "end", values=("Geography",geo_entry.get()))
    treeview.insert("", "end", values=("Economics",eco_entry.get()))
    treeview.insert("", "end", values=("Total Marks", round(float(eng_entry.get()) + float(dzo_entry.get()) + float(hist_entry.get()) + float(geo_entry.get()) + float(eco_entry.get()), 2)))
    treeview.insert("", "end", values=("Percentage", round(float(result_label.cget("text").split("\n")[1].split(":")[1].strip("%")), 2)))
    treeview.insert("", "end", values=("Results", result_label.cget("text").split("\n")[2].split(":")[1].strip()))

    
# Create the main window
root = Tk()
root.title("Marks Calculation")
root.geometry("500x450")

# widgets

Label(root, text ="Calculating Percentages for Marks").grid(row = 1, column =2)

Label(root, text="Std_code:").grid(row=2, column=1)
code_entry = Entry(root)
code_entry.grid(row=2, column=2)

Label(root, text="Name:").grid(row=3, column=1)
name_entry = Entry(root)
name_entry.grid(row=3, column=2)

Label(root, text="Class:").grid(row=4, column=1)
class_entry = Entry(root)
class_entry.grid(row=4, column=2)

Label(root, text="Section:").grid(row=5, column=1)
sec_entry = Entry(root)
sec_entry.grid(row=5, column=2)

Label(root, text="Gender:").grid(row=6, column=1)
gender_entry = Entry(root)
gender_entry.grid(row=6, column=2)


Label(root, text="English:").grid(row=7, column=1)
eng_entry = Entry(root)
eng_entry.grid(row=7, column=2)

Label(root, text="Dzongkha:").grid(row=8, column=1)
dzo_entry = Entry(root)
dzo_entry.grid(row=8, column=2)

Label(root, text="History:").grid(row=9, column=1)
hist_entry = Entry(root)
hist_entry.grid(row=9, column=2)

Label(root, text="Geography:").grid(row=10, column=1)
geo_entry = Entry(root)
geo_entry.grid(row=10, column=2)

Label(root, text="Economics:").grid(row=11, column=1)
eco_entry = Entry(root)
eco_entry.grid(row=11, column=2)


# Create the button to calculate the marks
calculate_button = Button(root, text="Calculate", command = calculate_marks)
calculate_button.grid(row=12, column=2)

# Create the button to display the mark details
details_button = Button(root, text="Display", command = display_details)
details_button.grid(row=17, column=2)

# Create the label to display the results
result_label = Label(root, text="")
result_label.grid(row=13, column=2, columnspan=2)

root.mainloop()
