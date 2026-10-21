# Write a function named calculate_discount that, Accepts price and discount as parameters.
# Calculates the discounted price by subtracting discount from price.
# Returns the discounted price.
# Calls the function with price = 10000 and discount = 1500.
# Stores the result in final_price and prints it.

def calculate_discount(price, discount):
    final_price = price - discount
    return final_price


final_price = calculate_discount(10000, 1500)
print(final_price)
