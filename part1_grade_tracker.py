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

## Part 2

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

## part 3

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85]),
]

print("\nClass Report:")
print("Name              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0
student_averages = []

for name, marks_list in class_data:
    avg = mean(marks_list)
    status = "Pass" if avg >= 60 else "Fail"
    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1
    student_averages.append(avg)
    print(f"{name:<17} | {avg:7.2f} | {status}")

class_topper_idx = student_averages.index(max(student_averages))
class_topper_name = class_data[class_topper_idx][0]
class_topper_avg = student_averages[class_topper_idx]

class_avg = mean(student_averages)

print("\nSummary:")
print(f"Pass: {pass_count}, Fail: {fail_count}")
print(f"Class topper: {class_topper_name} ({class_topper_avg:.2f})")
print(f"Class average: {class_avg:.2f}")

## part 4

clean_essay = essay.strip()
print("\nStep 1: clean_essay")
print(clean_essay)

title_essay = clean_essay.title()
print("\nStep 2: Title Case")
print(title_essay)

python_count = clean_essay.lower().count("python")
print("\nStep 3: python count")
print(python_count)

replaced_essay = clean_essay.replace("python", "Python 🐍")
print("\nStep 4: replace python")
print(replaced_essay)

sentences = clean_essay.split('. ')
print("\nStep 5: split sentences")
print(sentences)

print("\nStep 6: numbered sentences")
for i, sentence in enumerate(sentences, 1):
    s = sentence.strip()
    if s and not s.endswith('.'):
        s += '.'
    print(f"{i}. {s}")
