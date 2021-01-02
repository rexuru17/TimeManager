# this file will be used to create stats with data input from Time Manager


import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

name = input("Welcome to Time Manager, please enter your name: ")
print("Hello, ", name)

user_dir = name
user_file = f"{name}.csv"
# file_headers = ['date', 'activity', 'duration']

df = pd.read_csv(f'./{name}/{name}.csv')
group_sum = df.groupby(['activity']).sum()
group_count = df.groupby(['activity']).count()
group_dates = df.date.unique()
print("\n Your stats by activities (sum of minutes spent doing each task):")
print(group_sum)
print("\n How many times have you done each activity:")
print(group_count)
print("\n How many days have you logged:")
print(group_dates)
print("total days: ", len(group_dates))
