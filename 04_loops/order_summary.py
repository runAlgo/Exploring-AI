# You're preparing an order summary with customer names 
# and their total bill amount.
# Task:
# Use two lists: one for names and one for bills.
# Print: "[Name] paid Rs.[amount]"
names = ["Alice", "Bob", "Charlie", "David"]
bills = [250, 300, 150, 400]

for name, amount in zip(names, bills):
    print(f"{name} paid Rs.{amount}")