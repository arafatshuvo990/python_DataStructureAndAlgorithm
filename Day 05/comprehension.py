# list comprehesnsion
order_fruits = ['banana', 'apple', 'orange', 'kiwi', 'mango']

fruits = [my_fruits for my_fruits in order_fruits if len(my_fruits) > 5]
print(fruits)

#sets comprehension
grocery_items = ['apple', 'banana', 'orange', 'kiwi', 'mango', 'apple', 'banana']

grocery_sets = {grocery for grocery in grocery_items if 'apple' not in grocery}
print(grocery_sets)
grocery_sets = {grocery for grocery in grocery_items}
print(sorted(grocery_sets))

#dictionary comprehension
fruits_price = {'banana': 1.5, 'apple': 2.0, 'orange': 1.8, 'kiwi': 3.0, 'mango': 2.5}
discounted_fruits = {fruit: price * 0.9 for fruit, price in fruits_price.items()}
print(discounted_fruits)

#generator comprehension with condition

cricker_runs = [10, 25, 30, 45, 50, 60, 75, 80, 90, 100]

high_scores = sum(run for run in cricker_runs if run > 50)
print(high_scores)
    