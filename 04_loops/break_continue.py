# Some chai flavors are out of stock.
# You want to skip those and stop entirely if someone 
# requests a restricted flavor.
# Task: 
# Skip if flavor is "Out of Stock"
# Break if flavor "Discontinued"
flavors = ["Masala", "Ginger", "Out of Stock", "Cardamom", "Discontinued", "Saffron"]
for flavor in flavors:
    if flavor == "Out of stock":
        continue
    if flavor == "Discontinued":
        break
    print("Serving " + flavor + " chai") 