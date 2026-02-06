### Day 5 : Lists ###

## Exercises ##

# Level 1 :

# 1. Declare an empty list

empty_list = list()
print(empty_list) # first method, but only one argument can be put in it

empty_list = []
print(empty_list) # second method

# 2. Declare a list with more than 5 items

lst = ["manga", "simba", "kitty", "mikado", "arai", "luna"]
lenght_lst = len(lst)

# 3. Find the length of your list

print(lenght_lst)
more_than_5 = lenght_lst > 5
print(more_than_5)

# 4. Get the first item, the middle item and the last item of the list

first_item = lst[0]
middle_item = lst[2]
last_item = lst[-1]
print(first_item, middle_item, last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Ines", 25, 157, "Single", "Colombes"]
print(mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7.Print the list using print()

print(it_companies)

# 8. Print the number of companies in the list

print(len(it_companies)) # 6 companies 

# 9. Print the first, middle and last company

print(it_companies[0], it_companies[2],it_companies[-1])

# 10. Print the list after modifying one of the companies

it_companies[0] = "FaceBook"
print(it_companies)

# 11. Add an IT company to it_companies

it_companies.insert(0,"Capgemini")
print(it_companies) # don't forget to put the index

# 12. Insert an IT company in the middle of the companies list

it_companies.insert(3,"Canva")
print(it_companies) 

# 13. Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[4] = "APPLE"
print(it_companies)

# After checking I could have do that : 

it_companies[4] = it_companies[4].upper()
print(it_companies[4]) # I prefer this method :)

# 14. Join the it_companies with a string '#;  '

# I have to use join(), viewed in day 4

it_companies_join = "#, ".join(it_companies)
print(it_companies_join)

# 15. Check if a certain company exists in the it_companies list.

print("Canva" in it_companies)

# 16. Sort the list using sort() method

it_companies.sort() # i tried to do that "print(it_companies.sort())" but says "NONE" because I have to print it_companies directly
print(it_companies) # it works! 

# 17. Reverse the list in descending order using reverse() method

it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list

first_three = it_companies[0:3] # start (include) but end (exclude)
print(first_three)

# 19. Slice out the last 3 companies from the list

last_three = it_companies[-3:]
print(last_three) # start with -3 to the end and not the inverse

# 20. Slice out the middle IT company or companies from the list

print(len(it_companies)) # 8
middle_companies = it_companies[3:5] # 3 include 5 exclude
print(middle_companies)

# 21. Remove the first IT company from the list

# it_companies.remove() if we want to specify the item but for now we only want the first one
# we can use pop() or del

del it_companies[0]
print(it_companies) # oracle has been removed

# 23. Remove the last IT company or companies from the list

del it_companies[-1] # for the last, APPLE should be removed
print(it_companies) 

# 24. Remove all IT companies from the list

it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list

del it_companies 

# 26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end) # stocked in the lst1

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = front_end.copy()
print(full_stack)

full_stack.insert(5, "Python")
print(full_stack)

full_stack.insert(6, "SQL")
print(full_stack)

# Level 2 :

# 1. The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age

ages.sort()
print(ages)

# Find min and max

min_age = min(ages)
max_age = max(ages)
print("Min :", min_age, "Max :", max_age)

# Add min and max to the list

ages.append(min_age)
ages.append(max_age)

# Find the median age (one middle item or two middle items divided by two)

# formula for the median =  one or two middle item / 2

print(len(ages))

# the list is pair, so i have to take two elements

# I have to take (n/2) - 1 et n/2

print((12/2)- 1)
print(12/2)

# So, I have to take the 5 and 6th value

median_age = (ages[5] + ages[6])/2
print("The median age is ", median_age)

# Now let's calculate the average age
# I have to sum all of the ages / len 

sum_ages = sum(ages)
print(sum_ages)

average_age = sum_ages / (len(ages))
print("The average age is : ", average_age)

# For the range I have to do max - min

range_age = max_age - min_age
print("The range of the ages is ", range_age)

# Compare the value of (min - average) and (max - average), use abs() method

print(abs(min_age - average_age)) 
print(abs(max_age - average_age))

# min distance > max distance 

# 2. Find the middle country(ies) in the countries list

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

# I made researches : 

if n % 2 == 0:  # means the remainder is 0
    print("The list has an even number of elements")
    middle_index1 = (n // 2) - 1 # // bc we dont want a float 
    middle_index2 = n // 2
    print("The two middle countries are: ", countries[middle_index1], countries[middle_index2])
else :
    print("The list has an odd number of elements")
    middle_index = (n-1) // 2 
    print("The middle country is : ", middle_index)

# I also did 195/2 but this wasn't the best method so I tried with if

# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.

# I can't because the list is unpair but now we know the index of the middle country

first_half = countries[0:98] # end exclude
second_half = countries[98:] # start include

print(len(first_half), len(second_half))

# first half > second

# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries # i have to do it in this order

print(scandic_countries)
