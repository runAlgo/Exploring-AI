# A local cafe wants a program that suggests a snack.
# If a customer asks for cookies or samosa, it confirms
# the order. Otherwise, it says it's not available.

# Task:
# -- Take snack input
# -- If it's "cookies" or "samosa", confirm the order
# -- Else, show unavailability

snack = input("Enter your prefered snack: ").lower()
print(f"User said: {snack}")

if snack == "cookie" or snack == "samosa":
    print("Yes!, it's available!")
else:
    print("No!, it's not available!")