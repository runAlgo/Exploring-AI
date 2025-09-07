essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "black pepper", "ginger", "leman"}

all_spices = essential_spices | optional_spices

print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

only_essential_spices = essential_spices - common_spices
print(f"Only essential spices: {only_essential_spices}")

print(f"Is 'ginger' in essential spices? {'ginger' in essential_spices}")