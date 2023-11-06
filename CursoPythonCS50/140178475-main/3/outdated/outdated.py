months = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12"
}

while True:
    txt = input("Date: ").strip()
    if "/" in txt:
        lis = txt.split("/")
        try:
            if 1 <= int(lis[0]) <= 12 and 1 <= int(lis[1]) <= 30:
                print(f"{lis[2]}-{lis[0].zfill(2)}-{lis[1].zfill(2)}")
                break
        except ValueError:
            pass
    elif "," in txt:
        txt = txt.replace(",", "")
        lis = txt.split(" ")
        if lis[0] in months and len(lis) == 3 and 1 <= int(lis[1]) <= 30:
            print(f"{lis[2]}-{months[lis[0]].zfill(2)}-{lis[1].zfill(2)}")
            break
