import sqlite3
import csv

file_name = ""
table_name = ""
connection = sqlite3.connect('db_csv.db')
cursor = connection.cursor()

file = open(file_name)
contents = csv.reader(file)
insert_records = "INSERT INTO {table_name} VALUES(?, ?, ?)"
cursor.executemany(insert_records, contents)
connection.commit()
