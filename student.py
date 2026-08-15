students = {
    "Rahul": "A",
    "Priya": "B",
    "Amit": "C"
}

print("Current student grades:")
for name, grade in students.items():
    print(name, ":", grade)

# Add a new student
new_student = input("Enter a new student name: ")
new_grade = input("Enter the grade: ")

if new_student in students:
    print("Student already exists.")
else:
    students[new_student] = new_grade
    print("Student added successfully.")

# Update an existing student's grade
update_student = input("Enter the student name to update: ")

if update_student in students:
    updated_grade = input("Enter the new grade: ")
    students[update_student] = updated_grade
    print("Grade updated successfully.")
else:
    print("Student not found.")

# Print all student grades
print("\nAll student grades:")
for name, grade in students.items():
    print(name, ":", grade)