### Day 18 : Regular expressions ###

## Exercises ##

# Level 1 : 

# 1. What is the most frequent word in the following paragraph?

import re

# re.match() : only in the biginnin of the first line and returns matched objects
# re.search() : match objects anywhere in the string 
# re.findall() : list containing all matched 
# re.split() : split a the match points and returns a list
# re.sub() : replace one or many matches with a given string

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

frequency = dict()
regex_pattern = r"\b\w+\b" # means matches whole words made up of letters, digits, or underscores,
matches = re.findall(regex_pattern, paragraph)

for word in matches:
    frequency[word] = frequency.get(word, 0) +1

frequent_words = [(count, word) for word, count in frequency.items()] # .items() to have a view of the dic in tuples

print(sorted(frequent_words, reverse=True))

# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

paragraph = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. 
Extract these numbers from this whole text and find the distance between the two furthest particles."""

regex_pattern = r"-?[0-9]+" # means "-" optional and one or more digits between 0 and 9
points = re.findall(regex_pattern, paragraph)
print(points)

points_int = list(map(int, points)) # map(function, iterable) each point will be convert to an integer
print(points_int)

sorted_points = sorted(points_int)
print(sorted_points) # already sorted but nvm

distance = max(sorted_points) - min(sorted_points)
print(f"In the whole text, there is a lot of numbers : {points_int} ! I took the min and the max of the list to find the distance which is {distance}")

# Level 2 : 

# 1. Write a pattern which identifies if a string is a valid python variable

# Rules for a valid Python variable name:
# - Must NOT start with a digit, uppercase letter, or any symbol except underscore (_)
# - The first character can be a lowercase letter (a-z) or underscore (_)
# - Subsequent characters can be lowercase letters (a-z), digits (0-9), or underscores (_)
# - Variable names are case-sensitive
# - Variable names cannot be Python reserved keywords (e.g., for, if, while)

regex_pattern_true = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

def is_valid_variable(var): 
    if re.match(regex_pattern_true, var) is None:
        return False
    else: 
        return True 
    
print(is_valid_variable('first_name'))   # True
print(is_valid_variable('first-name'))   # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))    # True

# Level 3 : 

def clean_text(sentence): 
    regex_pattern = r"[%@$&#;]"
    cleaned_sentence = re.sub(regex_pattern, "", sentence)
    return cleaned_sentence

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
print(clean_text(sentence))

def most_frequent_words(txt): 
    regex_pattern = r"\b\w+\b" # means matches whole words made up of letters, digits, or underscores,
    matches = re.findall(regex_pattern, txt)
    frequency = dict()
    frequent_words = list()
    for word in matches: 
        frequency[word] = frequency.get(word, 0) + 1
    frequent_words = [(count, word) for word, count in frequency.items() if count > 1]
    return sorted(frequent_words, reverse=True)

print(most_frequent_words(clean_text(sentence))) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
