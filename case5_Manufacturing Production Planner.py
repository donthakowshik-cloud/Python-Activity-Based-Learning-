materials = [
    ("Steel", 500, 5),
    ("Plastic", 300, 2),
    ("Rubber", 150, 1)
]

order_demand = 80
planned_production = order_demand

print("MATERIAL REQUIREMENT REPORT")

for material, available, per_unit in materials:
    possible_units = available // per_unit

    print("\nMaterial:", material)
    print("Available:", available)
    print("Required per product:", per_unit)
    print("Products supported:", possible_units)

    if possible_units < planned_production:
        planned_production = possible_units

print("\nPRODUCTION FEASIBILITY")
print("Order demand:", order_demand)
print("Maximum feasible production:", planned_production)

if planned_production >= order_demand:
    print("Status: Order can be completed")
else:
    print("Status: Material shortage exists")
    print("Units short:", order_demand - planned_production)
produced = planned_production
defects = 6
defect_limit_percent = 5

if produced > 0:
    defect_percentage = defects * 100 / produced
else:
    defect_percentage = 0

print("\nQUALITY REPORT")
print("Units produced:", produced)
print("Defective units:", defects)
print("Defect percentage:", round(defect_percentage, 2), "%")

if defect_percentage <= defect_limit_percent:
    print("Quality status: Acceptable")
else:
    print("Quality status: Quality violation")

print("\nORDER SUMMARY")
print("Demand:", order_demand)
print("Produced:", produced)
print("Unfulfilled demand:", order_demand - produced)
