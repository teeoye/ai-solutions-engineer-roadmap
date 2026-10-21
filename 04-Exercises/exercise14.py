# Create a list named salaries containing 1800, 3500, 4200, 2700, and 5000.
salaries = [1800, 3500, 4200, 2700, 5000]
# Initialize a variable named count to 0.
count = 0
# Use a for loop to examine each salary.
for salary in salaries:
    # Use an if statement to check whether the salary is greater than 3000.
    if salary > 3000:
        # Increase count by one each time a salary satisfies the condition.
        count = count + 1
# Print the final count after the loop.
print(count)



