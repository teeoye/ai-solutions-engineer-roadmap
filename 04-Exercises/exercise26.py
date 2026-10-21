# Write a program that Initializes total to 0 and count to 0, While the number is not 0, adds it to total and then increase count.


number = int(input("Please enter a number (Press 0 to stop) : "))
total = 0
count = 0

while number != 0:
    total += number
    count += 1
    number = int(input("Please enter a number : "))

print("Total : ", total )
print("Count : ", count)