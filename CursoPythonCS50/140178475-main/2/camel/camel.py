t = input("camelCase: ")
#print("snake_case: ", end = "")
for c in t:
    if c.isupper():
         print(f"_{c.lower()}", end = "")
    else:
        print(c, end = "")
