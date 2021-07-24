# student_heights = [180, 124, 165, 173, 189, 169 , 146]
# totalHeight = 0
# for height in student_heights :
#     totalHeight = totalHeight+height
# numberOfStudent = len(student_heights)
#  averageHeight = int(totalHeight/numberOfStudent)
#print(averageHeight)

studentHeights = input("Enter height of students. \n")
student_heights = studentHeights.split(" ")
#print(student_heights)
totalHeight = 0
for n in range(0 , len(student_heights)) :
    totalHeight = totalHeight+int(student_heights[n])
    #print(n,totalHeight)
numberOfStudent = len(student_heights)
#print(numberOfStudent)
averageHeight = int(totalHeight/numberOfStudent)
print(averageHeight)
