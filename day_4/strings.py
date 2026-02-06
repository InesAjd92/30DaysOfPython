### Day 4 : Strings ###

## Exercises ##

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

challenge = ["Thirty", "Days", "Of", "Python"]
result = " ".join(challenge) # join with a space
print(result)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

challenge = ["Coding", "For", "All"]
result = " ".join(challenge)
print(result)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# 4. Print the variable company using print().

print(company)

# 5. Print the length of the company string using len() method and print().

print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.

print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.

print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.

print(company.split()[0])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.index("Coding")) # gives the index
print("Coding" in company) # better

# 11. Replace the word coding in the string 'Coding For All' to Python.

print(company.replace("Coding", "Python")) 

# 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.

challenge = "Python For Everyone"
print(challenge)
result = challenge.replace("Everyone", "All")
print(result)

# 13. Split the string 'Coding For All' using space as the separator (split()) .

print(company.split(" "))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

challenge = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
result = challenge.split(",")

print(result)

# 15. What is the character at index 0 in the string Coding For All.

print(company[0]) # not using index here because index will give me a number

# 16. What is the last index of the string Coding For All.


lenght_company = (len(company))
print(int(lenght_company))

last_index = lenght_company - 1
print(last_index) 

# 17. What character is at index 10 in "Coding For All" string.

print(company[10]) # the space

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.

challenge = "Python For All"
acronym = challenge[0] + challenge[7] + challenge[11]
print(acronym.upper())

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.

challenge = "Coding for All"
acronym = challenge[0] + challenge [7] + challenge [11]
print(acronym)

# 20. Use index to determine the position of the first occurrence of C in Coding For All.

substring = "C"
result = company.index(substring)
print(result) # position 0, so first letter

# 21. Use index to determine the position of the first occurrence of F in Coding For All.

substring = "F"
result = company.index(substring)
print(result) # the first occurence is at 7

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.

challenge = "Coding For All People"
result = challenge.rfind("l")
print(result) # last occurence of l

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

challenge = "You cannot end a sentence with because because because is a conjunction"
result = challenge.index("because")
print(result) # the word because appears for the first time at position 31

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

result = challenge.rindex("because")
print(result) # because appears the last time at position 47 of the sentence

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

result = challenge.replace("because", "")
print(result)

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

challenge = "You cannot end a sentence with because because because is a conjunction"
result = challenge.find("because")
print(result) # 31

# 28. Does 'Coding For All' start with a substring Coding?

result = company.startswith("Coding")
print(result) # true 

# 29. Does 'Coding For All' end with a substring coding?

result = company.endswith("Coding")
print(result) # false

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.

challenge = "   Coding For All      "
result = challenge.strip(" ")
print(result)

# 31. Which one of the following variables return True when we use the method isidentifier():

challenge = "30DaysOfPython"
result = challenge.isidentifier()
print(result)

challenge = "thirty_days_of_python"
result = challenge.isidentifier()
print(result) # this one 

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

challenge = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = "# ".join(challenge)
print(result)

# 33. Use the new line escape sequence to separate the following sentences.

challenge = "I am enjoying this challenge. \nI just wonder what is next"
print(challenge)

# 34. Use a tab escape sequence to write the following lines.

challenge ="Name \t Age \t Country \t City \n Asabeneh \t 250 \t Finland \t Helsinki"
print(challenge)

# 35. Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2

formated_string = "The area of a circle with radius {} is {} meters square".format(radius, area)
print(formated_string)


# 36. Make the following using string formatting methods:

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