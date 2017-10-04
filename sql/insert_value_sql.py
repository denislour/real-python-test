import sqlite3

# Create a connection
conn = sqlite3.connect('new.db')

# Create a cursor
cursor = conn.cursor()

# Insert values
cursor.execute("INSERT INTO population VALUES('New York City', \
	'NY', 8400000)")

cursor.execute("INSERT INTO population VALUES('San Francisco', \
	'CA', 8000000)")

# Commit database
conn.commit()

# Close connection
conn.close()