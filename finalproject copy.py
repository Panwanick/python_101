import json

students_data = []

for i in range(3):  # Input student details for 3 students
    print(f"\nEnter details for student {i+1}:")
    first_name = str(input("Enter first name: "))
    last_name = str(input("Enter last name: "))
    student_id = int(input("Enter student ID: "))
    math_score = int(input("Enter Mathematics score: "))
    science_score = int(input("Enter Science score: "))
    art_score = int(input("Enter Art score: "))

    if 80 <= math_score <= 100:
        math_grade = 'A'
    elif 70 <= math_score <= 79:
        math_grade = 'B'
    elif 60 <= math_score <= 69:
        math_grade = 'C'
    elif 50 <= math_score <= 59:
        math_grade = 'D'
    elif 0 <= math_score <= 49:
        math_grade = 'F'
    if 80 <= science_score <= 100:    # Calculate science score to grade
        science_grade = 'A'
    elif 70 <= science_score <= 79:
        science_grade = 'B'
    elif 60 <= science_score <= 69:
        science_grade = 'C'
    elif 50 <= science_score <= 59:
        science_grade = 'D'
    elif 0 <= science_score <= 49:
        science_grade = 'F'
    if 80 <= art_score <= 100:    # Calculate art score to grade
        art_grade = 'A'
    elif 70 <= art_score <= 79:
        art_grade = 'B'
    elif 60 <= art_score <= 69:
        art_grade = 'C'
    elif 50 <= art_score <= 59:
        art_grade = 'D'
    elif 0 <= art_score <= 49:
        art_grade = 'F'

# Create a dictionary for the student
student_dict = {
    "first_name": first_name,
    "last_name": last_name,
    "student_id": student_id,
    "math_score": math_score,
    "science_score": science_score,
    "art_score": art_score,
    "grade_math": math_grade,
    "grade_science": science_grade,
    "grade_art": art_grade
    }

# Append the student dictionary to the students list
students_data.append(student_dict)

# Save the list of students to a JSON file
with open("students.json", "a") as json_file:
    json.dump(students_data, json_file, indent=4)

print("\nStudent data has been saved to 'students.json'")

# Append information into students.txt
open("students.txt", "a")
try:
        with open("students.txt", "a", encoding="utf-8") as txt_file:
            for student in students_data:
                txt_file.write(f"นักเรียน: {student['first_name']} {student['last_name']} (รหัส: {student['student_id']})\n")
                txt_file.write(f"คะแนนวิชาคณิตศาสตร์: {student['math_score']} เกรด: {student['grade_math']}\n")
                txt_file.write(f"คะแนนวิชาวิทยาศาสตร์: {student['science_score']} เกรด: {student['grade_science']}\n")
                txt_file.write(f"คะแนนวิชาศิลปะ: {student['art_score']} เกรด: {student['grade_art']}\n")
                txt_file.write("-" * 40 + "\n")
            print("\nข้อมูลเกรดได้ถูกบันทึกลงในไฟล์ students.txt")
except Exception as e:
        print(f"เกิดข้อผิดพลาดในการบันทึกข้อมูล: {e}")