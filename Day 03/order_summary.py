order_fruits = ["apple", "banana", "cherry", "date"]
order_summary = [34, 56, 78,43]

for names, order in zip(order_fruits, order_summary):
    print(f"summary {order}: {names}")