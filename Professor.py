import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level)
        correct_answer = x + y
        attempts = 0

        while attempts < 3:
            user_answer = input(f"{x} + {y} = ")

            if user_answer.isdigit():
                user_answer = int(user_answer)

                if user_answer == correct_answer:
                    score += 1
                    print("Correct!")
                    break
                else:
                    attempts += 1
                    if attempts < 3:
                        print("EEE")
                    else:
                        print(f"{x} + {y} = {correct_answer}")
            else:
                print("EEE")

    print(f"{score}")

def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)
        else:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y

if __name__ == "__main__":
    main()
