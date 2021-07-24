# studentScore = [56, 78, 46, 89, 91, 61, 98, 33]
# numberOfStudent = len(studentScore)
# print(numberOfStudent)
# maximumScore = max(studentScore)
# print(maximumScore)
# minimumScore = min(studentScore)
# print(minimumScore)

studentScore = input("Enter the scores that students are got")
student_score = studentScore.split(" ")
maxScore = int(student_score[0])
minScore = int(student_score[0])
for score in student_score :
    if maxScore<int(score) :
        maxScore = int(score)
    if minScore>int(score) :
        minScore = int(score)

print("Maximum score is ",maxScore)
print("Minimum score is ",minScore)