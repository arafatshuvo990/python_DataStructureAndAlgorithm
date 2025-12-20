customer_order = input(("what is your order please?")).lower()
if customer_order == "cookies" or customer_order == "samosa":
    print("Your order has been confirmed")
else:
    print("Please order something that is in our menu")
print(customer_order)