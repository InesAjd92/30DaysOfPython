### Day 4

# Exercises

# 1/

challenge = ["Thirty", "Days", "Of", "Python"]
result = " ".join(challenge)
print(result)

#ok but dont forget the [], the separator and also how to write the join

# 2/

challenge = ["Coding", "For", "All"]
result = " ".join(challenge)
print(result)

# 3/

company = "Coding For All"

# 4/ 

print(company)

# 5/ 

print(len(company))

# 6/

print(company.upper())

# 7/ 

print(company.lower())

# 8/

print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9/ 

print(company.split()[0])

# 10/

print(company.index("Coding")) # renvoie la position
print("Coding" in company) # better

# 11/

print(company.replace("Coding", "Python")) #bienouéj

# 12/

challenge = "Python For Everyone"
print(challenge)
result = challenge.replace("Everyone", "All")
print(result)

# 13/ 

print(company.split(" "))

# 14/ 

challenge = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
result = challenge.split(",")

print(result)

# 15/ 

print(company[0]) # not using index here because index will give me a number

# 16/

lenght_company = (len(company))
print(int(lenght_company))

last_index = lenght_company - 1
print(last_index)

# 17/

print(company[10]) # the space

# 18/ create an acronym, we can use slice?

challenge = "Python For All"
acronym = challenge[0] + challenge[7] + challenge[11]
print(acronym.upper())

# i needed help a little

# 19/ 

challenge = "Coding for All"
acronym = challenge[0] + challenge [7] + challenge [11]
print(acronym)

# 20/ 

substring = "C"
result = company.index(substring)
print(result) #position 0 so first letter

# 21/
substring = "F"
result = company.index(substring)
print(result) #7

# 22/ 

challenge = "Coding For All People"
result = challenge.rfind("l")
print(result) # last occurence of l

# 23/ 

challenge = "You cannot end a sentence with because because because is a conjunction"
result = challenge.index("because")
print(result) # the word because appears for the first time at position 31

# 24/

result = challenge.rindex("because")
print(result) # because appears the last time at position 47 of the sentence

# 25/

result = challenge.replace("because", "")
print(result)

#helped

# 26/

challenge = "You cannot end a sentence with because because because is a conjunction"
result = challenge.find("because")
print(result)

# 28/

result = company.startswith("Coding")
print(result)

# 29/

result = company.endswith("Coding")
print(result)

# 30/ 

challenge = "   Coding For All      "
result = challenge.strip(" ")
print(result)

# 31/ 


challenge = "30DaysOfPython"
result = challenge.isidentifier()
print(result)

challenge = "thirty_days_of_python"
result = challenge.isidentifier()
print(result)

# 32/ 

challenge = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = "# ".join(challenge)
print(result)
#this is a little bit different than the others methods

# 33 / 

challenge = "I am enjoying this challenge. \nI just wonder what is next"
print(challenge)

# 34 / 

challenge ="Name \t Age \t Country \t City \n Asabeneh \t 250 \t Finland \t Helsinki"
print(challenge)

# 35 /

radius = 10
area = 3.14 * radius ** 2

formated_string = "The area of a circle with radius {} is {} meters square".format(radius, area)
print(formated_string)


# 36 / 

a = 8
b = 6

formated_string = "{} + {} = {}".format(a, b, a + b)
print(formated_string)

formated_string = "{} - {} = {}".format(a, b, a - b)
print(formated_string)

formated_string = "{} * {} = {}".format(a, b, a * b)
print(formated_string)

formated_string = "{} / {} = {}".format(a, b, a / b)
print(formated_string)

formated_string = "{} % {} = {}".format(a, b, a % b)
print(formated_string)

formated_string = "{} // {} = {}".format(a, b, a // b)
print(formated_string)

formated_string = "{} ** {} = {}".format(a, b, a ** b)
print(formated_string)

#fiouuuuu it was looong