class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

       

a = input("Please enter id number : ")
b = input("Please enter name : ")
c = input("Please enter dept : ")
d = input("Please enter salary : ")
employee1 = Employee(a,b,c,d)


e = input("Please enter id number : ")
f = input("Please enter name : ")
g = input("Please enter dept : ")
h = input("Please enter salary : ")
employee2 = Employee(e,f,g,h)

i = input("Please enter id number : ")
j = input("Please enter name : ")
k = input("Please enter dept : ")
l = input("Please enter salary : ")
employee3 = Employee(i,j,k,l)


print("Employee ID : ",employee1.employee_id)
print("Name : ",employee1.name)
print("Department : ",employee1.department)
print("Salary : ",employee1.salary)

print()
print("Employee ID : ",employee2.employee_id)
print("Name : ",employee2.name)
print("Department : ",employee2.department)
print("Salary : ",employee2.salary)
print()
print("Employee ID : ",employee3.employee_id)
print("Name : ",employee3.name)
print("Department : ",employee3.department)
print("Salary : ",employee3.salary)



