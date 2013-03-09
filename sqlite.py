import sqlite3 as dbapi

# connect to my SQLite database file
connection = dbapi.connect('portal.sqlite')

# create a cursor for interacting with the database
cursor = connection.cursor()

# execute SQL queries or commands
cursor.execute('''SELECT * FROM species''')

# we can loop over the cursor to get the results, row by row
for row in cursor:
    print row