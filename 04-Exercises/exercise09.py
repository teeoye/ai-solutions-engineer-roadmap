# Creates a list named employees
employees = ["Taiwo", "Kehinde", "Olumide", "Bukola", "Olugbade"]

# Prints First Employee
print(employees[0])

# Print last employee
print(employees[-1])

# Adds "David" to the end of the list.
employees.append("David")

# Removes "Kehinde" from the list.
employees.remove("Kehinde")

# Print the remaining employees
print(len(employees))

# Creates a separate copy named employees_copy
employees_copy = employees.copy()

# Adds "Mary" to employees_copy
employees_copy.append("Mary")

# Prints both lists to demonstrate that the original list remains unchanged by the final addition
print(employees)
print(employees_copy)