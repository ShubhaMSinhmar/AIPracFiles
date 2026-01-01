# Comprehensions

# List Comprehension

# syntax : [expression for item in iterable if condition]

tea = ["green tea", "hot blue tea", "hot matcha", "cold brew"]

hotStuff = [hot for hot in tea if "hot" in hot]

# print(f"hot stuff are {hotStuff}")


# --------------------------------------------------

# Set Comprehension

# syntax : {expression for item in iterable if condition}

houses = {
    "sector18House" : ['green', 'blue'],
    "sector11House" : ['black', 'blue'],
    "sector12House" : ['white', 'green'],
}

allHouseColors = {color for colorSets in houses.values() for color in colorSets}

# print(allHouseColors)

# --------------------------------------------------

# Dictionary Comprehension

food_items_inr = {"pasta":100, "pizza":150, "salad":85}

food_items_kurk = {food:price /50  for food, price in food_items_inr.items()}

print(food_items_kurk)