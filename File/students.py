import csv
name = input("What's your name? ")
home = input("What's your home? ")
with open("/home/anya/C_CODE/CS50-py/File/student.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow({"name": name, "home": home})

# students = []
# with open("/home/anya/C_CODE/CS50-py/File/student.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({
#             "name": row["name"].strip(),
#             "home": row["home"].strip()
#         })
# for student in sorted(students, key=lambda s: s["name"]):
#     print(f"{student['name']} is from {student['home']}")

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