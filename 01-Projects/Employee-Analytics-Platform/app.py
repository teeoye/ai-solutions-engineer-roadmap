
from employees.employee import Employee

def main():
    
    employee_id = input("Please enter id number : ")
    name = input("Please enter name : ")
    department = input("Please enter dept : ")
    salary = input("Please enter salary : ")
    employee1 = Employee(employee_id,name,department,salary)

    print("================================")
    print("Employee Analytics Platform")
    print("Version 0.1")
    print("================================")


    print()
    print("Employee ID : ",employee1.employee_id)
    print("Name : ",employee1.name)
    print("Department : ",employee1.department)
    print("Salary : ",employee1.salary)

if __name__ == "__main__":
    main()

