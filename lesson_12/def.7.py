#Write a function that takes a dictionary with information about students. Return info
#about the youngest student
students_info = students_info = {
'student1': {
'name': 'John Doe',
'age': 20,
'subjects': ['Math', 'Physics', 'English'],
'scores': [7, 9, 9, 6],
},
'student2': {
'name': 'Jane Smith',
'age': 19,
'subjects': ['Chemistry', 'Biology', 'History'],
'scores': [5, 6, 8, 10],
},
'student3': {
'name': 'Bob Johnson',
'age': 21,
'subjects': ['Computer Science', 'Statistics', 'Psychology'],
'scores': [8, 8, 9, 9, 9],
},
}


def youngest_student(students_info):
    youngest_student = "chka"
    min_age = float("inf")

    for k, v in students_info.items():
        age = v["age"]
        if age < min_age:
            min_age = age
            youngest_student = v
    return youngest_student

print(youngest_student(students_info))
