### Day 6 : Tuples ###

## Exercises ##

# Level 1 : 

# 1. Create an empty tuple

tpl = ()

# or tpl = tuple()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

sisters = ("Sarah", "Sofia", "Warda")
brothers = ("Gibril", "Karim")

# 3. Join brothers and sisters tuples and assign it to siblings

siblings = sisters + brothers
print(siblings)

# 4. How many siblings do you have?

print(" I have :", len(siblings),"siblings")

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

# option 1

family_numbers = list(siblings)
family_numbers.append("Rabiaa")
family_numbers.append("Farid")

print(family_numbers)

# option 2 

family_numbers = siblings + ("Rabiaa", "Farid")
print(family_numbers) # easy

# Level 2 :

# 1. Unpack siblings and parents from family_members

siblings = family_numbers [0:5] 
print(siblings)

parents = family_numbers [5:]
print(parents)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ("banana", "mango", "cherry", "strawberry")
vegetables = ("carrot", "onion", "potato")
animal_products = ("milk", "cheese", "butter", "yogurt", "eggs", "honey", "meat", "fish")

food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

n = len(food_stuff_lt)

if n % 2 == 0:
    middle_index1 = (n // 2) - 1
    middle_index2 = n // 2 
    print(middle_index1, middle_index2)
else : 
    middle_index = (n - 1) // 2 
    print("The middle index is", middle_index)

# 5. Slice out the first three items and the last three items from food_stuff_lt list

first_three = food_stuff_lt[0:4]
print(first_three)

print(len(food_stuff_lt))

last_three = food_stuff_lt[-4:]
print(last_three)

# 6. Delete the food_stuff_tp tuple completely

del food_stuff_tp

# 7. Check if an item exists in tuple:

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia is an Nordic country","Estonia" in nordic_countries)

print("Iceland is an Nordic country","Iceland" in nordic_countries)