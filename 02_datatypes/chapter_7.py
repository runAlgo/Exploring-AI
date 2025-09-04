masla_spices = ("cardamom", "cloves", "ginger")
(spice1, spice2, spice3) = masla_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2, 1
print(f"{ginger_ratio}, {cadramom_ratio}")

ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"{ginger_ratio}, {cadramom_ratio}")

#membership
print(f"Is ginger is in Masala spices? {'ginger' in masla_spices}")