def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check the length 
    if len(s) < 2 or len(s) > 6:
        return False

    # Check the first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    i = 0
    while i < len(s):
        # Check that the first non-alphabetical character is not '0'
        if not s[i].isalpha():
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    # Check that numbers only appear at the end of the plate
    for c in s[i:]:
        if not c.isdigit():
            return False

    # Check for periods, spaces, or punctuation marks
    for c in s:
        if c in [".", "!", " ", "?"]:
            return False

    return True

main()
