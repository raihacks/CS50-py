import random

def main():
    level = get_level()
    result = generate_integer(level)
    print(result)


def get_level():
    while True:
        level = int(input("Level: "))
        if 1 <= level <= 3:
            break
        else:
            raise ValueError
    return level


def generate_integer(level):
    score = 0
    def get_result(x , y, score):
        for _ in range(0, 3):
            result = int(input(f"{x} + {y} = "))
            if result == x + y:
                score += 1
                break
            else:
                print("EEE")
            print(f"{x} + {y} = {x + y}")


    for _ in range(1, 10):
        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
            get_result(x , y, score)
        elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
            get_result(x , y, score)
        else:
            x = random.randint(100,999)
            y = random.randint(100,999)
            get_result(x , y, score)
    
    print(f"Score: {score}")


if __name__ == "__main__":
    main()
