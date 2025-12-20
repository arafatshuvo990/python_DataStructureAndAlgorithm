
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"value - {my_dict.values()}")

print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])

my_dict["profession"] = "Engineer"
print("Updated Dictionary:", my_dict)

tel = {'jack': 4505, 'shape': 6782}
tel['steve']= 8902
print(tel)
print(tel.get('steve'))
print(tel.items())
print(tel.keys())
print(tel.values())
print(list(tel))