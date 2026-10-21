# Write a program that Initializes total to 0, While the number is not 0, adds it to total.


number = int(input("Please enter a number (Press 0 to stop) : "))
total = 0

while number != 0:
    total += number
    number = int(input("Please enter a number : "))

print(total)

