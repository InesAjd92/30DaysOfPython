### DAY 6 : Exercises

# Level 1 :

# 1/ 

tpl = ()
# or 
# tpl = tuple()

# 2/ 

sisters = ("Sarah", "Sofia", "Warda")
brothers = ("Gibril", "Karim")

# 3/ 

siblings = sisters + brothers
print(siblings)

# 4/ 

print(" I have :", len(siblings),"siblings")

# 5/ 

#option 1

family_numbers = list(siblings)
family_numbers.append("Rabiaa")
family_numbers.append("Farid")

print(family_numbers)

#option 2 

family_numbers = siblings + ("Rabiaa", "Farid")
print(family_numbers) # more easy


# Level 2

# 1/ 

siblings = family_numbers [0:5] 
print(siblings)

parents = family_numbers [5:]
print(parents)


# 2/ 

fruits = ("banana", "mango", "cherry", "strawberry")
vegetables = ("carrot", "onion", "potato")
animal_products = ("milk", "cheese", "butter", "yogurt", "eggs", "honey", "meat", "fish")

food_stuff_tp = fruits + vegetables + animal_products

# 3/ 

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4/ 

n = len(food_stuff_lt)

if n % 2 == 0:
    print("The nb of element in the list is pair")
    middle_index1 = (n // 2) - 1
    middle_index2 = n // 2 
    print(middle_index1, middle_index2)
else : 
    print("The number of elements in the list is unpair")
    middle_index = (n - 1) // 2 
    print("The middle index is", middle_index)

# 5/


first_three = food_stuff_lt[0:4]
print(first_three)

print(len(food_stuff_lt))

last_three = food_stuff_lt[-4:]
print(last_three)

# 6/ 

del food_stuff_tp

# 7/ 

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia is an Nordic country","Estonia" in nordic_countries)

print("Iceland is an Nordic country","Iceland" in nordic_countries)

#it was so easy today!!! :)