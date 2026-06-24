import re
# email = input("What's your email? ").strip()
# username, domain = email.split("@")
# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# txt = "The rain in Spain"
# x = re.search("\s", txt)
# print("The first white-space character is located in position:", x.start())

email = input("What's your email? ").strip()
if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
