import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    adress = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"
    if re.search(r'^' + adress + r'\.' + adress + r'\.' + adress + r'\.' + adress + r'$', ip):
        return True
    else:
        return False




if __name__ == "__main__":
    main()
