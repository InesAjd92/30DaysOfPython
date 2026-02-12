### Day 19 : File handling ###

## Exercises ##

# Level 1 : 

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:

import re 

with open("/home/inesajd/obama_speech.txt", "r") as obama_speech:
    text = obama_speech.read()

def count_lines_words(txt): 
    lines = txt.splitlines() # we split the text in a list of lines 
    count_lines = len(lines) # we count the len of the list 
    regex_pattern = r'\b\w+\b' # means a complete word 
    words = re.findall(regex_pattern, txt)
    count_words = len(words)
    return count_lines, count_words
    
lines, words = count_lines_words(text)
print(f"There are {lines} lines and {words} words in the Obama speech.")

with open("/home/inesajd/michelle_obama_speech.txt", "r") as michelle_obama_speech:
    text = michelle_obama_speech.read()

lines, words = count_lines_words(text)
print(f"There are {lines} lines and {words} words in the Michelle Obama speech.")

with open("/home/inesajd/donald_speech.txt", "r") as donald_speech:
    text = donald_speech.read()

lines, words = count_lines_words(text)
print(f"There are {lines} lines and {words} words in the Donald T. speech.")

with open("/home/inesajd/melina_trump_speech.txt", "r") as melina_trump_speech:
    text = melina_trump_speech.read()

lines, words = count_lines_words(text)
print(f"There are {lines} lines and {words} words in the Melina T. speech.")


# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

import json 

with open("/home/inesajd/countries_data.json", "r") as countries_data:
    countries = countries_data.read()


def most_spoken_languages(countries, n): 
    txt = json.loads(countries)
    count_languages = dict()
    for country in txt: 
        for language in country["languages"]:
            if language in count_languages: 
                count_languages[language] += 1
            else:
                count_languages[language] = 1
    sorted_languages = sorted(count_languages.items(), key=lambda x: x[1], reverse=True)
    return [(count, language) for language, count in sorted_languages[:n]]


print(most_spoken_languages(countries, 10))
print(most_spoken_languages(countries, 3))

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

with open("/home/inesajd/countries_data.json", "r") as countries_data:
    countries = countries_data.read() # with to close automaticcaly 

def most_populated_countries(countries,n):
    txt = json.loads(countries) # convert json to dic
    population_list = [] # to stock
    for country in txt: # for each country in txt
        name = country["name"] # name will be name
        population = country["population"] # pop will be pop
        population_list.append((population, name)) # we stock pop and name in our empty list
        population_list = sorted(population_list, reverse=True) # we sorted our list 
    return population_list[:n] # we return our new list with a parameter that can filter n rows 


print(most_populated_countries(countries, 10))

# Level 2 : 

# 1. Extract all incoming email addresses as a list from the email_exchange_big.txt file.

with open("/home/inesajd/email_exchanges_big.txt", "r") as email_exchanges:
    email_exchanges = email_exchanges.read()

"""
def extract_emails(txt): 
    adresses_list = []
    regex_pattern = r"<[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" # all letters, digits, before and after the @, then at least 2 char for the extension .com, .eu, etc.
    adresses = re.findall(regex_pattern, txt)
    adresses_list.append(adresses)
    return adresses_list

print(extract_emails(email_exchanges)) """ # sounds good 

# 2. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

def find_most_common_words(strg, n): # strg for a string, n for a number of words
    most_common_words = {}
    count_word = 0
    regex_pattern = r"\b\w+\b"
    common_words = re.findall(regex_pattern, strg)
    for word in common_words: 
        if word in most_common_words :
            most_common_words[word] += 1
        else: 
            most_common_words[word] = 1
    items = list(most_common_words.items()) # we trasnform our dict into a list of tuples
    items.sort(key=lambda x: x[1], reverse=True) # we sort by x[1], so by count
    return items[:n] 

print(find_most_common_words(email_exchanges, 10)) # ok

# 3. Use the function, find_most_frequent_words to find:

# i. The ten most frequent words used in Obama's speech

with open("/home/inesajd/obama_speech.txt", "r") as obama_speech:
    obama = obama_speech.read()

print("For Barack Obama : ", find_most_common_words(obama,10))

# ii. The ten most frequent words used in Michelle's speech


with open("/home/inesajd/michelle_obama_speech.txt", "r") as michelle_obama_speech:
    michelle = michelle_obama_speech.read()

print("For Michelle Obama : ", find_most_common_words(michelle,10))


# iii. The ten most frequent words used in Trump's speech

with open("/home/inesajd/donald_speech.txt", "r") as donald_speech:
    donald = donald_speech.read()

print("For Donald Trump : ",find_most_common_words(donald, 10))

# iv. The ten most frequent words used in Melina's speech

with open("/home/inesajd/melina_trump_speech.txt", "r") as melina_trump_speech:
    melina = melina_trump_speech.read()

print("For Melina Trump :", find_most_common_words(melina, 10))

# 4. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def clean_text(txt): 
    regex_pattern = r"\b\w+\b" # to extract each word
    common_words = re.findall(regex_pattern, txt.lower()) # lower to catch the "I"
    return common_words

def remove_support_words(common_words, stop_words): 
    filtered_words = [word for word in common_words if word not in stop_words]
    return filtered_words

def check_similarity(txt_1, txt_2):
    return set(txt_1) & set(txt_2)

txt_1 = clean_text(michelle)
txt_2 = clean_text(melina)

txt_1 = remove_support_words(txt_1, stop_words)
txt_2 = remove_support_words(txt_2, stop_words)

print(check_similarity(txt_1, txt_2))

common_words = check_similarity(txt_1, txt_2)
print(f"Common words ({len(common_words)}):")
print(sorted(common_words))

union = set(txt_1) | set(txt_2)
similarity_score = len(common_words) / len(union)
print(f"Similarity score (Jaccard index): {similarity_score:.2f}")

# 5. Find the 10 most repeated words in the romeo_and_juliet.txt

with open("/home/inesajd/romeo_and_juliet.txt", 'r') as romeo_and_juliet: 
    romeo_juliet = romeo_and_juliet.read()

print(find_most_common_words(romeo_juliet,10)) # there is a lot of stop words in it!

romeo_juliet_cleaned = clean_text(romeo_juliet)
romeo_juliet_filtered = remove_support_words(romeo_juliet_cleaned, stop_words)

text_filtered_str = " ".join(romeo_juliet_filtered)
print(find_most_common_words(text_filtered_str, 10))

# 6. Read the hacker news csv file and find out:

import csv 

# i.Count the number of lines containing python or Python

with open("/home/inesajd/hacker_news.csv") as hacker_news:
    csv_reader = csv.reader(hacker_news, delimiter=",")
    line_count = 0 
    python_lines = 0
    count_python_lines = 0
    for row in csv_reader: 
        if line_count == 0: 
            print(f'Column names are : {",".join(row)}')
            line_count += 1
        else: 
            line_count += 1
        for cell in row: 
            if "python" in cell.lower():
                count_python_lines += 1
        if count_python_lines > 0: 
            python_lines += 1

print(f"Nb of lines containing python:  {python_lines}")

# ii. Count the number lines containing JavaScript, javascript or Javascript

with open("/home/inesajd/hacker_news.csv") as hacker_news:
    csv_reader = csv.reader(hacker_news, delimiter=",")
    line_count = 0 
    javascript_lines = 0
    for row in csv_reader: 
        if line_count == 0: 
            print(f"The column are named : {','.join(row)}")
            line_count += 1
        else: 
            line_count +=1 
            found_javascript = False
            for cell in row: 
                if "javascript" in cell.lower(): 
                    found_javascript = True
                if found_javascript : 
                    javascript_lines +=1 

print(f"Nb of lines where the word javascript is : {javascript_lines}")


# iii. Count the number lines containing Java and not JavaScript

with open("/home/inesajd/hacker_news.csv") as hacker_news:
    csv_reader = csv.reader(hacker_news, delimiter=",")
    line_count = 0 
    javascript_lines = 0
    java_not_javascript_lines = 0
    for row in csv_reader: 
        if line_count == 0: 
            print(f"The column are named : {','.join(row)}")
            line_count += 1
        else: 
            line_count +=1 
            found_javascript = False
            found_java = False
            for cell in row: 
                if "javascript" in cell.lower(): 
                    found_javascript = True
                elif "java" in cell.lower():
                    found_java = True
                if found_java and not found_javascript: 
                    java_not_javascript_lines +=1 

print(f"Number of lines containing 'Java' but not 'JavaScript': {java_not_javascript_lines}")

