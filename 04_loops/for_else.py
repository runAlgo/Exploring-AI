staff = [("Amit", 15), ("Sunil", 10), ("Ravi", 5)]

for name, age in staff:
    if age <= 10:
        print(f"{name} is eligible to manage the staff.")
        break
else:
    print("No staff member is eligible to manage the staff.")