import sqlite3

# connect to sqlite
connection=sqlite3.connect('student.db')

# create a cursor object to insert record, create table
cursor=connection.cursor()

# create the table
table_info="""
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

# Insert some records
cursor.execute('''Insert into STUDENT VALUES('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''Insert into STUDENT VALUES('Vishal', 'Data Science', 'B', 100)''')
cursor.execute('''Insert into STUDENT VALUES('Akshay', 'Data Science', 'A', 86)''')
cursor.execute('''Insert into STUDENT VALUES('Sachin', 'DEVOPS', 'A', 50)''')
cursor.execute('''Insert into STUDENT VALUES('Rohan', 'DEVOPS', 'A', 35)''')

## Display all the rceords
print('Inserted records are')
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# commit your changes in databse
connection.commit()
connection.close()

