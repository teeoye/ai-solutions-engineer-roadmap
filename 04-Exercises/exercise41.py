# Write a function called calculate_salary that  Accepts basic_salary and allowance as parameters.
# Calculates the total salary by adding them.
# Returns the total salary.
# Calls the function with a basic salary of 250000 and an allowance of 50000.
# Stores the result in total_salary and prints it.

def calculate_salary(basic_salary,allowance):
    total_salary = basic_salary + allowance
    return total_salary


total_salary = calculate_salary(250000,50000)
print(total_salary)