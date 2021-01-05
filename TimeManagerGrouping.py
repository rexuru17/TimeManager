# this file will be used to create csv file that groups activities from all input
# possibly create a list of activities and then instead of typing them over and over, choose them from a list

from csv import DictWriter
import numpy
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

name = input("Welcome to Time Manager, what is your name? ")
print("Hello, ", name)

user_dir = name
user_file = f"{name}.csv"

df = pd.read_csv(f'./{name}/{name}.csv')
activities = list(numpy.asarray(df.activity.unique()))
print(activities)
groups_by_type = {}
file_headers = ['group', 'activity']
filecheck = os.path.isfile(f"{BASE_DIR}/{name}/{name}-groups.csv")
if filecheck is False:
    open(os.path.join(f"{BASE_DIR}/{name}", f"./{name}-groups.csv"), 'a+')
    with open(f"./{name}/{name}-groups.csv", 'w') as f:
        f.write("group,activity" + '\n')
    print("Above are the activities extracted from your database. Please input types of your activities: ")
    for activity in activities:
        activity_type = input(f"How would you describe your activity '{activity}'?")
        groups_by_type = {'group': str(activity_type), 'activity': str(activity)}
        with open(f"./{name}/{name}-groups.csv", "a+", newline='') as group_file:
            dict_writer = DictWriter(group_file, fieldnames=file_headers)
            dict_writer.writerow(groups_by_type)
    print("thank you")
else:
    print("You have already created groups")
