# How to create a dictionary
school ={
    "name":"Vinay Singh Chauhan",
    "teacher" :"ji sir",
    "subject" : "mathematics",
    "credit" : 4.5
}
# How to display or print a dictionary
print(school)
#How to access a dictionary
print(school["teacher"])
print(school["name"])
print(school["subject"])
print(school["credit"])

# how to add item in a dictionary
school["courseCode"] = "UCS001"
school["fee"] = 100000

print(school)

#how to remove itemfrom dictionary
print(school.pop("name"))
print(school.popitem())
print(school)

#how to create an empty dictionary
emptyDictionary = {}
print(emptyDictionary)

#how to copy a dictionary to another dictionary
emptyDictionary=school.copy()
print(emptyDictionary)

#how to edit a dictionary
emptyDictionary["credit"] = "5"
print(emptyDictionary)
print(school)

# how to clear a dictionary
# emptyDictionary = {}
emptyDictionary.clear()
print(emptyDictionary)

#how to loop a dictionary
for item in school :
    print(item)
    print(school[item],"\n")