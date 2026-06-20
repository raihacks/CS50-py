def main():
    x = get_int("Whats's x? ")
    print(f"x is {x}")

def get_int(promt):
    while True:
        try:
            return int(input(promt))
            # return int(input("Whats's x? "))
            # x=int(input("Whats's x? "))
            # break
        except ValueError:
           # print("x is not an integer!")
           pass
    #return x
        # else:
        #     return x
main()

#ValueError
#NameError