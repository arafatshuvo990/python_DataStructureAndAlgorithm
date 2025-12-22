##
# | Scope | Meaning   |
# | ----- | --------- |
# | **L** | Local     |
# | **E** | Enclosing |
# | **G** | Global    |
# | **B** | Built-in  |
##

#non local keyword
def outer():
    x=10
    def inner():
        nonlocal x
        print(x)
    inner()
outer()

## global keyword
locally =  10

def new_outer():
    x= 50
    print(f"outer {x}")
    def new_inner():
        global locally
        print(f"locally inner {locally}")
    new_inner()
new_outer()

## enclosing
def outer():
    x = 5
    def inner():
        print(x)
    inner()

outer()

"""
🧠 PYTHON SCOPE CHEAT SHEET

Situation              Keyword / Scope
--------------------------------------
Read global             none
Modify global           global
Modify enclosing        nonlocal
Function variable       local
"""
"""Read → none | Modify global → global | Modify enclosing → nonlocal | Inside function → local"""
