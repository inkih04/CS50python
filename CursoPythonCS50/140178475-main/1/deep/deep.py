answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = answer.strip()
if answer == "42" or answer.lower() == "forty-two" or answer.lower() == "forty two":
    print("Yes", end = "")
else:
    print("No", end = "")
