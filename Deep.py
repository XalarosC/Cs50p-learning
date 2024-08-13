#asking the quetion
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

#restricting the anser + answer
if answer.strip() == "42":
    print("Yes")
elif answer.lower().strip() == "forty two":
    print("Yes")
elif answer.lower().strip() == "forty-two":
    print("Yes")
else:
    print("No")
