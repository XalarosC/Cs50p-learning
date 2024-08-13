import sys
import random
from pyfiglet import Figlet

def main():
    available_fonts = Figlet().getFonts()

    if len(sys.argv) == 1:
        font = random.choice(available_fonts) 
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        specified_font = sys.argv[2]
        if specified_font in available_fonts:
            font = specified_font
        else:
            sys.exit(f"Font '{specified_font}' not found. Available fonts are: {', '.join(available_fonts)}")
    else:
        sys.exit("Invalid usage")

    figlet = Figlet(font=font)

    user_input = input("Input: ")


    rendered_text = figlet.renderText(user_input)
    print("Output: ")
    print(rendered_text)

if __name__ == "__main__":
    main()
