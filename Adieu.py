names = []

while True:
    try:
        adiue = input("Name: ")
        if adiue:
            names.append(adiue)
    except EOFError:
        print()
        break

if names:
    if len(names) == 1:
        print("Adieu, adieu, to " + names[0])
    elif len(names) == 2:
        print("Adieu, adieu, to " + names[0] + " and " + names[1])
    else:
        names_str = ", ".join(names[:-1]) + ", and " + names[-1]
        print("Adieu, adieu, to " + names_str)
