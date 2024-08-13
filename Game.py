import random

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            pass
        else:
            break
    except ValueError:
        pass

target_number = random.randint(1, level)


while True:
    try:
        guess = int(input("Guess: "))

        if guess < target_number:
            print("Too small!")
        elif guess > target_number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
