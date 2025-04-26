import json

# Function to calculate grade based on score
def calculate_grade(score): # Define the function "calculate_grade"
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    return 'F'

# Function to get student data
def get_student_data(): # Define the function "get_student_data"
    students = []
    for i in range(3):  # Get data for 3 students
        print(f"\nEnter details for student {i+1}:")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        student_id = input("Student ID: ")
        math_score = float(input("Math score (0-100): "))
        science_score = float(input("Science score (0-100): "))
        art_score = float(input("Art score (0-100): "))

        student_data = {
            "first_name": first_name,
            "last_name": last_name,
            "student_id": student_id,
            "math_score": math_score,
            "science_score": science_score,
            "art_score": art_score,
            "grade_math": calculate_grade(math_score),
            "grade_science": calculate_grade(science_score),
            "grade_art": calculate_grade(art_score)
        }
        
        students.append(student_data)
    with open("students.json", 'r', encoding="utf-8") as x:
        jsonstring = x.read()
    jsonobject = json.loads(jsonstring)
    for j in range(len(jsonobject)):
        print(jsonobject[j]['math_score'])
        jsonobject[j]['grade_math'] = calculate_grade(jsonobject[j]['math_score'])
        print(jsonobject[j]['art_score'])
        jsonobject[j]['grade_art'] = calculate_grade(jsonobject[j]['art_score'])
        print(jsonobject[j]['science_score'])
        jsonobject[j]['grade_science'] = calculate_grade(jsonobject[j]['science_score'])

    return students

# Save data to the existing JSON file
def save_to_json(students): # Define the fuction "save_to_json"
    try:
        # Try to load existing data from the file
        try:
            with open("students.json", "r", encoding="utf-8") as file:
                existing_data = json.load(file) # Read existing data and store in the "existing_data"
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []  # If file doesn't exist or is empty, initialize an empty list

        # Append the new students' data to the existing data
        existing_data.extend(students)

        # Save the updated list back to the same JSON file
        with open("students.json", "w", encoding="utf-8") as file: # Open the file students.json for writing
            json.dump(existing_data, file, ensure_ascii=False, indent=4) # Write the student_data into students.json
        print("Data saved to 'students.json'.")
    except Exception as e:
        print(f"Error saving data: {e}")

# Save grades to a TXT file
def save_to_txt(students):
    with open("students.txt", "a", encoding="utf-8") as file:
        for student in students:
            file.write(f"Student: {student['first_name']} {student['last_name']} (ID: {student['student_id']})\n")
            file.write(f"Math score: {student['math_score']} Grade: {student['grade_math']}\n")
            file.write(f"Science score: {student['science_score']} Grade: {student['grade_science']}\n")
            file.write(f"Art score: {student['art_score']} Grade: {student['grade_art']}\n")
            file.write("-" * 40 + "\n")
    print("Grades saved to 'students.txt'.")

# Display all students' data in the terminal
def display_students(students):
    print("\nStudent Data:")
    for student in students:
        print(f"\nStudent: {student['first_name']} {student['last_name']} (ID: {student['student_id']})")
        print(f"Math score: {student['math_score']} Grade: {student['grade_math']}")
        print(f"Science score: {student['science_score']} Grade: {student['grade_science']}")
        print(f"Art score: {student['art_score']} Grade: {student['grade_art']}")

# Main function
def main(): # Define main()
    students = get_student_data()  # Get student data
    save_to_json(students)         # Save to existing JSON file
    save_to_txt(students)          # Save to TXT file
    display_students(students)     # Display data in the terminal

# Run the program
if __name__ == "__main__":
    main()
