# You're building a simple app that registers users.
# You want to seperate concerns: getting input, validating it,
# and saving it.
# Task:-
# Write register_user() that calls:
# get_user_input()
# validate_input()
# save_to_db()

def get_user_input():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    return name, email

def validate_input():
    print("Validating user input")

def save_to_db():
    print("Saving to database")


def register_user():
    get_user_input()
    validate_input()
    save_to_db()
