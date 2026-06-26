# re.search(pattern, string, flags = 0)
'''
    .      any character except a newline
    *      0 or more repetitions
    +      1 or more repetitions
    ?      0 or 1 repetition
    {m}    m repetitions
    {m, n} m-n repetitions
    ^      matches the start of the string
    $      matches the end of the string on just before the newline at the end of the string
    [^]    complementing the set
    [ ]    set of characters
    A|B    either A or B
    (...)  a group
    (?:...)non-capturing version
    \d     decimal digit
    \D     not a decimal
    \s     whitespace characters
    \S     word characters as well as number and the underscore
    \w not a word character 
'''
import re

email = input("What's your email? ").strip()
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

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

