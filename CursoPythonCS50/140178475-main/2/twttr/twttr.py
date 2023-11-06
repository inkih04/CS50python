txt = input("Input: ")
print("Output: ", end = "")
for c in txt:
    x = c.lower()
    if x != "a" and x != "e" and x != "i" and x != "o" and x != "u":
        print(c, end = "")
