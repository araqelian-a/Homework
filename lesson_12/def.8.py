#Find student with highest average score
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
'scores': [8, 8, 9, 9, ],
},
}
def score_list(l):
    total_score = 0
    for i in l:
        total_score += i
    return total_score
def high_average_score(students_info):
     high_average_score = -float("inf")
     top_student = "chka"
     for k, v in students_info.items():
         score = v["scores"]
         total_score = score_list(v["scores"])
         avg_scores = total_score / len(score)
         if avg_scores > high_average_score:
            high_average_score = avg_scores
            top_student = v
     return top_student
print(high_average_score(students_info))
