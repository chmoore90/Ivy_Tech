# %% [markdown]
# ## M07 Getting Started with Python

# %% [markdown]
# Item 1 - Input and Output

# %%
name    = input("Enter Employee Name")
salary  = input("Enter salary")
company = input ("Enter Company name")
print("Printing Employee Details")
print ("Name", "Salary", "Company")
print (name, salary, company)

# %% [markdown]
# Item 2 - Python Functions

# %%
# add_numbers is a function that takes two numbers and adds them together.
def add_numbers(x, y):
    return x + y

add_numbers(1, 2)


# %%
# add_numbers updated to take an optional 3rd parameter. Using print allows printing of multiple expressions within a single cell.
def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))

# %%
# add_numbers updated to take an optional flag parameter.
def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z

print(add_numbers(1, 2, flag=True))

# %%

# Assign function add_numbers to variable a.
def add_numbers(x,y):
    return x+y

a = add_numbers
a(1,2)

# %% [markdown]
# Item 3 - Types and Sequences

# %%
# This code returns portions of a string, similar to the substring function in SQL.
x = 'This is a string'
print(x[0]) #first character
print(x[0:1]) #first character, but we have explicitly set the end character
print(x[0:2]) #first two characters

# %%
# This will return the last element of the string.
x = 'This is a string'
x[-4:-2]

# %%
# This is a slice from the beginning of the string and stopping before the 3rd element..
x = 'This is a string'
x[:3]

# %%
# split returns a list of all the words in a string, or a list split on a specific character.
firstname = 'Jean-Luc Picard'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Jean-Luc Picard'.split(' ')[-1] # [-1] selects the last element of the list
print(firstname)
print(lastname)

# %% [markdown]
# Item 4 - Reading and Writing to CSV Files

# %%
# load data from a CSV file ant ourput the first 12 dictionaries.

import csv


with open('M07\worldstats.csv') as csvfile:
    stats = list(csv.DictReader(csvfile))

stats[:12] # The first 12 dictionaries in our list.

# %%
# this code will get the avg population for each country across all years recorded.
CountryName = set(d['country'] for d in stats) # get the country names
avg_gdp = []

for t in CountryName: # iterate over all the countries
    pop = 0
    i = 0
    for d in stats: # iterate over all dictionaries
        if d['country'] == t: # if the country name matches
            pop += float(d['Population']) # add the hwy mpg
            i += 1 # increment the count
    avg_gdp.append((t, pop / i)) # append the tuple ('CountryName', 'pop')

avg_gdp.sort(key=lambda x: x[0]) # sort by country name i.e. column 0.
print(avg_gdp)


# %%
# What code would I use to get the average global population by year? Use the above code as an example, change what you need to make it work.

years = set(d["year"] for d in stats)
avg_gdp = []

for year in years:
    pop = 0
    i = 0
    for d in stats:
        if d["year"] == year:
            pop += float(d["Population"])
            i += 1
    avg_gdp.append((year, pop / i))

avg_gdp.sort(key=lambda x: x[0])
print(avg_gdp)

# %% [markdown]
# Item 5 - Using Pandas to Analyze Data

# %%
# use Pandas to import a CSV file and print the first 5 rows
import pandas as pd

df = pd.read_csv('M07\worldstats.csv')
print(df.head(5))

# %%
# use Pandas to import a CSV file and print the last 5 rows
import pandas as pd

df = pd.read_csv('M07\worldstats.csv')
print(df.tail(5))

# %% [markdown]
# Item 6 - Make It Your Own

# %%
# Average GPD per country, sorted by highest to lowest GDP

countries = set(d["country"] for d in stats)
avg_gdp = []

for country in countries:
    gdp = 0
    i = 0
    for d in stats:
        if d["country"] == country:
            gdp += float(d["GDP"])
            i += 1
    avg_gdp.append((country, gdp / i))

avg_gdp.sort(key=lambda x: x[1], reverse=True)
print(avg_gdp)

# %%
# Population of Canada

import pandas as pd

with open("M07\worldstats-canadapop.csv", "w") as can:
    can.write("year, population\n")
    for d in stats:
        if d["country"] == "Canada":
            can.write(f"{d['year']}, {d['Population']}\n")

df = pd.read_csv("M07\worldstats-canadapop.csv")
print(df)

# %%
"""
Python can be used to quickly sort data and perform calculations. Since it is interacting directly with the data file (eg. csv), it will much faster than Excel or Tableau.
In addition to pandas, there are other libraries like numpy and matplotlib that can assist in parsing, performing calculations, and display data.
"""
