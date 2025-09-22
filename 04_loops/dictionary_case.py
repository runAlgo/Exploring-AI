users = [
    {"id": 1, "total": 100, "coupen": "CHAI20"},
    {"id": 2, "total": 200, "coupen": "CHAI30"},
    {"id": 3, "total": 300, "coupen": "CHAI50"},
]

discounts = {
    "CHAI20": (0.2, 0),
    "CHAI30": (0.5, 0),
    "CHAI50": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupen"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount {discount}")