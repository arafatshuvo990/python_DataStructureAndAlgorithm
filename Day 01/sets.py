basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
vegetables = {'carrot', 'potato', 'cabbage', 'lettuce'}
print(basket)
basket.add('grape')
print(basket)
basket.remove('orange')
print(basket | vegetables)
print(basket & vegetables)
print(basket - vegetables)