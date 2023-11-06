fruits = {
        "banana": "110",
        "strawberries": "50",
        "cantaloupe": "50",
        "grapefruit": "60",
        "watermelon": "80",
        "grapes": "90",
        "sweet cherries": "100",
        "tangerine": "50",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "apple": "130",
        "pineapple": "50",
        "plums": "70",
        "honeydew melon": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "avocado": "50",
}
inp = input("Item: ")
if inp.lower() in fruits:
    print(f"Calories: {fruits[inp.lower()]}")