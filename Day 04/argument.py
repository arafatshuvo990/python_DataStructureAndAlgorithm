def user_info(**kwargs):
    for key, values in kwargs.items():
        print(f"{key}:{values}")
user_info(name='Arafat', Role='Software Engineer')

def total(price, *extras):
    print("Price:", price)
    print("Extras:", extras)

total(100, 10, 20, 30)

def optional(*args, **kwargs):
    print(f"Sum of args {sum(args)}")
    print(kwargs)

optional(1,2,100,3,4,new=5,old=6)