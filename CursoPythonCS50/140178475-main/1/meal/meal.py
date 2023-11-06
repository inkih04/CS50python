def main():
    time = input("What time is it? ")
    time = convert(time)
    # 7 <= time <= 8
    if 7<= time <= 8:
        print("breakfast time", end = "")
    #12 <= time <= 13
    elif 12 <= time <= 13:
        print("lunch time", end = "")
    elif 18 <= time <= 19:
        print("dinner time", end = "")


def convert(time):
    ltime = time.split(":")
    time = float(int(ltime[0]) + int(ltime[1])/60)
    return time


if __name__ == "__main__":
    main()