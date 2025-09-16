# A tea stall offers different prices for different cup sizes.
# Write a program that calculates the price based on size.
# Task:
# -- Input: "small", "medium", "large"
# -- Small -> RS.10, Medium -> Rs.15, Large -> Rs.20
# -- If invalid: show "Unknown cup size"

choice = input("Enter your choice: (small/ medium/ large): ").lower()
print(f"Your choice is: {choice}")

if choice == "small":
    print(f"Price of small cup: Rs.10")
elif choice == "medium":
    print(f"Price of medium cup: Rs.15")
elif choice == "large":
    print(f"Price of large cup: Rs.20")
else:
    print("Invalid cup size")