branches = [
    ("Main Library", 40, 1),
    ("Science Branch", 30, 2),
    ("Arts Branch", 25, 3),
    ("Engineering Branch", 35, 1)
]

available_copies = 100
for i in range(len(branches)):
    for j in range(i + 1, len(branches)):
        if branches[j][2] < branches[i][2]:
            branches[i], branches[j] = branches[j], branches[i]

allocated_total = 0
unmet_total = 0

print("LIBRARY ALLOCATION REPORT")

for branch, required, priority in branches:

    allocated = min(required, available_copies)
    available_copies -= allocated
    unmet = required - allocated

    allocated_total += allocated
    unmet_total += unmet

    print("\nBranch:", branch)
    print("Priority:", priority)
    print("Required copies:", required)
    print("Allocated copies:", allocated)
    print("Unmet demand:", unmet)

print("\nFINAL SUMMARY")
print("Total allocated:", allocated_total)
print("Total unmet demand:", unmet_total)
print("Copies remaining:", available_copies)
