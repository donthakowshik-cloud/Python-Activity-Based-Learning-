requirements = [
    ("Area A", 50, 1),
    ("Area B", 40, 3),
    ("Area C", 30, 2),
    ("Area D", 20, 1)
]

stock = 100
for i in range(len(requirements)):
    for j in range(i + 1, len(requirements)):
        if requirements[j][2] < requirements[i][2]:
            requirements[i], requirements[j] = (
                requirements[j], requirements[i]
            )

print("SUPPLY ALLOCATION REPORT")

allocated_total = 0
unmet_total = 0

for area, required, urgency in requirements:

    if stock >= required:
        allocated = required
    else:
        allocated = stock

    stock -= allocated
    unmet = required - allocated

    allocated_total += allocated
    unmet_total += unmet

    print("\nArea:", area)
    print("Urgency:", urgency)
    print("Required:", required)
    print("Allocated:", allocated)
    print("Unmet demand:", unmet)

print("\nFINAL SUMMARY")
print("Total allocated:", allocated_total)
print("Total unmet demand:", unmet_total)
print("Remaining stock:", stock)
