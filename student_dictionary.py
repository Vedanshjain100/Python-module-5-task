student = {"Rahul": 57,
           "Mohit": 45,
           "Teena": 37,
           "John": 77,
           "Vedansh":94
           }
name = input("Enter The Student Name:")
if name in student:
    print(f"{name} marks {student[name]}")
else:
    print("Student not found")