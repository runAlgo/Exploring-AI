# Your shop adds a 10% VAT on every order.
# You wnat this to be consistent and traceable.
# Task:
# Write add_vat(price, vat_rate)
# Use it to compute final prices for 3 orders

def add_vat(price, vat_rate):
    return price + (price * vat_rate / 100)

orders = [100, 150, 200]

for price in orders:
    result = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {result}")
    