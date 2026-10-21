# Write a program that . Defines a function called calculate_average. Accepts two numbers as parameters: number1 and number2.
# Calculates their average inside the function using (number1 + number2) / 2.
# Returns the average.
# Calls the function with 80 and 100.
# Stores the returned value in a variable named average.
# Prints average.

def calculate_average(number1, number2):
    average = (number1 + number2) / 2
    return average

average = calculate_average(80, 100)
print(average)