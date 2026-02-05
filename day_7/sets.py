## Day 7 : Sets

# Exercises 

# Level 1

# 1/

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
#it_companies is 7

# 2/ 

it_companies.add("Twitter")
print(it_companies)
print(len(it_companies))

# 3/

#update for multiple elements 

it_companies.update(["Canva", "Capgemini"])
print(it_companies)

# CAUTION !! must be a list to udpate multiple elements


# 4/ 

it_companies.remove("Capgemini")
print(it_companies)

# 5/ 

#it_companies.remove("Twitter") #KeyError when element doesnt exist
it_companies.discard("Twitter") #does nothing if element doesnt exist
print(it_companies)

# Level 2

# 1/

joined_set = a.union(b)
print(joined_set)

# 2/ 

print(a.intersection(b))

#return elements in the both sets

# 3/

print(a.issubset(b)) #true

# 4/ 

print(a.isdisjoint(b))
print(b.isdisjoint(a))

#false 

# 5/

print(a.union(b), b.union(a))

# 6/ 

print(a.symmetric_difference(b))

# 7/

del a, b

# Level 3 

# 1/ 

print(len(age))
age = set(age)
print(len(age), age)

#The list is bigger than the set, because it removes the doublon

# 2/ 

# String =  immutable sequence of characters used to store text.
# List = ordered and mutable collection of elements that can contain duplicates.
# Tuple = An ordered and immutable collection of elements, often used for fixed data.
# Set = An unordered collection of unique elements with no duplicates, used for set operations

# 3/ 

sentence = "I am a teacher and I love to inspire and teach people"
print(sentence)
print(len(sentence))

sentence = sentence.split()
print(sentence)

sentence = set(sentence)
print(sentence)

# just to print len to see hwo much unique word

print(len(sentence)) # 10 unique words 