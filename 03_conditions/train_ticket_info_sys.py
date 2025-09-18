# You're building a ticket info system for a railway app.
# Based on seat type, show its features.

# Task:
# 1. Input: "sleeper", "AC", "general", "luxury"
# 2. Match using match-case
# 3. Unknown -> show: "Invalid seat type"

seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()
match seat_type:
    case "sleeper":
        print("Sleeprer: Non-AC, 3-tier berths, affordable")
    case "ac":
        print("AC: Air-conditioned, 2/3-tier berths, confortable")
    case "general":
        print("General: Non-AC, unreserved seating, budget-friendly")
    case "luxury":
        print("Luxury: Premium AC, spacious berths, high-end amenities")
    case _:
        print("Invalid seat type")
