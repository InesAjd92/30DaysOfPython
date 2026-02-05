### Day 9 : Conditionals 

# By default, python execut statements from top to bottom, so we have to use conditionals!

# Exercises : 

# Level 1 

# 1/

# si user = or > 18 then, give "you are old enought"
# or "wait"

#age = int(input("Enter your age"))

#if age >= 18: 
#    print("Your are old enough to drive")
#else:
#    print("You need to wait", 18 - age, "years to drive")

# it works but need to check if it was the best method

# 2/ 

""" my_age = int(input("Enter my age:"))
your_age = int(input("Enter your age:"))
difference = abs(your_age - my_age) #need to do abs() bc could returns a neg

if my_age > your_age:
    if difference > 1: 
        print("I am", difference, "years older than you")
    if difference <= 1: 
        print("I am", difference, "year older than you")
else : 
    if difference > 1: 
        print("You are", difference, "years", "older than me")
    if difference <= 1: 
        print("You are", difference, "year older than me") """

# 3/ 

""" a = int(input("Enter number one: "))
b = int(input("Enter number two : "))

if a > b: 
    print(a, "is greater than", b)
elif a < b: 
    print(a, "is smaller than", b)
else : 
    print(a, "is equal to", b) """


# Level 2

# 1/ 

""" grade = int(input("Enter your grade"))

if grade >= 90:
    print("Your grade is A")
elif grade >= 80:
    print("Your grade is B")
elif grade >= 70:
    print("Your grade is C")
elif grade >= 60:
    print("Your grade is D")
else: 
    print("Your grade is F") """

# 2/ 

# month = str(input("Enter a month : "))

""" if month == "September" or "October" or "November":
    print("The season is autumn")
elif month == "December" or "January" or "February":
    print("The season is Winter")
elif month == "March" and "April" and "Mary":
    print("The season is Spring")
else : 
    print("The season is summer") """ # this was wrong

"""
if month in ["September", "October", "November"]: 
    print("The season is autumn")
elif month in ["December", "January", "February"]: 
    print("The season is winter")
elif month in ["March", "April", "May"]:
    print("The season is spring")
else : 
    print("The season is summer") """

# 3/ 

"""fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input("Enter a fruit "))

if fruit in fruits: 
    print("This fruit already exist in the list")
else :
    fruits.append(fruit)
    print(fruits)"""

# 4/ 

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#a  * Check if the person dictionary has skills key, 
# if so print out the middle skill in the skills list.

x = int(len(person.get("skills")))
remainder = x % 2

print(x, remainder)

n = int(len(person.get("skills")))

if "skills" in person: 
    if n % 2 != 0: 
        middle_index = (n-1) // 2
        print("The middle skill is", person['skills'][middle_index])
    else : 
        middle_index1 = n // 2 - 1
        middle_index2 = n // 2 
        print("The middle skills are", middle_index1, "and", middle_index2)
else: 
    print("Person has no skills")


# b/ 
#  * Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill and print out the result.


if "skills" in person :
    if "Python" in person.get("skills"): 
        print("Person has Python skill ")
    else : 
        print("Person does not have Python skill")
else: 
    print("Person has no skills")
    
# c/
 # * If a person skills has only JavaScript and React, print('He is a front end developer'), 
 # if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
 #  if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
 # else print('unknown title') 
 # - for more accurate results more conditions can be nested!

skills = person.get('skills', [])

if set(skills) == {'JavaScript', 'React'}:
    print('He is a front end developer')
elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
    print('He is a backend developer')
elif set(['React', 'Node', 'MongoDB']).issubset(skills):
    print('He is a fullstack developer')
else:
    print('unknown title') 

#i was helped!!! 

# d/  * If the person is married 
# and if he lives in Finland, 
# print the information in the following format:

is_married = person.get("is_married")
country = person.get("country")

first_name = person.get("first_name")
last_name = person.get("last_name")

if is_married == True and "Finland" in country:
    print("He is {}{}. He lives in {} and he is married".format(first_name, last_name, country))