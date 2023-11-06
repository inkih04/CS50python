
total = 0
while total < 50:
    print(f"Amount Due: {50 - total}")
    inp = int(input("Insert Coin: "))
    if inp == 25 or inp == 5 or inp == 10:
        total += inp
change = total - 50
print(f"Change Owed: {change}")