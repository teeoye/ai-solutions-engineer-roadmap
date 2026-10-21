# Write a program that uses forloop to examine age

ages = [15, 22, 17, 30, 12]
for age in ages:
    if age >= 18:
        print(age, "is an adult")
    else:
        print(age, "is a minor")