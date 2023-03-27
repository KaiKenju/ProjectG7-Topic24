from input import * 
def show_customer():
        print("List of customer: ")
        print(f"| {'No':<5} | {'Customer ID': <10} | {'Customer Name': <20} | {'DOB': <10} | {'Phone' :<10} | {'Join Date' : <10} |")
        print("+" + "-" * 83 + "+")
        for index,customer in enumerate(customers):
            print(f"| {index:5} | {customer.customer_id:11} | {customer.name:20} | {customer.dob:10} | {customer.phone:10} | {customer.date:10} |")
        print("+" +"-" * 83 + "+")

    #show list of course
def show_course():
        print("List of course: ")
        print(f"| {'No': <5} | {'Course ID' :<10} | {'Course Name': <20} | {'Cost':<10} |")
        print("+" + "-" * 56 + "+")
        for index,course in enumerate(courses):
            print(f"| {index:5} |{course.course_id:11} | {course.name:20} | {course.fee:10} |")
        print("+" + "-" * 56 +  "+")

def show_customer_unpaid():
        print("List of customers who have not completed payment")
        print(f"| {'No':5} | {'Customer ID': <10} | {'Customer name': <10} | {'Course ID': <10} | {'Fee (USD)': <10} | {'Pay (USD)': <10} | {'Amount owed': <10} |")
        print("+" + "-" * 90 +  "+")
        for index,feepay in enumerate(pay1):
            print(f"| {index:5} | {feepay.customer_id:10} | {feepay.customer_name:14} | {feepay.course_id:10} | {feepay.fee:10} | {feepay.pay:10} | {feepay.pay_amount:11} |")
        print("+" + "-" * 90 + "+")
