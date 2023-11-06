def main():
    txt = input("Fraction: ")
    prcntg = convert(txt)
    output = gauge(prcntg)
    print(output)


def convert(txt):
    while True:
        if "/" in txt:
            x, y = txt.split("/")
            if not "." in x and not "." in y:
                try:
                    x = int(x)
                    y = int(y)
                except ValueError:
                    raise
                else:
                    try:
                        prcntg = x/y
                    except ZeroDivisionError:
                        raise
                    else:
                        if 0 <= prcntg <= 1:
                            return prcntg
        txt = input("Fraction: ")


def gauge(n):
    if 0 <= n <= 1:
        if n >= 0.99:
            return "F"
        elif n <= 0.01:
            return "E"
        else:
            return (f'{n:.0%}')


if __name__ == "__main__":
    main()