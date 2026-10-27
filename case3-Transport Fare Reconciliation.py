# Case Study 93: Transport Fare Reconciliation

# Passenger tuple: (name, category, distance, amount_collected)
passengers = [
    ("Arun", "Adult", 10, 50),
    ("Priya", "Student", 8, 20),
    ("Ravi", "Senior", 12, 30),
    ("Meena", "Adult", 5, 25),
    ("Kiran", "Student", 10, 30)
]

fare_per_km = 5
expected_total = 0
collected_total = 0

print("FARE RECONCILIATION REPORT")

for name, category, distance, collected in passengers:

    if category == "Adult":
        discount = 0
    elif category == "Student":
        discount = 50
    elif category == "Senior":
        discount = 40
    else:
        discount = 0

    base_fare = distance * fare_per_km
    expected_fare = base_fare - (base_fare * discount // 100)

    difference = collected - expected_fare

    expected_total += expected_fare
    collected_total += collected

    print("\nPassenger:", name)
    print("Category:", category)
    print("Distance:", distance, "km")
    print("Expected fare:", expected_fare)
    print("Collected fare:", collected)

    if difference == 0:
        print("Status: Correct")
    elif difference < 0:
        print("Status: Underpayment of", -difference)
    else:
        print("Status: Overpayment of", difference)

print("\nTOTAL SUMMARY")
print("Expected revenue:", expected_total)
print("Collected revenue:", collected_total)
print("Revenue difference:", collected_total - expected_total)