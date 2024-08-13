while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if not (isinstance(x, int) and isinstance(y, int)) or x > y or y == 0:
            raise ValueError

        percentage = (x / y) * 100

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{round(percentage)}%")

        break

    except (ValueError, ZeroDivisionError):
        pass
