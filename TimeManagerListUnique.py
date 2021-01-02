# this file will be used to create a list fo unique activities to chose from OR create a new activity


import pandas as pd
import os
import numpy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

name = input("Welcome to Time Manager, what is your name? ")
print("Hello, ", name)

user_dir = name
user_file = f"./{name}/{name}.csv"
unique_dict = {}

df = pd.read_csv(user_file)
unique_names = list(numpy.asarray(df.activity.unique()))
x = 0
for name1 in unique_names:
    unique_dict[x] = name1
    x += 1

# this thing prints keys and values for unique items in database.
# now find a way to make the n-th item create new item and by selecting key, automatically add value instead of typing
for k, v in unique_dict.items():
    print(k, v)
