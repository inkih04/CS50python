text = input("Greeting: ")
if "Hello" in text:
    print("$0", end = "")
elif text[0] == "H":
    print("$20")
else:
    print("$100")
