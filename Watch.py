import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if search := re.search(r'(https?://(www\.)?youtube\.com/)embed/([a-zA-Z0-9]+)"></iframe>', s):
        return (f"https://youtu.be/" + search.group(3))
    else:
        return None




if __name__ == "__main__":
    main()
