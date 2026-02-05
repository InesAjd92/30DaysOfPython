### Day 5

# Exercises 

### Level 1 

# 1/

empty_list = list()
print(empty_list) #first method, but only one argument can be put in it

empty_list = []
print(empty_list) #second method

# 2/ 

lst = ["manga", "simba", "kitty", "mikado", "arai", "luna"]
lenght_lst = len(lst)


# 3/ 

print(lenght_lst)
more_than_5 = lenght_lst > 5
print(more_than_5)

# 4/ 

first_item = lst[0]
middle_item = lst[2]
last_item = lst[-1]
print(first_item, middle_item, last_item)

# 5/ 

mixed_data_types = ["Ines", 25, 157, "Single", "Colombes"]
print(mixed_data_types)

# 6/ 

it_companies = ["Facebook", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7/

print(it_companies)

# 8/

print(len(it_companies)) #6 companies 

# 9/

print(it_companies[0], it_companies[2],it_companies[-1])

# 10/ 

it_companies[0] = "FaceBook"
print(it_companies)

# 11/ 

it_companies.insert(0,"Capgemini")
print(it_companies) #dont forget the index

# 12/ 

it_companies.insert(3,"Canva")
print(it_companies) 

# 13/ 

#Reminder : 
it_companies[4] = "APPLE"
print(it_companies) # i thought i could use .upper() but only apply with str?

#After checking we could have do that : 

it_companies[4] = it_companies[4].upper()
print(it_companies[4]) #I prefer this method :)

# 14/ 

# I have to use join(), viewed in day 4
# Join the it_companies with a string '#;  '

it_companies_join = "#, ".join(it_companies)
print(it_companies_join)

# 15/ 

print("Canva" in it_companies)

# 16/ 

it_companies.sort()
# i tried to do that "print(it_companies.sort())" but "NONE" because i have to print it_companies directly

print(it_companies) # it works! 

# 17/ 

it_companies.reverse()
print(it_companies)

# 18/

first_three = it_companies[0:3] #start (include) but end(exclude)
print(first_three)

# 19/ 

last_three = it_companies[-3:]
print(last_three) #star with -3 to the end and not the inverse

# 20/ 

print(len(it_companies)) # 8
middle_companies = it_companies[3:5] #3 include 5 exclude
print(middle_companies)

# 21/

# it_companies.remove() if we want to speciy the item but for now we only want the first one
# we can use pop() or del

del it_companies[0]
print(it_companies) #oracle has been remove


# 23/  

del it_companies[-1] #for the last, APPLE should be removed
print(it_companies) #great!

# 24/

it_companies.clear()
print(it_companies)

# 25/

del it_companies #bye bye

# 26/
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end) #stocked in the lst1

# 27/

full_stack = front_end.copy()
print(full_stack)

full_stack.insert(5, "Python")
print(full_stack)


full_stack.insert(6, "SQL")
print(full_stack)

# Level 2 :

#1. 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

print("Min :", min(ages), "Max :", max(ages))

# or bc better for adding this again

min_age = min(ages)
print(min_age)

max_age = max(ages)
print(max_age)

# i add the min and the max a second time

# i did errors
# i cant do this like that because the first argument is an index, i have to do it twice
# ages.insert(max_age, min_age)

ages.append(min_age)
ages.append(max_age)


# formula for the median =  one or two middle item / 2

print(len(ages))

#the list is pair, so i have to take two elements

# I have to take (n/2) - 1 et n/2

print((12/2)- 1)
print(12/2)

#So, i have to take the 5 and 6th value

median_age = (ages[5] + ages[6])/2
print("The median age is ", median_age)

# Now lets calculate the average age
# I have to sum all of the ages / len 

sum_ages = sum(ages)
print(sum_ages)

average_age = sum_ages / (len(ages))
print("The average age is : ", average_age)

# For the range I have to do max - mon

range_age = max_age - min_age
print("The range of the ages is ", range_age)

# Compare the value of (min - average) and (max - average), use abs() method

print(abs(min_age - average_age)) 
print(abs(max_age - average_age))

# min distance > max distance 

# 2/ Find the middle

countries = [


  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

print(len(countries))

n = len(countries)

if n % 2 == 0: 
    print("The list have a pair nb element")
    middle_index1 = (n // 2) - 1 # // bc we dont want a float 
    middle_index2 = n // 2
    print("Les deux pays du milieux sont", countries[middle_index1], countries[middle_index2])
else :
    print("The list is unpair")
    middle_index = (n-1) // 2 
    print("Le pays du milieu est", middle_index)



# i also did 195/2 but this wasnt the best method so i tried with if

# Divide the countries list into two equal lists if it is even if not one more country for the first half.

# we cant because the list is unpair but now we know the index of the middle country

first_half = countries[0:98] #end exclude
second_half = countries[98:] # start include

print(len(first_half), len(second_half))

#first half > second

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries # i have to do it in this order

print(scandic_countries)

#yaaaay!

