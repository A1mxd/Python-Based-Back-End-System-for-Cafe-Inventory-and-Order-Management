import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")


try:
    print('Opening connection...')
    # TODO Establish a database connection
    # Hint: use "with ..."
    with pymysql.connect(
        host = host_name, database = database_name,
        user = user_name, password = user_password
        ) as connection:


        # This bit won't compile till the "with" is done...
        print('Opening cursor...')
        # TODO open a cursor
        cursor = connection.cursor()



        print('Inserting new record...')
        # TODO Add code here to insert a new record
        sql = """
            INSERT INTO `person` (`first_name`, `last_name`, `age`, `email`)
            VALUES (%s, %s, %s, %s)
            """
        data_values = ('Aaliyah', 'Connor', 47, 'AaliyahConnor@teleworm.us')
        cursor.execute(sql, data_values)
        connection.commit()



        print('Selecting all records...')
        # TODO Add code here to select all the records
        cursor.execute('SELECT first_name, last_name, age FROM person ORDER BY person_id ASC')
        rows = cursor.fetchall()




        print('Displaying all records...')
        # TODO Add code here to print out all the records
        for row in rows:
            print(f'First Name: {str(row[0])}, Last Name: {row[1]}, Age: {row[2]}')




        print('Closing cursor...')
        # TODO close the cursor
        cursor.close()



    # The connection will automatically close here
except Exception as ex:
    print('Failed to open connection', ex)

# Leave this line here!
print('All done!')
