### Day 7 : Sets ###

## Exercises ##

# Level 1 :

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies

print(len(it_companies))
# it_companies is 7

# 2. Add 'Twitter' to it_companies

it_companies.add("Twitter")
print(it_companies)
print(len(it_companies))

# 3. Insert multiple IT companies at once to the set it_companies

# update() for multiple elements 

it_companies.update(["Canva", "Capgemini"])
print(it_companies)

# must be a list to udpate multiple elements

# 4. Remove one of the companies from the set it_companies

it_companies.remove("Capgemini")
print(it_companies)

# 5. What is the difference between remove and discard

#it_companies.remove("Twitter") # KeyError when element doesnt exist
it_companies.discard("Twitter") # does nothing if element doesnt exist
print(it_companies)

# Level 2 : 

# 1. Join A and B

joined_set = a.union(b)
print(joined_set)

# 2. Find A intersection B

print(a.intersection(b)) # return elements in both sets

# 3. Is A subset of B

print(a.issubset(b)) # true

# 4. Are A and B disjoint sets

print(a.isdisjoint(b))
print(b.isdisjoint(a)) # false 

# 5. Join A with B and B with A

print(a.union(b), b.union(a))

# 6. What is the symmetric difference between A and B

print(a.symmetric_difference(b))

# 7. Delete the sets completely

del a, b

# Level 3 :

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?

print(len(age))
age = set(age)
print(len(age), age)

# The list is bigger than the set, because the set only contains unique elements

# 2. Explain the difference between the following data types: string, list, tuple and set

# String =  immutable sequence of characters used to store text.
# List = ordered and mutable collection of elements that can contain duplicates.
# Tuple = An ordered and immutable collection of elements, often used for fixed data.
# Set = An unordered collection of unique elements with no duplicates, used for set operations

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people"
print(sentence)
print(len(sentence))

sentence = sentence.split()
print(sentence)

sentence = set(sentence)
print(sentence)

print(len(sentence)) # 10 unique words 