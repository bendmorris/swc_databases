import sqlite3 as dbapi

# connect to my SQLite database file
connection = dbapi.connect('portal.sqlite')

# create a cursor for interacting with the database
cursor = connection.cursor()

# execute SQL queries or commands
cursor.execute(''' 
SELECT SUM(wgt) 
FROM main 
WHERE yr > 2000 AND wgt IS NOT NULL
GROUP BY species
ORDER BY SUM(wgt) DESC
''')

# create a list with the first value from every row
values = [row[0] for row in cursor]

# plot the values using matplotlib
import pylab as p
p.plot(range(1, 1+len(values)), values)
p.xlim(1, len(values))
p.yscale('log')
p.show()