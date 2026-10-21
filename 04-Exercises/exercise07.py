employees = ["Taiwo", "Kehinde", "Olumide", "Bukola", "Olugbade"]
# Part A — insert()

employees.insert(2,"David")
print(employees)

# Part B — remove()

employees.remove("Kehinde")
print(employees)

# Part C — pop()

removed_employee = employees.pop(2)
print(removed_employee)

#Part D — index()

employees.index("Bukola")
print(employees.index("Bukola"))

# Part E — count()
departments = ["IT", "HR", "IT", "Finance", "IT", "HR"]
print(departments.count("IT"))


# Part F — sort()
numbers = [45, 12, 78, 23, 9, 34]
numbers.sort()
print(numbers)

# Part G — sort(reverse)
numbers = [45, 12, 78, 23, 9, 34]
numbers.sort(reverse = "True")
print(numbers)

#Part H — reverse()
names = ["John", "Mary", "David", "Sarah"]
names.reverse()
print(names)





