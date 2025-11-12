# Student Grade Calculator

print("=== Student Grade Calculator ===")

name = input("Enter student name: ")

marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

average = sum(marks) / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print(f"\nStudent Name: {name}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
