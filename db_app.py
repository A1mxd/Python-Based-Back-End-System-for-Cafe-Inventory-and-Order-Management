import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

def save_product_db(product_list, new_product, new_price):
    try:
        # TODO Establish a database connection
        # Hint: use "with ..."
        with pymysql.connect(
            host = host_name, database = database_name,
            user = user_name, password = user_password
            ) as connection:

            # TODO open a cursor
            cursor = connection.cursor()



            # TODO Add code here to insert a new record
            sql = """
                INSERT INTO `product` (`name`, `price`)
                VALUES (%s, %s,)
                """
            data_values = (new_product, new_price)

            cursor.execute(sql, data_values)
            connection.commit()


            # TODO Add code here to select all the records
            cursor.execute('SELECT product_id, name, price FROM person ORDER BY person_id ASC')
            rows = cursor.fetchall()


            for row in rows:
                print(f'product_id: {str(row[0])}, name: {row[1]}, price: {row[2]}')


            # TODO close the cursor
            cursor.close()



        # The connection will automatically close here
    except Exception as ex:
        print('Failed to open connection', ex)

def update_product_db(product_list, new_product, new_price):
    try:
        # TODO Establish a database connection
        # Hint: use "with ..."
        with pymysql.connect(
            host = host_name, database = database_name,
            user = user_name, password = user_password
            ) as connection:


            
            # TODO open a cursor
            cursor = connection.cursor()



            # TODO Add code here to insert a new record
            sql = """
                INSERT INTO `product` (`name`, `price`)
                VALUES (%s, %s,)
                """
            data_values = (new_product, new_price)

            cursor.execute(sql, data_values)
            connection.commit()



            # TODO Add code here to select all the records
            cursor.execute('SELECT product_id, name, price FROM person ORDER BY person_id ASC')
            rows = cursor.fetchall()


            for row in rows:
                print(f'product_id: {str(row[0])}, name: {row[1]}, price: {row[2]}')


            # TODO close the cursor
            cursor.close()



        # The connection will automatically close here
    except Exception as ex:
        print('Failed to open connection', ex)