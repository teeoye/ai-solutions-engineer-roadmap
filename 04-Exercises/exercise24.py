# Write a program that Continues asking for numbers while the entered number is not 0.


number = int(input("Please enter a number (0 to stop): "))

while number !=0:
    print(number)
    number = int(input("Please enter a number (0 to stop) : "))

print("Program ended.")

