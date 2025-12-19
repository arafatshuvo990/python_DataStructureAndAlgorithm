#  tupple is immutable means we can not change the value of tupple once it is created
#  but we can change the reference of tupple to another tupple
my_tupple = (1, 2, 3)
print(f"Initial tupple: {my_tupple}")
print(f"Memory location of initial tupple: {id(my_tupple)}")
my_tupple = (4, 5, 6)
print(f"Updated tupple: {my_tupple}")
print(f"Memory location of updated tupple: {id(my_tupple)}")

#membership test
is_in_tupple = 2 in my_tupple
print(f"Is 2 in tupple? {is_in_tupple}")
is_in_tupple = 5 in my_tupple
print(f"Is 5 in tupple? {is_in_tupple}")