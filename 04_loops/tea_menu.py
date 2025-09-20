# You're creating a tea menu board.
# Each item must be numbered.
# Task: 
# Use enumerate() to print menu items with their numbers.

menu_items = ["Green Tea", "Black Tea", "Oolong Tea", "Herbal Tea", "Chai"]

for index, item in enumerate(menu_items, start=1):
    print(f"{index}. {item}")