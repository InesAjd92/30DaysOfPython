### Day 2 : Variables, Built-in functions ###

## Exercises ##

# Level 1 : 

# 1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py

# 2. Write a python comment saying 'Day 2: 30 Days of python programming'

# Day 2: 30 Days of python programming

# 3-13. Declare first name, last name, full name, country, city, age, year, is_married, is_true, is_light_on and multiple variables, and assign values to them. 

first_name = "Ines"
last_name = "Amdj"
full_name ="Inesamdj"
country = "France"
city = "Colombes"
age = 25
year = 2026
is_married = False
is_true = True
is_light_on = True
have_boyfriend, his_name, his_age = True, "FakeName", 26

# Level 2 : 

# 1. Check the data type of all your variables using type() built-in function

print("first_name:", type(first_name))
print("last_name:", type(last_name))
print("full_name:", type(full_name))
print("country:", type(country))
print("city:", type(city))
print("age:", type(age))
print("year:", type(year))
print("is_married:", type(is_married))
print("is_true:", type(is_true))
print("is_light_on:", type(is_light_on))
print("have_boyfriend:", type(have_boyfriend))
print("his_name:", type(his_name))
print("his_age:", type(his_age))

# 2. Using the len() built-in function, find the length of your first name

print(len(first_name)) 

# 3. Compare the length of your first name and your last name

print(len(first_name),len(last_name)) 

# 4. Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4

# 5. Add num_one and num_two and assign the value to a variable total

total = sum([num_one, num_two]) # don't forget the []
print(total)

# 6. Subtract num_two from num_one and assign the value to a variable diff

diff = num_two - num_one
print(diff)

# 7. Multiply num_two and num_one and assign the value to a variable product

product = num_two * num_one
print(product)

# 8. Multiply num_two and num_one and assign the value to a variable product

division = num_one / num_two
print(division)

# 9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder

remainder = num_two % num_one
print(remainder)

# 10. Calculate num_one to the power of num_two and assign the value to a variable exp

exp = num_one**num_two
print(exp)

# 11. Find floor division of num_one by num_two and assign the value to a variable floor_division

floor_division = num_one // num_two
print(floor_division)

# 12. The radius of a circle is 30 meters

# i/ Calculate the area of a circle and assign the value to a variable name of area_of_circle

# Here is the forumula : 
# aera = pi * radius ** 2

pi = 3.1416
radius = float(input("What is the radius: "))

area_of_circle = pi * (radius**2)
print(area_of_circle)

# ii/ Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

# The formula is :
# 2 * pi * radius

circum_of_circle = 2*pi*radius
print(circum_of_circle)

# iii. Take radius as user input and calculate the area.

radius = float(input("What is the radius (m): "))
area_of_circle = pi * (radius**2)
print("The area of the circle is:", area_of_circle, "m²")

# 13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

first_name = input("What is your name?")
last_name = input("And your last name?")
country = input("What is your country?")
age = input("How old are you?")

print("My name is", 
first_name, last_name,",I am", age,"and I live in", country)

# 14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

help('keywords')