def main():
    
    answer = input("What time is it? ")

    time = convert(answer)

    if time >= 7 and time <= 8:
        print("Breakfast Time")
    if time >= 12 and time <= 13:
         print("Lunch time")
    if time >= 18 and time <= 19:
         print("Dinner Time")


def convert(time):
    h, m = time.split(":")
    m1 = float(m) / 60
    return float(h) + m1



if __name__ == "__main__":
    main()
