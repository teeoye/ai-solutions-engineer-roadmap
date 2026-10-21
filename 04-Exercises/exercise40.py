# Write a function called calculate_area that Accepts length and width as parameters.
# Calculates the area by multiplying them.
# Returns the area instead of printing it inside the function.
# Calls the function with length = 10 and width = 5.
# Stores the returned value in a variable called area.
# Prints area.

def calculate_area(length,width):
    area = length * width
    return area


area = calculate_area(10,5)
print(area)