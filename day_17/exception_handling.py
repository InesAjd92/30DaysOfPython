### Day 17 : Exception handling ###

## Exercises ##

# 1. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

*nordic_countries, es, ru = names 

print(nordic_countries)
print(es, ru)

## Others exercises given by Ecosia ## 

# 1. Create a function 'sum_numbers' that takes a variable number of arguments and returns their sum.

def sum_numbers(*args):
    return sum(*args)

numbers = [1,2,4,9,9]

print(sum_numbers(numbers))

# 2. Create a function 'greeting' that takes variable keyword arguments and prints each key and value.

def greeting(**kwargs):
    for key in kwargs: 
        print(f"My {key} is {kwargs[key]}")

greeting(name = "Ines", age = 25)

# 3. Write a function 'print_info(name, age, city)' that prints these details.
# Call it by unpacking a tuple and a dictionary.

def print_info(name, age, city): 
    return print(f"My name is {name}, I am {age}, and I live in {city}")

info_tuple = ("Ness", 25, "Paris")
info_dict = {"name" : "Ines", "age" : 23, "city" : "Paris"}

print_info(*info_tuple)
print_info(**info_dict)

# 4. Merge two lists into one using spreading (*).

lst_1 = [1,2,3,4]
lst_2 = [12,10,3,3]

spread_lst = [*lst_1, *lst_2]
print(spread_lst)

# 5. Iterate over the list 'fruits' with enumerate and print the index and the fruit.

fruits = ["banana", "apple", "cherry", "strawberry"]

for index, fruit in enumerate(fruits):
    print(index, fruit) 

for index, fruit in enumerate(fruits, start = 2):
    print(index, fruit)

# 6. Given two lists 'names' and 'ages', use zip to print "<name> is <age> years old."

names = ["Ines", "Sofia", "Laetitia"]
ages = [25, 24, 25]

for name, age in zip(names, ages): 
    print(f"My name is {name} and I am {age}")

# 7. Given a list of tuples 'pairs', unzip it into two separate lists using zip.

paires = [(1, 'a'), (2, 'b'), (3, 'c')]

numbers, letters = zip(*paires)
print(numbers)
