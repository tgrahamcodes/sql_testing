import psycopg2

# Connecting to RDS
connection = psycopg2.connect(
    host = '',
    port = '',
    user = '',
    password = '',
    database=''
    )

# Creating a SQL table
sql_table = """CREATE TABLE languages(
id SERIAL PRIMARY KEY,
language text,
difficulty integer,
level integer)
"""

# Testing various SQL functions
# sql_insert = """INSERT INTO languages(id, language, difficulty, level) VALUES('4', 'Python', '2', '4')"""
sql_insert = """INSERT INTO languages(id, language, difficulty, level) VALUES('1', 'JavaScript', '2', '4')"""

sql_drop = """DROP TABLE languages"""
sql_select = """SELECT * FROM languages;"""

# Cursor allows python to connect to the database
cursor=connection.cursor()

if (cursor):
    print ('\nCreated the connection.')
    print ('\nRetrieving data...\n')
else:
    print ('Failed to create connection.')

#cursor.execute(sql_table)
#cursor.execute(sql_insert)
cursor.execute(sql_select)
for language in cursor:
    print (language)

print()

# Commiting the actual commands
connection.commit()

if __name__ == "__main__":
    pass
