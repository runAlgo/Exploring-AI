# value = 13
# reminder = value % 3

# if reminder:
#     print(f"reminder value is {reminder}")


# value = 13

# if reminder := value % 3:  # Using the walrus operator to assign and check in one line
#     print(f"reminder value is {reminder}")

# available_flavors = ["masala", "ginger", "tulsi", "cardamom", "saffron"]

# if (requested_flavors := input("Enter the flavors you want: ")) in available_flavors:
#     print(f"Preparing chai with {requested_flavors} flavor.")
# else:
#     print(f"Sorry, we don't have {requested_flavors} flavor.")



flavors = ["masala", "ginger", "tulsi", "cardamom", "saffron"]
print("Available flavors: ", flavors)

while (requrested_flavor := input("Enter the flavor you want: ")) not in flavors:
    print(f"Sorry, we don't have {requrested_flavor} flavor. Please choose from the available flavors.")
print(f"You choose {requrested_flavor} flavor.")
