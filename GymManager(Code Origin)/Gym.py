from input import *
from output import *
#main
def main():
    while(True):
        print("\n")
        print("------------ Gym Management System -------------")
        print("1. Add new customer ")
        print("2. Add the course ")
        print("3. Show all customer ")
        print("4. Show all courses ")
        print("5. Find the customer ")
        print("6. Input fee of customer ")
        print("7. Show customer unpaid ")
        print("0. Exit ")
            
        temp = int(input("Your option: "))
        if temp == 1:
            input_customer_infor()
        elif temp == 2:
            input_course_infor()
        elif temp == 3:
            show_customer()
        elif temp == 5:
            find_customer()
        elif temp == 4:
            show_course()
        elif temp == 6:
            cal_fee()
        elif temp == 7:
            show_customer_unpaid()
        elif temp == 0:
            break
        else:
            print("Invalid choice! ")

if __name__ == '__main__':
    main()
