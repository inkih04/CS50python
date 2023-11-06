
while True:
    txt = input("Fraction: ")
    if "/" in txt:
        x, y = txt.split("/")
        if not "." in x and not "." in y:
            try:
                x = int(x)
                y = int(y)
            except ValueError:
                pass
            else:
                try:
                    n = x/y
                except ZeroDivisionError:
                    pass
                else:
                     if 0 <= n <= 1:
                        if n >= 0.99:
                            print("F", end = "")
                        elif n <= 0.01:
                            print("E", end = "")
                        else:
                            print(f'{n:.0%}')
                        break