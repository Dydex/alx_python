"""
This is module help list all states from the database
"""
import MySQLdb

if __name__ == '__main__':

    # Connect to the MySQL server
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Dydex1590$',
        db='hbtn_0e_0_usa'
    )

# Create a cursor object
cursor = database.cursor()

# Execute the SQL query
cursor.execute('SELECT * FROM states ORDER BY id ASC')

# Fetch all the rows
states = cursor.fetchall()

# Display the results
for state in states:
    print(state)

# Close the cursor and database connection
cursor.close()
database.close()
