from employees.employee import Employee
from employees.department import Department




employee_id = input("Please enter id number : ")
name = input("Please enter name : ")
department = input("Please enter dept : ")
salary = input("Please enter salary : ")
employee1 = Employee(employee_id, name, department, salary)

employee_id = input("Please enter id number : ")
name = input("Please enter name : ")
department = input("Please enter dept : ")
salary = input("Please enter salary : ")
employee2 = Employee(employee_id, name, department, salary)


name = input("Please enter department name : ")
manager = input("Please enter manager name : ")
department1 = Department(name,manager)


name = input("Please enter department name : ")
manager = input("Please enter manager name : ")
department2 = Department(name,manager)


print("Employee ID : ",employee1.employee_id)
print("Name : ",employee1.name)
print("Department : ",employee1.department)
print("Salary : ",employee1.salary)

print("Employee ID : ",employee2.employee_id)
print("Name : ",employee2.name)
print("Department : ",employee2.department)
print("Salary : ",employee2.salary)

print("Department Name : ",department1.name)
print("Manager Name : ",department1.manager)

print("Department Name : ",department2.name)
print("Manager Name : ",department2.manager)




