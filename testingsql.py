import psycopg2

# Testing RDS

# Connection to RDS
connection = psycopg2.connect(
    host = '',
    port = '',
    user = '',
    password = '',
    database=''
    )

# Creating a SQL Query
sql = """CREATE TABLE languages(
id SERIAL PRIMARY KEY,
language text,
difficulty integer,
level integer)
"""

sql_drop = """DROP TABLE languages"""

sql_select = """SELECT difficulty from languages"""

# Allows Python to connect to database and stays
# connected the entire lifetime of the session
cursor=connection.cursor()
if (cursor):
    print ('Created the connection.')
else:
    print ('Failed to create connection.')

if (cursor.execute(sql_drop)):
    print ('Created the table')

# Commiting
connection.commit()
