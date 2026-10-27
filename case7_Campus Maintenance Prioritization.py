# Case Study 97: Campus Maintenance Prioritization

# Incident tuple: (ID, location, severity, frequency)
# Severity: 1 = low, 2 = medium, 3 = high

incidents = [
    ("I101", "Classroom", 2, 5),
    ("I102", "Laboratory", 3, 4),
    ("I103", "Library", 1, 8),
    ("I104", "Hostel", 3, 7),
    ("I105", "Canteen", 2, 3)
]

ranked = []

for incident_id, location, severity, frequency in incidents:

    if severity == 3:
        priority = 3
    elif severity == 2:
        priority = 2
    else:
        priority = 1

    # Give additional priority to frequent reports
    score = priority * 10 + frequency

    if severity == 3 or frequency >= 7:
        status = "Urgent"
    elif severity == 2 or frequency >= 4:
        status = "Medium"
    else:
        status = "Low"

    ranked.append(
        (incident_id, location, severity, frequency, score, status)
    )

# Sort by score in descending order
for i in range(len(ranked)):
    for j in range(i + 1, len(ranked)):
        if ranked[j][4] > ranked[i][4]:
            ranked[i], ranked[j] = ranked[j], ranked[i]

print("PRIORITIZED INCIDENT REPORT")

urgent_count = 0
medium_count = 0
low_count = 0

for item in ranked:
    incident_id, location, severity, frequency, score, status = item

    print("\nIncident:", incident_id)
    print("Location:", location)
    print("Severity:", severity)
    print("Report frequency:", frequency)
    print("Priority score:", score)
    print("Classification:", status)

    if status == "Urgent":
        urgent_count += 1
    elif status == "Medium":
        medium_count += 1
    else:
        low_count += 1

print("\nPRIORITY SUMMARY")
print("Urgent incidents:", urgent_count)
print("Medium incidents:", medium_count)
print("Low-priority incidents:", low_count)