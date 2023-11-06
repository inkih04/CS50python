import inflect
names = []
p = inflect.engine()
txt = "Adieu, adieu, to"
while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
    else:
        names.append(name)
print(txt, p.join(names))


