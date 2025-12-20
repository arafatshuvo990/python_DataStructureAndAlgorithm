tea_orders = input(("What is your order size: "))

if tea_orders == "small":
    print(f"You order is {tea_orders} and your price is 10")
elif tea_orders == "medium":
    print(f"You order is {tea_orders} and your price is 15")
elif tea_orders == "large":
    print(f"You order is {tea_orders} and your price is 20")
else:
    print(f"Having nothing")
    

