import random
import sys


def main():
    ca = 0
    n = get_level()
    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        for i in range(3):
            try:
                sol = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
            else:
                if sol != (x + y):
                    print("EEE")
                else:
                    ca += 1
                    break
                if i == 2:
                    print(f"{x} + {y}= {(x+y)}")

    print(f"Score: {ca}")

def get_level():
    while True:
        try:
            le = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1 <= le <= 3:
                return int(le)


def generate_integer(level):
    if level == 1:
        n_min = 0
        n_max = 10
    elif level == 2:
        n_min = 10
        n_max = 100
    else:
        n_min = 100
        n_max = 1000
    return random.randrange(n_min ,n_max)


if __name__ == "__main__":
    main()