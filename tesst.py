from tkinter import *

class Customer:
    def __init__(self, customer_id, name, dob):
        self.customer_id = customer_id
        self.name = name
        self.dob = dob
    
customers = []
courses = []

def input_customer_infor():
    customer_id = int(customer_id_entry.get())
    customer_name = customer_name_entry.get()
    customer_dob = customer_dob_entry.get()
    customer = Customer(customer_id,customer_name,customer_dob)
    customers.append(customer)
    customer_id_entry.delete(0, END)
    customer_name_entry.delete(0, END)
    customer_dob_entry.delete(0, END)

def show_customer():
    customer_listbox.delete(0, END)
    print(f"{'Customer ID': <10} | {'Name' :<10} | {'DOB':}|")
    for customer in customers:
        customer_listbox.insert(END, f"ID: {customer.customer_id} | Name: {customer.name} | DOB: {customer.dob}")

# create GUI window
root = Tk()
root.title("Customer Information")
root.geometry("600x400")

# create customer input fields and labels
customer_id_label = Label(root, text="Customer ID:")
customer_id_label.grid(row=0, column=0)

customer_id_entry = Entry(root, width=30)
customer_id_entry.grid(row=0, column=1)

customer_name_label = Label(root, text="Customer Name:")
customer_name_label.grid(row=1, column=0)
customer_name_entry = Entry(root, width=30)
customer_name_entry.grid(row=1, column=1)

customer_dob_label = Label(root, text="Date of Birth:")
customer_dob_label.grid(row=2, column=0)
customer_dob_entry = Entry(root, width=30)
customer_dob_entry.grid(row=2, column=1)

# create buttons to input and show customer information
input_button = Button(root, text="Input Customer", command=input_customer_infor)
input_button.grid(row=3, column=0)

show_button = Button(root, text="Show Customers", command=show_customer)
show_button.grid(row=3, column=1)

# create customer listbox to display customer information
customer_listbox = Listbox(root, width=80)
customer_listbox.grid(row=4, column=0, columnspan=2)

# run GUI
root.mainloop()
