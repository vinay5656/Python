student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"
for name in student_scores :
    if student_scores[name]>=91 and student_scores[name]<=100 :
        student_grades[name] = "Outstanding"
    elif student_scores[name]>=81 and student_scores[name]<=90 :
        student_grades[name] = "Exceeds Expectations"
    elif student_scores[name]>=71 and student_scores[name]<=80  :
        student_grades[name] = "Acceptable"
    else : 
        student_grades[name] = "Fail"
 
print(student_grades)