# Write a program that contains a list named scores containing 45, 80, 30, 90, and 55.
# Uses a for loop to examine each score . Uses continue to skip any score below 50.  Prints every score that is 50 or higher.

numbers = [45, 80, 30, 90, 55]
for number in numbers:
    if number < 50:
        continue
    print(number)