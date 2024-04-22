import sqlite3


connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
Create Table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));
"""

cursor.execute(table_info)


cursor.execute('''Insert Into STUDENT Values('Krish', 'Data Science', 'A')''')
cursor.execute('''Insert Into STUDENT Values('Rahul', 'Data Engineering', 'A')''')
cursor.execute('''Insert Into STUDENT Values('Rajeev', 'ML', 'A')''')
cursor.execute('''Insert Into STUDENT Values('Naveen', 'AI', 'A')''')
cursor.execute('''Insert Into STUDENT Values('Kiran', 'Data Science', 'B')''')


print("The Inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
    
connection.commit()
connection.close()
