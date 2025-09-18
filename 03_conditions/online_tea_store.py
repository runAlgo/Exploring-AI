# You run an online tea store.
# If the order amount is more than $300, delivery is free.
# otherwise, delivery cost $30.

# Task: 
# Input: order_amount
# Use ternary operator to decide delivery cost

order_amount = float(input("Enter the order amount: $"))
delivery_cost = 0 if order_amount > 300 else 30
print(f"Delivery cost: ${delivery_cost}")
print(f"Total amount to be paid: ${order_amount + delivery_cost}")