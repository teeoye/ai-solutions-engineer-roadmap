employee = {
    "employee_id": "EMP001",
    "name": "Taiwo",
    "department": "IT",
    "salary": 5000
}

print(employee["name"])

employee["salary"] = 6500
employee["location"] = "Lagos"

for key,value in employee.items():
    #print(key, value)
    print(f"{key}: {value}")
