# Case Study 91: Registration Record Analyzer

# Format: ID|Name|Age|Email
records = [
    "R101|Arun|20|arun@gmail.com",
    "R102|Priya|19|priya@gmail.com",
    "R103|Kiran|17|kiran@gmail.com",
    "R101|Meena|21|meena@gmail.com",
    "R104|Raj|22|rajgmail.com",
    "R105|Anu|abc|anu@gmail.com",
    "R106|Sai|20|sai@gmail.com"
]

seen_ids = []
valid_records = []
errors = []

for record in records:
    fields = record.split("|")

    if len(fields) != 4:
        errors.append((record, "Incorrect field count"))
        continue

    reg_id, name, age, email = fields
    error = ""

    if len(reg_id) != 4 or not reg_id.startswith("R"):
        error = "Invalid ID format"
    elif reg_id in seen_ids:
        error = "Duplicate registration ID"
    elif len(name) < 2 or len(name) > 20:
        error = "Invalid name length"
    elif not age.isdigit():
        error = "Age must be numeric"
    elif int(age) < 18 or int(age) > 60:
        error = "Age out of range"
    elif "@" not in email or "." not in email:
        error = "Invalid email format"

    if reg_id not in seen_ids:
        seen_ids.append(reg_id)

    if error == "":
        valid_records.append((reg_id, name, int(age), email))
    else:
        errors.append((reg_id, error))

print("VALID REGISTRATION RECORDS")
for item in valid_records:
    print(item)

print("\nERROR REPORT")
for item in errors:
    print(item)

print("\nTotal records:", len(records))
print("Valid records:", len(valid_records))
print("Invalid records:", len(errors))