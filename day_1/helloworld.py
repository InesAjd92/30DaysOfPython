# Exercices - Day 1 

### Ex 1
# Dont' forget to use print()

print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)


### Ex 2 

print("Ines")
print("Amdj")
print("France")
print("I am enjoying 30 days of python")

### Ex 3 

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asanabeh', 'Python', 'France']))
print(type('Ines'))
print(type('Amdj'))
print(type('France'))


# Exercice Level 3 
#Write an example for each data type then find an euclidian distance

# a- Examples for each data types 

#Number
1
1.1
3j-12

#String

"My name is Ines!"
["Ines", "France", 12] #list
{12.2, 11} #set, order is not important
("Asanabeh", "Pawel", "Brook") #tuple, cant be modified once created

{"first_name": "Ines"} #dictionary

#Euclidian distance

# formula : x2-x1 = 10-2 = 8
# y2-y1 = 8-3 = 5

#Then we put each result au carré
# 8² = 64
# 5² = 25
# 64+25 = 89
# Then on calcule la racine au carré 

# Let's do simply with Python

eucl_distance = ((10-2)**2 + (8-3)**2)**0.5 # "**2" means "au carré","**0.5" means racince carré
print(eucl_distance)


