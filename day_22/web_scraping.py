### Day 22 : Web scraping ###

## Exercises ##

# 1.Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').

import requests
from bs4 import BeautifulSoup
import json

# Url to scrape : 

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Fetch the data : 

response = requests.get(url) # fetch data from url 
status = response.status_code
print(status) # ok 200 

content = response.content
soup = BeautifulSoup(content, "html.parser")

# We initialize an empty dict to store the extracted data 

data = dict()

# First, i want to extract "Community" and all similiar selctions 

for section in soup.select('section.stat-section'): # we use select for the css selectors , here we get all the <section> and <stat-section>
    # I extract the section title (h4)
    title_tag = section.find('h4', class_='stat-group-title')
    title = title_tag.text.strip() if title_tag else "No Title"
    
    # Extract all stats in the list
    stats = {}
    for li in section.select('ul.custom-stat-list li'): # for each line (ul)
        label = li.find('span', class_='stat-label').text.strip()
        figure = li.find('span', class_='stat-figure').text.strip()
        stats[label] = figure
    
    data[title] = stats

# Now i want to extract blocks of stats with articles (like "Campus", "Quick Facts & Stats")

for block in soup.select('div.bu-stat-list'): # all div with bu-stat-list 
    # The section title is usually the previous sibling h4
    prev_h4 = block.find_previous_sibling('h4', class_='stat-group-title')
    title = prev_h4.text.strip() if prev_h4 else "No Title"
    
    stats = {}
    # Each article contains one stat
    for article in block.select('article.bu-stat-single'):
        stat_title = article.find('h3', class_='bu-stat-title').text.strip()
        
        # The value is built from multiple spans (prefix, number, suffix)
        value_container = article.find('div', class_='bu-stat-value-container')
        value_parts = value_container.find_all('span', class_='bu-stat-value-field')
        value = ''.join(part.text.strip() for part in value_parts)
        
        stats[stat_title] = value
    
    data[title] = stats

# Ok, now we are going to save the data dictionary to a JSON file
with open('bu_facts_stats.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Data scraped and saved to 'bu_facts_stats.json'")

# 2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

# note : doesn't work anymore bc the structure of the website has changed!

# fetching the data 
"""

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

datasets_table = soup.find('table', class_='table')

# Now, we extract the table header cells (<th>) to get the  column names

table_header = datasets_table.find('thead')
header_cells = table_header.find_all('th')

column_names = []
for header_cell in header_cells:
    header_text = header_cell.get_text(strip=True) # allow to get the text without the <> html, strip to get rid off spaces
    column_names.append(header_text)

# Extract all rows from the table body (<tbody>)

table_body = datasets_table.find('tbody')
table_rows = table_body.find_all('tr')

datasets = []
for row in table_rows: # each line is an <tr>
    data_cells = row.find_all('td') # for each line we're searching for cells <td>
    if len(data_cells) == len(column_names): # we check if the nb of cells in a line == nb of columns
        dataset_info = {} # to stock 
        for i in range(len(column_names)): # index by index following the nb of columns stocked in column names
            column_name = column_names[i]
            data_cell = data_cells[i]
            cell_text = data_cell.get_text(strip=True)
            dataset_info[column_name] = cell_text
        datasets.append(dataset_info)

with open('uci_datasets.json', 'w', encoding='utf-8') as json_file:
    json.dump(datasets, json_file, ensure_ascii=False, indent=4)

print(f'Successfully saved {len(datasets)} datasets to uci_datasets.json') """

# 3. Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

response = requests.get(url)
print(response.status_code)  # error 403, wikipedia has blocked my requests
print(response.url)          # Should print the URL I requested, yes

table = soup.find('table', class_='wikitable')
