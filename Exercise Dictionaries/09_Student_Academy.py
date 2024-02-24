count_of_students = int(input())
students = {}
for student in range(count_of_students):
    student_name = input()
    student_grade = float(input())
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(student_grade)

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
        

