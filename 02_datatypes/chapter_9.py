ingredients = ["water", "milk", "black_tea"]
ingredients.append("sugar")
ingredients.remove("water")
print(f"Ingredients: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
chai_ingredients.insert(1, "lemon")
print(f"Chai ingredients: {chai_ingredients}")


last_added = chai_ingredients.pop()
print(f"Last added: {last_added}")
print(f"Chai ingredients: {chai_ingredients}")

chai_ingredients.reverse()
print(f"Chai ingredients: {chai_ingredients}")


chai_ingredients.sort()
print(f"Sorted: {chai_ingredients}")

sugar_labels = [1, 2, 3, 4, 5, 6]
print(f"Maximum sugar level: {max(sugar_labels)}")
print(f"Minimum sugar level: {min(sugar_labels)}")