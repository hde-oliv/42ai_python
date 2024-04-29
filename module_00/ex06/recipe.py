cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10,
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    },
}


def print_recipe_names():
    [print(recipe) for recipe in cookbook]


def print_recipe_details(recipe: str):
    print(cookbook[recipe])


def delete_recipe(recipe: str):
    del cookbook[recipe]


def add_recipe():
    name = input("Enter a name:\n")

    ingredients = []
    while True:
        print("Enter ingredients:")
        ingredient = input("\n")
        if ingredient is None:
            break
        ingredients.append(ingredient)

    meal = input("Enter a meal type:\n")
    prep_time = input("Enter a preparation time:\n")

    cookbook[name] = {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}


def option_handler():
    pass


def main():
    print("Welcome to the Python Cookbook !")
    print("List of available option:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")

    op = input("\nPlease select an option:\n")


if __name__ == "__main__":
    main()
