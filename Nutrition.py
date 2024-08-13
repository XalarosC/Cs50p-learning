fruits = [
    {"Fruit": "Apple", "Calories": "130"},
    {"Fruit": "Avocado", "Calories": "50"},
    {"Fruit": "Banana", "Calories": "110"},
    {"Fruit": "Cantaloupe", "Calories": "50"},
    {"Fruit": "Grapefruit", "Calories": "60"},
    {"Fruit": "Grapes", "Calories": "90"},
    {"Fruit": "Honeydew Melon", "Calories": "50"},
    {"Fruit": "Kiwifruit", "Calories": "90"},
    {"Fruit": "Lemon", "Calories": "15"},
    {"Fruit": "Lime", "Calories": "20"},
    {"Fruit": "Nectarine", "Calories": "60"},
    {"Fruit": "Orange", "Calories": "80"},
    {"Fruit": "Peach", "Calories": "60"},
    {"Fruit": "Pear", "Calories": "100"},
    {"Fruit": "Pineapple", "Calories": "50"},
    {"Fruit": "Plums", "Calories": "70"},
    {"Fruit": "Strawberries", "Calories": "50"},
    {"Fruit": "Sweet Cherries", "Calories": "100"},
    {"Fruit": "Tangerine", "Calories": "50"},
    {"Fruit": "Watermelon", "Calories": "80"}
]

item = input("Item: ")

item = item.lower()

calories = None

for fruit in fruits:
    if fruit["Fruit"].lower() == item:
        calories = fruit["Calories"]
        break

if calories is not None:
    print(calories)
    
