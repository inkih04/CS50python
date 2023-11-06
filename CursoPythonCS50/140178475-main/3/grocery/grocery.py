grocery ={}

while True:
    try:
        clave = input().upper()
    except EOFError:
        break
    else:
        if clave in grocery:
            grocery[clave] += 1
        else:
            grocery[clave] = 1
for item in sorted(grocery):
    print(f"{grocery[item]} {item}")