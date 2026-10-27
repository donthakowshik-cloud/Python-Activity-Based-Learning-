# Case Study 100: Smart Campus Management

students = []
events = []
resources = []

while True:
    print("\n===== SMART CAMPUS MANAGEMENT =====")
    print("1. Add Student")
    print("2. Record Attendance")
    print("3. Enter Marks")
    print("4. Register for Event")
    print("5. Allocate Resources")
    print("6. Display Student Records")
    print("7. Display Summary")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter student ID: ")

        duplicate = False

        for student in students:
            if student[0] == student_id:
                duplicate = True

        if duplicate:
            print("Student ID already exists")
        else:
            name = input("Enter student name: ")

            # [ID, name, attendance, marks, events]
            students.append([student_id, name, 0, 0, []])
            print("Student added successfully")

    elif choice == "2":
        student_id = input("Enter student ID: ")
        found = False

        for student in students:
            if student[0] == student_id:
                attendance = int(
                    input("Enter attendance percentage: ")
                )

                if 0 <= attendance <= 100:
                    student[2] = attendance
                    print("Attendance recorded")
                else:
                    print("Invalid attendance percentage")

                found = True
                break

        if not found:
            print("Student not found")

    elif choice == "3":
        student_id = input("Enter student ID: ")
        found = False

        for student in students:
            if student[0] == student_id:
                marks = int(input("Enter marks out of 100: "))

                if 0 <= marks <= 100:
                    student[3] = marks
                    print("Marks recorded")
                else:
                    print("Invalid marks")

                found = True
                break

        if not found:
            print("Student not found")

    elif choice == "4":
        student_id = input("Enter student ID: ")
        event_name = input("Enter event name: ")
        found = False

        for student in students:
            if student[0] == student_id:
                if event_name not in student[4]:
                    student[4].append(event_name)
                    events.append((student_id, event_name))
                    print("Event registration successful")
                else:
                    print("Already registered for this event")

                found = True
                break

        if not found:
            print("Student not found")

    elif choice == "5":
        resource_name = input("Enter resource name: ")
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            resources.append((resource_name, quantity))
            print("Resource allocated")
        else:
            print("Quantity must be positive")

    elif choice == "6":
        print("\nSTUDENT RECORDS")

        for student_id, name, attendance, marks, registered_events in students:
            print("\nStudent ID:", student_id)
            print("Name:", name)
            print("Attendance:", attendance, "%")
            print("Marks:", marks)
            print("Events:", registered_events)

            if attendance < 75:
                print("Warning: Attendance shortage")

            if marks < 40:
                print("Warning: Marks below pass level")

    elif choice == "7":
        print("\nCAMPUS SUMMARY")
        print("Total students:", len(students))
        print("Total event registrations:", len(events))
        print("Total resource allocations:", len(resources))

        print("\nEVENT REGISTRATIONS")
        for student_id, event_name in events:
            print(student_id, "-", event_name)

        print("\nRESOURCE ALLOCATIONS")
        for resource_name, quantity in resources:
            print(resource_name, "-", quantity)

        passed = 0
        failed = 0

        for student in students:
            if student[3] >= 40:
                passed += 1
            else:
                failed += 1

        print("\nAcademic Summary")
        print("Students meeting the marks threshold:", passed)
        print("Students below the marks threshold:", failed)

    elif choice == "8":
        print("Exiting Smart Campus Management System")
        break

    else:
        print("Invalid choice. Please try again.")