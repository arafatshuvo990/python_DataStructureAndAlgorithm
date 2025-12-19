#list in python
#list are mutable
#list is a collection of items
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[0])        
print(len(fruits))     
print(fruits)          
fruits.insert(1, "mango")    
fruits.remove("banana")      
fruits.pop()                 
fruits.sort()                
fruits.reverse()             
print(fruits)

sugar_levels = [5, 3, 8, 6, 2]
sugar_levels.sort()
max_sugar = max(sugar_levels)
min_sugar = min(sugar_levels)
print(f"Sorted sugar levels: {sugar_levels}")
print(f"Maximum sugar level: {max_sugar}")
print(f"Minimum sugar level: {min_sugar}")
