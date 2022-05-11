#LAKSHMI URJITHA DHADIGAM - LAB 4-1223270

from personobject import Person,Customer,Employee

def get_input(choice):
    firstname = input("First Name: ")
    lastname = input("Last Name: ")
    email = input("Email: ")
    
    if choice == "c":
        print()
        number = input("Number: ")
        customer = Customer(firstname,lastname,email,number)
        return customer
    elif choice == "e":
        print()
        ssn = input("SSN: ")
        employee = Employee(firstname,lastname,email,ssn)
        return employee
def display(person):
    if isinstance(person, Customer):
        print("CUSTOMER")
    elif isinstance(person, Employee):
        print("EMPLOYEE")
    else:
        print("PERSON")
    print("Name: ", person.fullname)
    print("Email: ", person.email)
    if isinstance(person, Customer):
        print("Number: ",person.number)
    elif isinstance(person, Employee):
        print("SSN: ",person.ssn)
    print()

def main():
    print("Customer/Employee Data Entry")
    print()

    again = "y"
    while again.lower() == "y":
        choice = input("Customer or employee? (c/e):")
        print()
        if choice == "c" or choice == "e":
            person = get_input(choice)
            print()
            display(person)
        else:
            print("Invalid choice, try again")
            continue
        
        again = input("Continue? (y/n): ")
        print()

    print(" Bye! ")

if __name__=="__main__":
    main()
