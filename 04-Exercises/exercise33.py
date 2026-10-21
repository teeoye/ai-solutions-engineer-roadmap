product = {
    "name": "Laptop",
    "price": 850000,
    "quantity": 4
}

print(product["name"])

product["price"] = 900000
product["category"] = "Electronics"

for key,value in product.items():
    #print(key, value)
    print(f"{key}: {value}")

    
