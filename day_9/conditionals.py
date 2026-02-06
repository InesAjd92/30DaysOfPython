### Day 9 : Conditionals ###

## Exercises ##

# Level 1 :

# 1. Get user input using input("Enter your age: ").
# If the user is 18 or older, give feedback:
# "You are old enough to drive."
# If below 18, give feedback to wait for the missing amount of years.

age = int(input("Enter your age"))

if age >= 18: 
    print("Your are old enough to drive")
else:
    print("You need to wait", 18 - age, "years to drive")

# 2. Compare the values of my_age and your_age using if … else.
# Who is older (me or you)? Use input("Enter your age: ") to get the age as input.
# Use a nested condition to print 'year' for 1 year difference, 'years' for bigger differences and a custom text if my_age == your_age.

my_age = int(input("Enter my age:"))
your_age = int(input("Enter your age:"))
difference = abs(your_age - my_age) # need to add abs() bc could returns a neg

if my_age > your_age:
    if difference > 1: 
        print("I am", difference, "years older than you")
    if difference <= 1: 
        print("I am", difference, "year older than you")
else : 
    if difference > 1: 
        print("You are", difference, "years", "older than me")
    if difference <= 1: 
        print("You are", difference, "year older than me")

# 3. Get two numbers from the user using input prompt.
# If a is greater than b return "a is greater than b", if a is less than b return "a is smaller than b", else a is equal to b.

a = int(input("Enter number one : "))
b = int(input("Enter number two : "))

if a > b: 
    print(a, "is greater than", b)
elif a < b: 
    print(a, "is smaller than", b)
else : 
    print(a, "is equal to", b)

# Level 2 : 

# 1. Write a code which gives grade to students according to their scores:

grade = int(input("Enter your grade"))

if grade >= 90:
    print("Your grade is A")
elif grade >= 80:
    print("Your grade is B")
elif grade >= 70:
    print("Your grade is C")
elif grade >= 60:
    print("Your grade is D")
else: 
    print("Your grade is F")

# 2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer.

month = str(input("Enter a month : "))

if month in ["September", "October", "November"]: 
    print("The season is autumn")
elif month in ["December", "January", "February"]: 
    print("The season is winter")
elif month in ["March", "April", "May"]:
    print("The season is spring")
else : 
    print("The season is summer")

# 3. The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print 'That fruit already exists in the list'.

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input("Enter a fruit "))

if fruit in fruits: 
    print("This fruit already exist in the list")
else :
    fruits.append(fruit)
    print(fruits)

# Level 3 : 


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

# a/ Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

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


# b/ Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if "skills" in person :
    if "Python" in person.get("skills"): 
        print("Person has Python skill ")
    else : 
        print("Person does not have Python skill")
else: 
    print("Person has no skills")
    
# c. If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!

skills = person.get('skills', [])

if set(skills) == {'JavaScript', 'React'}:
    print('He is a front end developer')
elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
    print('He is a backend developer')
elif set(['React', 'Node', 'MongoDB']).issubset(skills):
    print('He is a fullstack developer')
else:
    print('unknown title') 

# d/ If the person is married and if he lives in Finland, print the information in the following format:

is_married = person.get("is_married")
country = person.get("country")

first_name = person.get("first_name")
last_name = person.get("last_name")

if is_married == True and "Finland" in country:
    print("He is {}{}. He lives in {} and he is married".format(first_name, last_name, country))