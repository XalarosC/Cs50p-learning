import re

def main():
    print(count(input("Text: ")))



def count(s):
    find = "(^|\\W)um($|\\W)"
    match = re.findall(find, s, re.IGNORECASE)
    if match:
        return(len(match))





if __name__ == "__main__":
    main()
