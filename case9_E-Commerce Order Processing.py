# Case Study 99: E-Commerce Order Processing

# Product tuple: (name, price, opening_stock)
products = [
    ("Laptop", 50000, 10),
    ("Mouse", 500, 50),
    ("Keyboard", 1500, 30)
]

# Order tuple: (product_name, quantity, discount_percentage)
orders = [
    ("Laptop", 2, 10),
    ("Mouse", 5, 5),
    ("Keyboard", 3, 10)
]

# Returns: (product_name, returned_quantity)
returns = [
    ("Laptop", 1),
    ("Mouse", 1)
]

inventory = []
for name, price, stock in products:
    inventory.append([name, price, stock])

revenue = 0

print("ORDER PROCESSING REPORT")

for product_name, quantity, discount in orders:

    found = False

    for item in inventory:
        if item[0] == product_name:
            found = True

            if quantity <= item[2]:
                gross = item[1] * quantity
                discount_amount = gross * discount // 100
                net_amount = gross - discount_amount

                item[2] -= quantity
                revenue += net_amount

                print("\nProduct:", product_name)
                print("Quantity dispatched:", quantity)
                print("Gross amount:", gross)
                print("Discount:", discount_amount)
                print("Net amount:", net_amount)
                print("Status: Dispatched")
            else:
                print("\nProduct:", product_name)
                print("Status: Insufficient stock")

    if not found:
        print("Product not found:", product_name)

print("\nRETURN PROCESSING")

for product_name, returned_quantity in returns:
    for item in inventory:
        if item[0] == product_name:
            item[2] += returned_quantity
            refund = item[1] * returned_quantity
            revenue -= refund

            print(product_name, "returned:", returned_quantity)
            print("Refund amount:", refund)

print("\nFINAL INVENTORY")

for name, price, stock in inventory:
    print("Product:", name)
    print("Price:", price)
    print("Available stock:", stock)

print("\nRECONCILIATION SUMMARY")
print("Net revenue after returns:", revenue)