from domain.customer import Customer 
from domain.course import Course
from domain.feemanager import FeeManager
import numpy as np

customers = []
courses = []
fees = []
pay1 = []

def input_customer_infor():
        print(f"---------- Customer ---------")
        customer_id = int(input("Enter the customer ID: "))
        customer_name = input("Enter customer name: ")
        customer_dob = input("Enter customer date of birth (DD-MM-YYYY): ")
        customer_phone = int(input("Enter customer phone: "))
        customer_date = input("Enter the JoinDate: ")
        customer = Customer(customer_id,customer_name,customer_dob, customer_phone, customer_date)
        customers.append(customer)
        

    #data course
def input_course_infor():
        course_id = int(input("Enter the course ID: "))
        course_name = input("Enter the course name: ")
        course_fee = int(input("Enter the fee of course: "))
        course = Course(course_id,course_name,course_fee)
        courses.append(course)

def find_customer():
    new_list1 = []
    new_list2 = []
    new_list3 = []
    new_list4 = []
    new_list5 = []
    n = input("Enter the name of customer: ")
    for customer in customers:
        new_list1.append(customer.name)
        new_list2.append(customer.customer_id)
        new_list3.append(customer.dob)
        new_list4.append(customer.phone)
        new_list5.append(customer.date)

    arr = np.array(new_list1)
    if n in arr:
        print(f"| {'Customer ID': <10} | {'Customer Name': <20} | {'DOB': <10} | {'Phone:' :<10} | {'Join Date': <10} |")
        print("-" * 77)
        for i in range(0,len(new_list1)): #(0,2) i=1,2
                # ['hiep' ,'hieu' ,'hiep']
            if n == new_list1[i]: #hieu = 2
                print(f"| {new_list2[i]:11} | {new_list1[i]:20} | {new_list3[i]:10} | {new_list4[i]:10} | {new_list5[i]:10} |")    
    else:           
        print(f"Error! Customer {n} hasn't found")

# def to calculate money
def cal_fee():
        
        fee_list1  = [] #contains cus_id
        fee_list2  = [] #contains cus_name
        fee_list3 = [] # contains course id [12 23 45]
        customer_id = int(input("Enter the customer ID: "))
        customer_name = input("Enter customer name: ")
        for customer in customers:
            fee_list1.append(customer.customer_id)
            fee_list2.append(customer.name)
        for course in courses:
            fee_list3.append(course.course_id) 
            fees.append(course.fee) # fee of course sever [150 250]
        
        arr1 = np.array(fee_list3) # [111 222]
        arr2 = np.array(fees) # fee of course sever [150 250]
        k = 0
        if customer_id in fee_list1 and customer_name in fee_list2:
            x = int(input("Enter the  course id  to pay the fee: "))
            #check course id in arr1 yes or not!
            if x in arr1:
                for j in range(0,len(arr1)): # j-> 0 , 1 ; arr1 = [1 2]
                     
                    if x == arr1[j]: #location:1  
                        y = int(input("Enter the fee of the course: "))
                        for i in range(0, len(arr2)): # , range(0,2) ;fees = [150 250]
                            if i==j:
                                k = arr2[i] - y
                                      
                print(f"| {'Customer ID': <10} | {'Customer name': <20} | {'Course ID': <10} | {'Fee (USD)': <10} | {'Pay (USD)': <10} | {'Amount owed': <10} |")
                print("+" + "-" * 89 + "+")
                print(f"| {customer_id:11} | {customer_name:20} | {x:10} | {arr2[i]:10} | {y:10} | {k:11} |")
                pay1.append(FeeManager(customer_id,customer_name,x,arr2[i],y,k))# error
                
            else:
                print(f"Something wrong! The customer {customer_name} or the customer id {customer_id} have not exits.")
    
        else:
            print("Error! Customer has not found")