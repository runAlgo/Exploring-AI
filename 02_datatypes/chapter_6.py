chai_type = "Ginger chai"
customer_name = "Priya"
print(f"Order for {customer_name} : {chai_type} please")

chai_description = "Aromatic and Bold"

print(f"First word: {chai_description[0:8:2]}")
print(f"First word: {chai_description[:8]}")
print(f"First word: {chai_description[12:]}")
print(f"First word: {chai_description[::-1]}")


label_text = "Chai Special kalu"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded text: {label_text}")
print(f"Encoded text: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")