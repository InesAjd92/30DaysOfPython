### Day 25 : Pandas ###

## Exercises ##

import pandas as pd
print(pd.__version__)
import numpy as np

# 1. Read the hacker_news.csv file from data directory

df = pd.read_csv("/home/inesajd/hacker_news.csv")
print(df)

# 2. Get the first five rows

print(df.head())

# 3. Get the last five rows

print(df.tail())

# 4. Get the title column as pandas series

columns = df.columns
print(columns)

titles = df["title"]
print(titles)

# 5. Count the number of rows and columns

print(df.shape, columns) 

# There are 20099 rows and 7 columns. 

# - Filter the titles which contain python

python_titles = df[df['title'].str.contains('python', case=False, na=False)]
print(python_titles)

# - Filter the titles which contain JavaScript

java_titles = df[df["title"].str.contains("javascript", case=False,na=False )]
print(java_titles)

# - Explore the data and make sense of it



# My notes : 

# A panda serie is just one column of data. We can create one with np.array (one dimensiona) or a list.
# To have multiple columns we use data frames

# To create series with panda we use .Series(lst) or .Series(one dim array)
# We can specify a custum index, for ex to begin with 1 not 0

# With a dict, the index will be updated with the key names

# To create dataframes, there are different ways : 
# - from list (pd.dataframe(data, columns = [])) # data will be a list of lists
# - from a dict, pd.dataframe(data)
# - list of dict

# Data exploration 

# to show only 5 rows we can use df.head()
# for the last 5 is df.tail()
# to know the nb of rows we use df.shape
# to know the column : df.columns
# to get a specifif column we can use the column key
# the describe() methode provides descriptive startiscial values 
# to add a new column we create a new lst and we specify df['name of the coumn'] = lst



