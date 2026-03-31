raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

print(raw_students)

student_103_name = None
for student in raw_students:
    clean_name = student["name"].strip().title()
    clean_roll = int(student["roll"].strip())
    clean_marks = list(map(int, student["marks_str"].split(",")))

    if clean_roll == 103:
        student_103_name = clean_name

    words = clean_name.split()
    is_valid = all(word.isalpha() for word in words)
    status = "✓ Valid name" if is_valid else "✗ Invalid name"

    print(f"Name: {clean_name}")
    print(f"Roll Number: {clean_roll}")
    print(f"Marks: {clean_marks}")
    print(f"Status: {status}")
    print("------")

