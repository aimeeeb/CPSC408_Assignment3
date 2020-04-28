# Created by Aimee Bowen
# Student ID: 2277842
# Email: bowen126@mail.chapman.edu
# Description: This file connects to final_project MySQL database and generates fake data for the tables using Faker.

import mysql.connector
import csv
from faker import Faker

# INPUT DATABASE INFORMATION HERE
db = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
)

# create cursor for database
mycursor = db.cursor()

# variable for Faker
fake = Faker()

# ask for user input
filename = input("Input name of file: ") + '.csv'

tuples = 0

# error checking for tuples
while tuples == 0:
    user_input = input("How many tuples would you like generated?: ")
    try:
        tuples = int(user_input)
        print("Creating CSV now...")
        break
    except ValueError:
        print("Input must be a whole number.")
        tuples = 0

# create csv file
with open(filename, 'w') as csvfile:
    fields = ['ListName', 'ItemName', 'Description', 'DueDate', 'EventName', 'Date', 'AttendeeName', 'Username']

    writer = csv.DictWriter(csvfile, fieldnames=fields)

    while tuples != 0:
        writer.writerow({'ListName': fake.word(),
                         'ItemName': fake.word(),
                         'Description': fake.sentence(),
                         'DueDate': fake.date_time(),
                         'EventName': fake.word(),
                         'Date': fake.date_time(),
                         'AttendeeName': fake.name(),
                         'Username': fake.user_name()
                         })
        tuples -= 1

print("CSV created, writing to database...")

# write csv file to database
with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if row:
            mycursor.execute("INSERT INTO Lists(ListName) VALUES(%s)", (row[0],))
            mycursor.execute("INSERT INTO ListItems(ItemName, Description, DueDate, List) VALUES(%s, %s, %s, %s)", (row[1], row[2],row[3], 1))
            mycursor.execute("INSERT INTO Events(Name, Date) VALUES(%s, %s)", (row[4], row[5],))
            mycursor.execute("INSERT INTO EventAttendees(AttendeeName, Event) VALUES(%s, %s)", (row[6], 1,))
            mycursor.execute("INSERT INTO Users(Username) VALUES(%s)", (row[7],))


db.commit()
print("Done.")

# close connection
db.close()
