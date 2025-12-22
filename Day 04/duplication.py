def order_tea(tea_name, quantity):
    print(f"Your Order tea is {tea_name} and quantity is {quantity} cup.")

tea = input("What is your order name? ");
quantity = int(input("How much you want to order? "))

order_tea(tea, quantity)