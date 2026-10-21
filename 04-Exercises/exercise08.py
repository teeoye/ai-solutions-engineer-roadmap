# Part A — Assignment
list_a =[10, 20, 30]
list_b = list_a
list_b.append(40)
print(list_a )
print(list_b )

# Part B — Copying
list_c =[10, 20, 30]
list_d = list_c.copy()
list_d.append(40)
print(list_c)
print(list_d)


# Why does appending 40 to list_b also affect list_a?
# It does affect it because b is a replica of a

# Why does appending 40 to list_d not affect list_c?
# It does affect it because d is a copy of c

