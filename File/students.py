

# students = []
# with open("student.csv") as file:
#     for line in file:
#         name, title = line.rstrip().split(",")
#         student = {"name": name, "title": title}
#         # student["names"] = name
#         # student["title"] = title
#         students.append(student)
# # def get_name(student):
# #     return student["title"]
# # for student in sorted(students, key = get_name):
# for student in sorted(students, key = lambda student: student['name']):
#     print(f"{student['name']}{student['title']}")

# with open("student.csv") as file:
#     for line in file:
#         name, title = line.rstrip().split(",")
#         print(f"{name},{title}")