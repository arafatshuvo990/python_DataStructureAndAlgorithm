total_ballons = 100
print(f"Total ballons: {total_ballons}")

selling_ballons = 4
print(f"Selling ballons: {selling_ballons}")

remaining_ballons = total_ballons - selling_ballons
print(f"Remaining ballons: {remaining_ballons}")

## division
ballons_per_child = remaining_ballons / 4
print(f"Ballons per child: {ballons_per_child}")

##floor division
ballons_per_child_floor = remaining_ballons // 4
print(f"Ballons per child (floor division): {ballons_per_child_floor}")

##modulus
leftover_ballons = remaining_ballons % 4
print(f"Leftover ballons: {leftover_ballons}")

##boolean
are_ballons_enough = remaining_ballons >= 20
print(f"Are ballons enough for the party? {are_ballons_enough}")

##exponentiation
double_ballons = 2 ** 3
print(f"Double ballons (2^3): {double_ballons}")

##new variable
fruits_available = 15
print(f"Fruits available: {fruits_available}")
fruits_invited = fruits_available <10
print(f"Are fruits enough for the party? {fruits_invited}")

##updating variable
fruits_available += 5
print(f"Updated fruits available: {fruits_available}")
fruits_invited = fruits_available <10
print(f"Are fruits enough for the party after update? {fruits_invited}")