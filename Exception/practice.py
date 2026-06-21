try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")