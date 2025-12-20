order_fruits = ["apple", "banana", "cherry", "date"]

for fruit in order_fruits:
    print(f"Order ready for {fruit}")
    
#enumurate
for id, items in enumerate(order_fruits, start=1):
    print(f"{id} :- {items} here")
    