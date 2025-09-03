is_boiling = True
stair_count = 5
total_actions = stair_count + is_boiling #upcasting
print(f"Total actions: {total_actions}")


milk_present = 0  # no milk
print(f"Is there milk?: {bool(milk_present)}")


water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Serve if water_hot and tea_added: {can_serve}")