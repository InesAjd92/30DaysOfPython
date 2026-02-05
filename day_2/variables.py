### Exercices : Day 2

# Level 1 

#Day 2 : 30 days of Python Programming

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

have_boyfriend, his_name, his_age = True, "Karim", 26

# Level 2

#1/ Check the data type of all your variable 

print(len(first_name)) # 2/ find the lenght
print(len(first_name),len(last_name)) # 3/ compare the lenghts of f and l name 

#4/ 

num_one = 5
num_two = 4

#5/
total = sum([num_one, num_two]) # dont forget the []
print(total)

#6/
diff = num_two-num_one
print(diff)

#7/
product = num_two * num_one
print(product)

#8/ 

division = num_one / num_two
print(division)

#9/ with "%"

remainder = num_two % num_one
print(remainder)

#10 / with "**"

exp = num_one**num_two
print(exp)

#11/ floor division with "//"

floor_division = num_one // num_two
print(floor_division)

#12 - radius of a circle == 30m

#i) So, here is the formula 

#aera = pi * radius ** 2

pi = 3.1416
radius = float(input("What is the radius: "))

aera_of_circle = pi * (radius**2)
print(aera_of_circle)

#ii) Find the circumference 

# The formula is == 2*pi*radius

circum_of_circle = 2*pi*radius
print(circum_of_circle)

# iii) take radius as user input and calculate the area

radius = float(input("What is the radius: "))
aera_of_circle = pi * (radius**2)
print("The area of the circle is:", aera_of_circle, "meters")

# 13/ 

first_name = input("What is your name?")
last_name = input("And your last name?")
country = input("What is your country?")
age = input("How old are you?")

print("My name is", first_name, last_name, ",I am", age,"and I live in", country)

# 14/

help('keywords')

#finiiiiiiish :)