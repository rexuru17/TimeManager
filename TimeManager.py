# this file will be used to add new activities to log into database
import os
import datetime
# import csv
from csv import DictWriter
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

name = input("Welcome to Time Manager, please enter your name: ")
print("Hello, ", name)

user_dir = name
user_file = f"{name}.csv"
file_headers = ['date', 'activity', 'duration']


def make_user_dir():
    dir_path = os.path.join('./', user_dir)
    try:
        os.mkdir(dir_path)
        open(os.path.join(dir_path, f"{name}.csv"), 'a+')
        with open(f"./{name}/{name}.csv", "w") as f:
            f.write("date,activity,duration" + '\n')
    except FileExistsError:
        print(f'Directory {dir_path} already exists, welcome back')
    else:
        print(f'Directory {dir_path} created, ready to log your activity')


make_user_dir()
input_data = "Y"
while input_data == "Y":

    activity = input(f"{name}, what activity would you like to log?")
    assert isinstance(activity, str)
    duration = int(input(f"How long did the activity {activity} lasted in minutes?"))
    assert isinstance(duration, int)
    check_date = input("Is this activity being logged for today(Y/N)?").upper()
    if check_date == "Y":
        log_stamp = datetime.date.today()
    else:
        log_stamp = input("Please input date for which to log this activity (format yyyy-mm-dd):")

    log_activity = {"date": str(log_stamp), "activity": activity, "duration": duration}
    with open(f"./{name}/{name}.csv", 'a+', newline='') as logfile:
        dict_writer = DictWriter(logfile, fieldnames=file_headers)
        dict_writer.writerow(log_activity)

    input_data = input("Would you like to continue with another activity? (Y/N)").upper()

print(f"Your log has been saved. Thank you and have a nice day, {name}")
