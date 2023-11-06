
def main():
    exp = input("Expression: ")
    exp = exp.split()
    x = int(exp[0])
    y = int(exp[2])
    if exp[1] == "+":
        print("{:.1f}".format(add(x, y)))
    elif exp[1] == "-":
        print("{:.1f}".format(sub(x, y)))
    elif exp[1] == "*":
        print("{:.1f}".format( mult(x, y) ))
    else:
        print("{:.1f}".format(div(x, y)))

def add(x, y):
    return float(x + y)


def sub(x, y):
    return float(x - y)


def mult(x, y):
    return float(x*y)


def div(x, y):
    return float(x/y)



main()