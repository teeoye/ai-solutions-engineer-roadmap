# Write a function called calculate_discounted_price that .Accepts price and discount_percent.
# Gives discount_percent a default value of 10.
# Calculates the discount amount using price * discount_percent / 100.
# Returns the price after the discount is subtracted.
# Calls the function once with price = 20000 and no discount percentage.
# Calls it again with price = 20000 and discount_percent = 25.
# Prints both results.

def calculate_discounted_price(price, discount_percent=10):
    discount_amount = price * discount_percent / 100
    price = price - discount_amount
    return price


price = calculate_discounted_price(20000)
price1 = calculate_discounted_price(20000,25)

print(price)
print(price1)