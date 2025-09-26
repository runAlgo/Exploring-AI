# You're creating a monthly report for a cafe's sales.
# Instead of putting all logic in one place, break it down.
# Task:-
# Write a function generate_report() that calls:
# fetch_sales()
# filter_valid_orders()
# summarize_sales()

def fetch_sales():
    print("Fetching sales data...")

def filter_valid_orders():
    print("Filtering valid orders...")

def summarize_sales():
    print("Summarizing sales data...")

def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_sales()
    print("Report generated.")
generate_report()