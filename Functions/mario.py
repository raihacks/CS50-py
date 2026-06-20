def main():
    print_square(10)
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
main()