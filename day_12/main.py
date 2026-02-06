### Day 12 : Modules 

# main.py file

import mymodule

print(mymodule.generate_full_name('Ines', 'Ajd')) 

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

import string 
import random

## Exercises ## 

# Level 1 : 

# 1. Write a function which generates a six digit/character random_user_id.

def random_user_id(): 
    char = string.ascii_letters
    digits = string.digits
    punctuations = string.punctuation
    all = char + digits + punctuations
    user_id = ''.join(random.choices(all, k = 6))
    return user_id
    

print(random_user_id()) 

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def id_gen_by_user(): 
    lenghts_id = int(input("Lenght of user id:"))
    how_much_id = int(input("Number of user id: "))
    char = string.ascii_letters
    digits = string.digits
    punctuations = string.punctuation
    all = char + digits + punctuations
    for n in range(how_much_id): 
        user_id = ''.join(random.choices(all, k = lenghts_id))
        print(user_id)
    return None


print(id_gen_by_user()) # user input: 5 5

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    rgb_1 = str(randint(0,255))
    rgb_2 = str(randint(0,255))
    rgb_3 = str(randint(0,255))
    all_rgb = [rgb_1, rgb_2, rgb_3]
    rgb_colors = ','.join(all_rgb)
    return f"rgb({rgb_colors})"

print(rgb_color_gen())


# Level 2 : 

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).


def list_of_hexa_colors():
    possible_char = "0123456789abcdef"
    chars = "".join(random.choices(possible_char, k = 6))
    hexa_color = "#" + chars
    return hexa_color

print(list_of_hexa_colors())

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors():
    number_of_colors = randint(0,20)
    lst = list()
    for n in range(number_of_colors): 
        rgb_1 = str(randint(0,255))
        rgb_2 = str(randint(0,255))
        rgb_3 = str(randint(0,255))
        rgb_colors = [rgb_1, rgb_2, rgb_3]
        rgb_colors = ",".join(rgb_colors)
        color = f"rgb({rgb_colors})"
        lst.append(color)
    return lst


print(list_of_rgb_colors())

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colors(type, number):
    colors_generated = list()
    for n in range(number):
        if type == "hexa":
            possible_char = "0123456789abcdef"
            chars = "".join(random.choices(possible_char, k = 6))
            hexa_color = "#" + chars
            colors_generated.append(hexa_color)
        else :
            rgb_1 = str(randint(0,255))
            rgb_2 = str(randint(0,255))
            rgb_3 = str(randint(0,255))
            rgb_colors = [rgb_1, rgb_2, rgb_3]
            rgb_colors = ",".join(rgb_colors)
            rgb_color = f"rgb({rgb_colors})"
            colors_generated.append(rgb_color)
    return colors_generated


print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b']
print(generate_colors('rgb', 5))

# Level 3 : 

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(lst): 
    random.shuffle(lst)
    return lst

print(shuffle_list(["ness", "so", "lae"]))

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def random_numbers():
    set_numbers = set()
    while len(set_numbers) < 7: 
        number = randint(0,9)
        set_numbers.add(number)
    return list(set_numbers)

print(random_numbers())

