### Day 20 : Package manager ###

## Exercises ##

# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

import requests

romeo_and_juliet = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"

response = requests.get(romeo_and_juliet)
print(response)
print(response.status_code)
print(response.headers)
print(response.text) 

txt = response.text

import re

def find_most_frequent_words(txt, n):
    regex_pattern = r'b\w+\b'
    empty_dict = dict()
    count = 0
    frequent_words = re.findall(regex_pattern, txt)
    for word in frequent_words: 
        if word in empty_dict: 
            empty_dict[word] += 1
        else: 
            empty_dict[word] = 1
    items = list(empty_dict.items())
    items.sort(key = lambda x: x[1], reverse=True)
    return items[:n]

print(find_most_frequent_words(txt, 10))

# 2. Read the cats API and find

# i. the min, max, mean, median, standard deviation of cats' weight in metric units.

cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
print(response)
print(response.status_code)
cats = response.json()
print(cats)

print(type(cats))

weights = list()


def clean_range(range): 
    parts = range.split('-') # convert in two parts
    low = float(parts[0].strip()) # remove empty spaces and convert to a float 
    high = float(parts[1].strip())
    return (low + high) / 2

for cat in cats: 
    weight_metric = cat["weight"]["metric"]
    avg_weight = clean_range(weight_metric)
    weights.append(avg_weight)

import numpy as np 

weight_array = np.array(weights)

print("Min:", weight_array.min())
print("Max:", weight_array.max())
print("Mean:", weight_array.mean())
print("Median:", np.median(weight_array))
print("Standard Deviation:", weight_array.std())

print(weight_array)

# ii. the min, max, mean, median, standard deviation of cats' lifespan in years.


lifespan = list()

for cat in cats: 
    life_span = cat["life_span"]
    avg_life_span  = clean_range(life_span)
    lifespan.append(avg_life_span)

life_span_array = np.array(lifespan)

print("Min:", life_span_array.min())
print("Max:", life_span_array.max())
print("Mean:", life_span_array.mean())
print("Median:", np.median(life_span_array))
print("Standard Deviation:", life_span_array.std())

# iii. Create a frequency table of country and breed of cats

freq_table = dict()

for cat in cats: 
    country = cat.get("country_code") or cat.get("country_codes") or "Unknown"
    breed = cat.get("name", "Unknown")
    key = (country, breed)
    if key in freq_table: 
        freq_table[key] += 1
    else:
        freq_table[key] = 1

print(freq_table)

print(f"{'Country':<10} | {'Breed':<30} | {'Frequency':<5}")
print("-" * 50)

for (country, breed), count in freq_table.items():
    print(f"{country:<10} | {breed:<30} | {count:<5}")

# 3. Read the countries API and find

url = "https://restcountries.com/v3.1/all?fields=name,area,languages"
response = requests.get(url)
countries = response.json()

# i. the 10 largest countries

countries_sorted = sorted(countries, key=lambda country: country.get('area', 0), reverse=True) # we take the value of the key area for each country, else 0

print("10 most largest countries")
for country in countries_sorted[:10]: 
    name = country["name"]["common"]
    area = country.get("area")
    print(f"{name} : {area} km²")

# ii. the 10 most spoken languages

languages_count = dict()

for country in countries:  # for each country 
    languages = country.get("languages") # we take languages 
    if languages : # if there is languages
        for lang in languages.values(): # for each language in languages values
            if lang in languages_count: 
                languages_count[lang] +=1
            else: 
                languages_count[lang] = 1
 
languages_sorted = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)

print("10 most spoken languages (by nb of country) : ")
for lang, count in languages_sorted[:10]:
    print(f"{lang} : spoken in {count} countries")

# iii. the total number of languages in the countries API

langu_count = dict()

for country in countries: 
    languages = country.get("languages")
    if languages: 
        for lang in languages.values(): 
            if lang in langu_count: 
                langu_count[lang] += 1
            else:
                langu_count[lang] = 1

total_languages = len(langu_count)
print(f"Total number of languages : {total_languages}")

# 4. UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

import requests 
from bs4 import BeautifulSoup

url = "https://archive.ics.uci.edu/datasets"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(response.text[:1000])  # Affiche les 1000 premiers caractères


# Find the main table that contains the datasets
# This table has an attribute border="1"

table = soup.find('table', {'border': '1'})

datasets = [] # empty list 

for row in table.find_all("tr")[1:]: # we loop through all rows except the first one bc is the header
    cols = row.find_all("td") # columns in the current row
    if len(cols) >= 6: 
        name = cols[0].get_text(strip=True)           # Dataset name
        data_types = cols[1].get_text(strip=True)     # Data types in the dataset
        default_task = cols[2].get_text(strip=True)   # Default task for the dataset
        attribute_types = cols[3].get_text(strip=True) # Attribute types
        instances = cols[4].get_text(strip=True)      # Number of instances (rows)
        attributes = cols[5].get_text(strip=True)     # Number of attributes (features)
        datasets.append({
            'name': name,
            'data_types': data_types,
            'default_task': default_task,
            'attribute_types': attribute_types,
            'instances': instances,
            'attributes': attributes
        })

# Display the first 10 datasets with selected information
print("First 10 datasets from UCI Machine Learning Repository:")
for d in datasets[:10]:
    print(f"Name: {d['name']}, Instances: {d['instances']}, Attributes: {d['attributes']}")