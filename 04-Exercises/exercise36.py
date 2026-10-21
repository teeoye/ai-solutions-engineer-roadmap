# Write a program that Creates a set called skills containing "Python", "SQL", and "AWS".
# Adds "PostgreSQL" to the set.
# Removes "AWS" from the set.
# Prints the final set.
# Prints the number of items using len()

skills = {"Python", "SQL", "AWS"}

skills.add("PostgreSQL")
skills.remove("AWS")

print(skills)

print(len(skills))