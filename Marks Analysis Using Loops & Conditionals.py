
def compute_grade(mark):
    if 90 <= mark <= 100:
        return "A+"
    if 80 <= mark <= 89:
        return "A"
    if 70 <= mark <= 79:
        return "B"
    if 60 <= mark <= 69:
        return "C"
    return "F"


print(f"Student: {student_name}\n")
print("Subject    Marks    Grade")
print("--------   -----    -----")
for subject, mark in zip(subjects, marks):
    grade = compute_grade(mark)
    print(f"{subject:<10}{mark:<9}{grade}")

from statistics import mean

total_marks = sum(marks)
avg_marks = mean(marks)
max_idx = marks.index(max(marks))
min_idx = marks.index(min(marks))

print("\nSummary:")
print(f"Total marks: {total_marks}")
print(f"Average marks: {avg_marks:.2f}")
print(f"Highest scoring subject: {subjects[max_idx]} ({marks[max_idx]})")
print(f"Lowest scoring subject: {subjects[min_idx]} ({marks[min_idx]})")

# While-loop marks entry system
new_subjects = []
new_marks = []
print("\nAdd new subjects (type 'done' as subject name to stop).")

while True:
    new_sub = input("Subject name: ").strip()
    if new_sub.lower() == "done":
        break
    if not new_sub:
        print("Empty subject name not allowed. Try again.")
        continue

    raw_mark = input("Marks (0-100): ").strip()
    try:
        mark_val = float(raw_mark)
        if mark_val != int(mark_val):
            mark_val = int(mark_val)
        if not (0 <= mark_val <= 100):
            raise ValueError("Out of range")
    except ValueError:
        print("Invalid marks entry. Please provide a number between 0 and 100.")
        continue

    new_subjects.append(new_sub)
    new_marks.append(int(mark_val))
    print(f"Added {new_sub} with marks {int(mark_val)}")

added_count = len(new_marks)
all_marks = marks + new_marks
updated_avg = mean(all_marks) if all_marks else 0

print(f"\nNew subjects added: {added_count}")
print(f"Updated average across all subjects: {updated_avg:.2f}")
