# Create a tuple of student names and their corresponding scores. Write a function to find
#the student with the highest score
def get_high_score(students_score):
     high_score = 0
     student = ""
     for name, score in students_score:
         if score > high_score:
             high_score = score
             student = name
     return f"student is {student} score is {high_score}"


students_info = (
    ("Arsen", 78),
    ("Armen", 84),
    ("Karen", 47)
)

print(get_high_score(students_info))


