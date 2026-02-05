### Day 1 : Introduction ###

## Exercises ## 

# Level 1 : 

# The exercises were done on the interactive shell. 

# Level 2 :

# 1. Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

# The operands are 3 and 4. 

print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

print("Ines")
print("Amdj")
print("France")
print("I am enjoying 30 days of python")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))

print(type(['Asanabeh', 'Python', 'France']))
print(type('Ines'))
print(type('Amdj'))
print(type('France'))


# Level 3 :

# 1. Write an example for each data type then find an euclidian distance

# a- Examples for each data types 

# Numbers

1 #integer
1.1 #float
3j-12 #complex

# String

"My name is Ines!"
["Ines", "France", 12] #list
{12.2, 11} #set (order is not important)
("Asanabeh", "Pawel", "Brook") #tuple (can't be modified once created)
{"first_name": "Ines"} #dictionary

# How to find an euclidian distance ? 

# Formula : 
# x2-x1 = 10-2 = 8
# y2-y1 = 8-3 = 5

# Then, I square each result. 
# 8² = 64
# 5² = 25
# 64+25 = 89
# Then, I calculate the square root. 

# Let's do it with Python. 

eucl_distance = ((10-2)**2 + (8-3)**2)**0.5 # "**2" means "squared","**0.5" means square root
print(eucl_distance)


