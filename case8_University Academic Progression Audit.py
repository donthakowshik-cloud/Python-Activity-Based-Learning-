# Case Study 98: University Academic Progression Audit

# Subject tuple:
# (subject, marks, attendance_percentage, prerequisite_completed)

subjects = [
    ("Python", 75, 85, True),
    ("Mathematics", 42, 80, True),
    ("Physics", 35, 75, True),
    ("Data Structures", 68, 82, False),
    ("English", 55, 60, True)
]

pass_mark = 40
minimum_attendance = 75

eligible = True
total_marks = 0
total_subjects = len(subjects)

print("ACADEMIC PROGRESSION REPORT")

for subject, marks, attendance, prerequisite in subjects:

    total_marks += marks
    requirements = []

    if marks < pass_mark:
        requirements.append("Failed in subject")

    if attendance < minimum_attendance:
        requirements.append("Attendance shortage")

    if not prerequisite:
        requirements.append("Prerequisite incomplete")

    print("\nSubject:", subject)
    print("Marks:", marks)
    print("Attendance:", attendance, "%")
    print("Prerequisite completed:", prerequisite)

    if len(requirements) == 0:
        print("Status: Eligible")
    else:
        eligible = False
        print("Status: Requirements outstanding")

        for requirement in requirements:
            print("-", requirement)

average = total_marks / total_subjects

print("\nFINAL ACADEMIC SUMMARY")
print("Total marks:", total_marks)
print("Number of subjects:", total_subjects)
print("Average marks:", round(average, 2))

if eligible:
    print("Progression decision: Eligible")
else:
    print("Progression decision: Not eligible")