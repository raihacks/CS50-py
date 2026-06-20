# x = float(input("What's x?"))
# y = float(input("What's y?"))
# z = x/y
# print(f"{z:.2f}")

def main():
    x = float(input("What's x?"))
    print("x squared is", square(x))

def square(n):
    return n * n # n ** 2 or pow(n, 2)

if __name__ == "__main__":
    main()

'''
int(x) or int(input("What's x?")) is converting the str to int
float
'''

# age = input("Enter your age: ")
# print("You entered:", age)
