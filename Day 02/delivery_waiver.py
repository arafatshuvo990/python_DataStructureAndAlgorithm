order_amount = int(input("What is the order amount? "));

deleiver_fee = 0;
if order_amount >= 100 and order_amount < 300:
    deleiver_fee = 50
    print(f"Your delivery fee is {deleiver_fee}")
elif  order_amount >= 300:
    print("You have free delivery")
else:
    deleiver_fee = 10;
    print(f"Your delivery fee is {deleiver_fee}")