import json

with open('students.json', 'r', encoding="utf-8") as file:
    # Read the contents of the file
    json_string = file.read()

json_object = json.loads(json_string)
count_index = len(json_object)
list_items = []
for i in range(3):
    name = input("Enter your name: ").strip()
    surname = input("Enter your last name: ").strip()
    student_id = input("Enter your student ID: ").strip()
    math_score = int(input("Enter your Mathematics score: "))
    science_score = int(input("Enter your Science score: "))
    art_score = int(input("Enter your Arts score: "))
    count_index += 1
    dict_items = {
        "index": count_index,
        "first_name": name,
        "last_name": surname,
        "student_id": student_id,
        "math_score": math_score,
        "science_score": science_score,
        "art_score": art_score
    }
    print('-'*30)
    json_object.append(dict_items)

for j in range(len(json_object)):
    # Check score Math
    if json_object[j]['math_score'] >= 80 and json_object[j]['math_score'] <= 100:
        json_object[j]['grade_math'] = 'A'
    elif json_object[j]['math_score'] >= 70:
        json_object[j]['grade_math'] = 'B'
    elif json_object[j]['math_score'] >= 60:
        json_object[j]['grade_math'] = 'C'
    elif json_object[j]['math_score'] >= 50:
        json_object[j]['grade_math'] = 'D'
    else:
        json_object[j]['grade_math'] = 'F'
    # Check score Science
    if json_object[j]['science_score'] >= 80 and json_object[j]['science_score'] <= 80:
        json_object[j]['grade_science'] = 'A'
    elif json_object[j]['science_score'] >= 70:
        json_object[j]['grade_science'] = 'B'
    elif json_object[j]['science_score'] >= 60:
        json_object[j]['grade_science'] = 'C'
    elif json_object[j]['science_score'] >= 50:
        json_object[j]['grade_science'] = 'D'
    else:
        json_object[j]['grade_science'] = 'F'
    # Check score Art
    if json_object[j]['art_score'] >= 80 and json_object[j]['art_score'] <= 100:
        json_object[j]['grade_art'] = 'A'
    elif json_object[j]['art_score'] >= 70:
        json_object[j]['grade_art'] = 'B'
    elif json_object[j]['art_score'] >= 60:
        json_object[j]['grade_art'] = 'C'
    elif json_object[j]['art_score'] >= 50:
        json_object[j]['grade_art'] = 'D'
    else:
        json_object[j]['grade_art'] = 'F'

with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_object, json_file, ensure_ascii=False, indent=4)