### Day 13: Exercises


# Remember : list comprehension is a fast way to create a new list (faster than loop)
# Syntaxe : 
# new_list = [expression for item in iterable if condition == True]


# 1/ Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_numbers = [n for n in numbers if n <= 0]
print(filtered_numbers)

# 2/ Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


new_dimensional_list = [n for sublist in list_of_lists for n in sublist]
# i.e on prend chaque nombre dans chaque sous liste qu'on apose ensuite a une nouvelle liste ou chaque n esr un element 
print(new_dimensional_list)

# 3/ 

# Chaque tuple à la forme : (n,n0,n1,n2,n3,n4,n5)
# n varie de 0 à 10
# pour chaque n i fais un tple avec ces élements

# n will be n 
# k will be the exposant 
# n**k for k in range(6) # pr aller de 0 à T

# [expression for variable1 in iterable1 for variable2 in iterable2]

result = [(n, *[n**k for k in range(6)]) for n in range(11)]
print(result)

# pas tout compris ici

# 4/ 

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output : [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# premiere element = uppercase
# deuxieme element = trois premieres lettre 
# troiseme element uppercase 
# new_list = [expression for item in iterable if condition == True]
# 3 tuples (trois sous listes)
# p = pays 



flatten_countries = [[tpl[0].upper(), tpl[0][:3], tpl[1].upper()] for sublist in countries for tpl in sublist]
print(flatten_countries)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

dict_countries = [{"country" : tpl[0].upper(), "city" : tpl[1].upper()} for sublist in countries for tpl in sublist]
print(dict_countries)

# 6/ 

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]


concatened_names = [tpl[0] + " " + tpl[1] for sublist in names for tpl in sublist]
print(concatened_names)

# 7/ 

solve_slope = lambda x1, x2, y1, y2 : (y2 - y1) / (x2-x1)

print(solve_slope(2, 3, 1, 2))  # Affiche 1.0
