from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
import tkinter as tk
import sqlite3
from prettytable import PrettyTable


# Creating the universal font variables
headlabelfont = ("@Yu Gothic UI Semibold", 14, 'bold')
labelfont = ('Cambria', 14)
entryfont = ('Cambria', 12)

# Connecting to the Database where all information will be stored
connector = sqlite3.connect('GymManagement.db')
cursor = connector.cursor()

#create database 
connector.execute(
"CREATE TABLE IF NOT EXISTS GYM_MANAGEMENT (NO_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, ID TEXT, PHONE_NO TEXT, GENDER TEXT, DOB TEXT, JOINDATE TEXT, COURSE_ID TEXT, COURSE_NAME TEXT)"
) 

# Creating the functions
def reset_fields():
    global name_strvar, customerID_strvar, contact_strvar, gender_strvar, dob_strvar, join_strvar, courseid_strvar, coursename_strvar

    for i in ['name_strvar', 'customerID_strvar', 'contact_strvar', 'gender_strvar', 'dob_strvar','join_strvar', 'courseid_strvar','coursename_strvar']:
        exec(f"{i}.set('')") 
    
#reset
def reset_form():
    global tree
    tree.delete(*tree.get_children())

    reset_fields()

#display information from database
def display_records():
    tree.delete(*tree.get_children())

    curr = connector.execute('SELECT * FROM GYM_MANAGEMENT')
    data = curr.fetchall()

    for records in data:
        tree.insert('', END, values=records)

#add information
def add_record():
    global name_strvar, customerID_strvar, contact_strvar, gender_strvar, dob_strvar, join_strvar, courseid_strvar, coursename_strvar

    name = name_strvar.get()
    customer_id = customerID_strvar.get()
    contact = contact_strvar.get()
    gender = gender_strvar.get()
    dob = dob_strvar.get() 
    join = join_strvar.get()
    courseid = courseid_strvar.get()
    coursename = coursename_strvar.get()


    if not name or not customer_id or not contact or not gender or not dob or not join or not courseid or not coursename:
        mb.showerror('Error!', "Please fill all the missing fields!!")
    else:
        try:
            connector.execute(
            'INSERT INTO GYM_MANAGEMENT (NAME, ID, PHONE_NO, GENDER, DOB, JOINDATE, COURSE_ID, COURSE_NAME) VALUES (?,?,?,?,?,?,?,?)', (name, customer_id, contact, gender, dob, join, courseid, coursename)
            )
            connector.commit()
            mb.showinfo('Record added', f"Record of {name} was successfully added")
            reset_fields()
            display_records()
        except:
            mb.showerror('Wrong type', 'The type of the values entered is not accurate. Pls note that the contact field can only contain numbers')

#remove information 
def remove_record():
    if not tree.selection():
        mb.showerror('Error!', 'Please select an item from the database')
    else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values["values"]

        tree.delete(current_item)

        connector.execute('DELETE FROM GYM_MANAGEMENT WHERE NO_ID=%d' % selection[0])
        connector.commit()

        mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')

        display_records()

# choose the one customer to view in entry
def view_record():
    global name_strvar, customerID_strvar, contact_strvar, gender_strvar, dob_strvar, join_strvar, courseid_strvar, coursename_strvar

    current_item = tree.focus()
    values = tree.item(current_item)
    selection = values["values"]

    name_strvar.set(selection[1]); customerID_strvar.set(selection[2])
    contact_strvar.set(selection[3]); gender_strvar.set(selection[4])
    dob_strvar.set(selection[5]); join_strvar.set(selection[6])
    courseid_strvar.set(selection[7]); coursename_strvar.set(selection[8])

#search information
def search_record():
    keyword = entry_search.get()
    if not keyword:
        return

    tree.delete(*tree.get_children())
    curr = connector.execute('SELECT * FROM GYM_MANAGEMENT WHERE NAME LIKE ? OR ID LIKE ?',
        (f'%{keyword}%', f'%{keyword}%'))
    data = curr.fetchall()

    for record in data:
        tree.insert('', END, values=record)
    mb.showinfo("Search Results", f"Found {len(data)} records matching '{keyword}'")

#back
def back_information ():
    # Clear the entry search
    entry_search.delete(0, END)
    # Delete all results from the treeview widget
    tree.delete(*tree.get_children())
    # Display all records again
    display_records()
    
# Initializing the GUI window
main = Tk()
main.title('Gym Management System')
main.geometry('1000x600')
main.resizable(0, 0)

# Creating the background and foreground color variables
lf_bg = '#67cabc' # bg color for the left_frame
cf_bg = '#adff2f' # bg color for the center_frame

# Creating the StringVar or IntVar variables
name_strvar = StringVar()
customerID_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
join_strvar = StringVar()
courseid_strvar = StringVar()
coursename_strvar = StringVar()
dob_strvar = StringVar()

# Placing the components in the main window
Label(main, text="GYM MANAGEMENT SYSTEM", font=headlabelfont, bg='White',relief=tk.GROOVE).pack(side=TOP, fill=X)

left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)

center_frame = Frame(main, bg=cf_bg)
center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)

right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)


# Placing components in the left frame
Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(relx=0.375, rely=0.005)
Label(left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(relx=0.175, rely=0.09)
Label(left_frame, text="Customer ID", font=labelfont, bg=lf_bg).place(relx=0.2, rely=0.185)
Label(left_frame, text="Gender", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.275)
Label(left_frame, text="Date of Birth (DOB)", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.39)
Label(left_frame, text="Join Date", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.50)
Label(left_frame, text="Course ID", font=labelfont, bg=lf_bg).place(relx=0.26, rely=0.60)
Label(left_frame, text="Course Name", font=labelfont, bg=lf_bg).place(relx=0.20, rely=0.70)
Label(center_frame, text='Search by Name/ID:', font=labelfont, bg=cf_bg).place(relx=0.1, rely=0.10)
#create entry
Entry(left_frame, width=19, textvariable=name_strvar, font=entryfont).place(x=14, rely=0.05)
Entry(left_frame, width=19, textvariable=contact_strvar, font=entryfont).place(x=14, rely=0.14)
Entry(left_frame, width=19, textvariable=customerID_strvar, font=entryfont).place(x=14, rely=0.23)
OptionMenu(left_frame, gender_strvar, 'Male', "Female").place(x=55, rely=0.32, relwidth=0.4)
Entry(left_frame, width=19, textvariable=dob_strvar, font=entryfont).place(x=16, rely=0.45)
Entry(left_frame, width=19, textvariable=join_strvar, font=entryfont).place(x=14, rely=0.55)
Entry(left_frame, width=19, textvariable=courseid_strvar, font=entryfont).place(x=14, rely=0.65)
Entry(left_frame, width=19, textvariable=coursename_strvar, font=entryfont).place(x=14, rely=0.75)
entry_search = Entry(center_frame, width=19, font=entryfont)
entry_search.place(relx=0.07, rely=0.15)


Button(left_frame, text='Submit', font=labelfont, command=add_record, width=10).place(relx=0.2, rely=0.85)

# Placing components in the center frame
Button(center_frame, text='Delete Record', font=labelfont, command=remove_record, width=15).place(relx=0.1, rely=0.25)
Button(center_frame, text='View Record', font=labelfont, command=view_record, width=15).place(relx=0.1, rely=0.35)
Button(center_frame, text='Reset Fields', font=labelfont, command=reset_fields, width=15).place(relx=0.1, rely=0.45)
Button(center_frame, text='Delete database', font=labelfont, command=reset_form, width=15).place(relx=0.1, rely=0.55)
Button(center_frame, text='Back', font=labelfont, command=back_information, width=15).place(relx=0.1, rely=0.65)
Button(center_frame, text='Search', font=labelfont, command=search_record, width=15).place(relx=0.1, rely=0.03)
# Placing components in the right frame
Label(right_frame, text='Customer Records', font=headlabelfont, bg='DarkGreen', fg='LightCyan').pack(side=TOP, fill=X)

tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                    columns=('NO_ID', "Name", "Customer ID", "Contact Number", "Gender", "Date of Birth", "JoinDate", "Course ID", "Course Name"))

X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)

tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)

tree.heading('NO_ID', text='No', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Customer ID', text='ID', anchor=CENTER)
tree.heading('Contact Number', text='Phone', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('JoinDate', text='Join Date', anchor=CENTER)
tree.heading('Course ID', text='Course ID', anchor=CENTER)
tree.heading('Course Name', text='Course Name', anchor=CENTER)

tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=80, stretch=NO)
tree.column('#3', width=43, stretch=NO)
tree.column('#4', width=57, stretch=NO)
tree.column('#5', width=48, stretch=NO) #gender
tree.column('#6', width=70, stretch=NO)
tree.column('#7', width=70, stretch=NO)
tree.column('#8', width=80, stretch=NO)
tree.column('#9', width=90, stretch=NO)

tree.place(y=30, relwidth=1, relheight=0.9, relx=0)

# Finalizing the GUI window
main.update()
main.mainloop()



 
