
# Write a program that Creates a list named numbers containing 2, 4, 6, 8, and 10 . Uses a for loop to examine each number.
# Uses an if statement to check whether the number equals 6. If the number equals 6, use continue to skip it.

numbers = [2, 4, 6, 8, 10 ]
for number in numbers:
    if number == 6:
        continue
    print(number)