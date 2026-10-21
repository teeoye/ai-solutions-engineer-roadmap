# Part  A : Create a list

employees = ["Taiwo","Kehinde","Olumide","Bukola","Olugbade"]

# Part  B : Print Entire list
print(employees)

# Part  C : Print: - the first employee- the second employee- the last employee
print(employees[0])
print(employees[1])
print(employees[2])

# Part  D : Add a sixth employee using:

employees.append("Folawiyo")

# Part  E : Remove an employee using:
employees.remove("Folawiyo")

# Part  F : Final print
print(employees)

# Part  G :  print length
print(len(employees))

# Part  H :  search
if "Kehinde" in employees:
    print("yes")

# Part A.Print: ["Taiwo", "Kehinde"]
print(employees[0:2])

# Part B.Print: ["Olumide", "Bukola", "Olugbade"]
print(employees[2:])

# Part C.Print: ["Bukola", "Olugbade"]
print(employees[3:])

# Part D.Print: ["Taiwo", "Kehinde", "Olumide", "Bukola"]
print(employees[0:])

# Part E.Print:  every second employee, starting from Taiwo:
print(employees[0:5:2])

# Part F.Print:  the employees in reverse order:
print(employees[::-1])


