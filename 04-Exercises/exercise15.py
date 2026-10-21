# Creates the salaries list above.
salaries = [2200, 4500, 1800, 6000, 3500, 2700]
# Initializes total to 0.
total = 0
# Initializes count to 0.
count = 0
# Uses a for loop to examine each salary.
for salary in salaries:
    # If a salary is greater than 3000, adds that salary to total and increases count by one.
    if salary > 3000:
        total = total + salary
        count = count + 1
# After the loop, prints both total and count.
print("total", total)
print("count", count)