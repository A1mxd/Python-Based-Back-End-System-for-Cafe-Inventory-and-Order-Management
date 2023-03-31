import pymysql
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

# todo the update and load and delete in my functions and app properly
# todo this function
# current_connection = None

# def get_connection():
#     global current_connection
#     if current_connection == None:
#         current_connection = pymysql.connect( 
#         host = host_name, database = database_name,
#         user = user_name, password = user_password )
#         return current_connection

# def close_connection():
#     global current_connection
#     if current_connection:
#         current_connection.close()
#         current_connection = None
# def get_connection():
#     global current_connection
#     # Optional print statements
#     if current_connection:
#         print('connection already running')
#     else:
#         print('new connection starting')
#     if current_connection == None:
#         current_connection = pymysql.connect(host=host_name, database=database_name,
#                                              user=user_name, password=user_password)
    
#     return current_connection


# def close_connection():
#     if current_connection:
#         current_connection.close()
#         print('Connection closed')
        

                                         ############## Product Section ###################

def new_product_db(new_product, new_price):
    try:
        with pymysql.connect(
            host = host_name, database = database_name,
            user = user_name, password = user_password
            ) as connection:
            cursor = connection.cursor()

            
            sql = """
                INSERT INTO product (product_name, product_price)
                VALUES (%s, %s);
                """
            product_values = (new_product, new_price)

            cursor.execute(sql, product_values)
            connection.commit()
            cursor.execute('SELECT product_id FROM product')

            rows = cursor.fetchall()
            product_number = rows[-1][0]
            cursor.close()
            return product_number
        
    except Exception as ex:
        print('Failed to open connection', ex)
    # finally:
    #     close_connection()
        

def load_product_db():
    try:
        with pymysql.connect(
            host = host_name, database = database_name,
            user = user_name, password = user_password
            ) as connection:
            cursor = connection.cursor()
            
            cursor.execute('SELECT product_id, product_name, product_price FROM product ORDER BY product_id ASC')

            rows = cursor.fetchall()
            cursor.close()
            print(rows)
            if not rows:
                return
            # product_list = []
            # for product in rows:
            #     product_info = {'product_id': rows[0],
            #                     "name": rows[1],
            #                     "price": rows[2]}
            #     product_list.append(product_info)
            return rows
    except Exception as ex:
        print('Failed to open connection', ex)
        time.sleep(4)
    # finally:
    #     close_connection()

def update_product_both_db(product_id, product_name, product_price):
    try:
        with pymysql.connect(
            host = host_name, database = database_name,
            user = user_name, password = user_password
            ) as connection:
            cursor = connection.cursor()

            sql = """
                UPDATE product SET product_name = %s, product_price = %s WHERE product_id = %s;
                """
            product_values = (product_name, product_price, product_id)
            
            cursor.execute(sql, product_values)
            connection.commit()
            cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)
    # finally:
    #     close_connection()
        
#todo try find the row 1 error
def update_product_name_db(product_id, product_name):
    try:
        with pymysql.connect(
            host = host_name, database = database_name,
            user = user_name, password = user_password
            ) as connection:
            cursor = connection.cursor()

            sql = """
                UPDATE product SET product_name = %s WHERE product_id = %s;
                """
            product_values = (product_name, product_id)
            
            cursor.execute(sql, product_values)
            connection.commit()
            cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)
    # finally:
    #     close_connection()

def update_product_price_db(product_id, product_price):
    try:
        with pymysql.connect(
            host = host_name, database = database_name,
            user = user_name, password = user_password
            ) as connection:
            cursor = connection.cursor()

            sql = """
                UPDATE product SET product_price = %s WHERE product_id = %s;
                """
            product_values = (product_price, product_id)
            
            cursor.execute(sql, product_values)
            connection.commit()
            cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)
    # finally:
    #     close_connection()


def delete_product_db(product_id):
    try:
        with pymysql.connect(
            host = host_name, database = database_name,
            user = user_name, password = user_password
            ) as connection:
            cursor = connection.cursor()

            sql = """
                DELETE FROM product WHERE product_id = %s;
                """
            product_values = (product_id)
            
            cursor.execute(sql, product_values)
            connection.commit()
            cursor.execute('SELECT product_id FROM product')

            rows = cursor.fetchall()
            cursor.close()
            if not rows:
                return
            last_product_number = rows[-1][0]
            return last_product_number
    except Exception as ex:
        print('Failed to open connection', ex)
    # finally:
    #     close_connection()

                                     ############## Courier Section ###################

def new_courier_db(new_name, new_number):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:

            sql = """
                INSERT INTO courier (courier_name, courier_number)
                VALUES (%s, %s);
                """
            courier_values = (new_name, new_number)

            cursor.execute(sql, courier_values)
            connection.commit()
            cursor.execute('SELECT courier_id FROM courier')

            rows = cursor.fetchall()
            courier_number = rows[-1][0]
            cursor.close()
            return courier_number
        
    except Exception as ex:
        print('Failed to open connection', ex)
        time.sleep(4)
    finally:
        close_connection()

def load_courier_db():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:

            cursor.execute('SELECT courier_id, courier_name, courier_number FROM courier ORDER BY courier_id ASC')

            rows = cursor.fetchall()
            cursor.close()
            if not rows:
                return
            courier_list = []
            for courier in rows:
                courier_info = {'courier_id': rows[0],
                                "courier_name": rows[1],
                                "courier_number": rows[2]}
                courier_list.append(courier_info)
            return courier_list
    except Exception as ex:
        print('Failed to open connection', ex)
    finally:
        close_connection()

def update_courier_both_db(courier_id, courier_name, courier_number):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:

            sql = """
                UPDATE courier SET courier_name = %s, courier_number = %s WHERE courier_id = %s;
                """
            courier_values = (courier_name, courier_number, courier_id)
            
            cursor.execute(sql, courier_values)
            connection.commit()
            cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)
    finally:
        close_connection()

def update_courier_name_db(courier_id, courier_name):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:

            sql = """
                UPDATE courier SET courier_name = %s WHERE courier_id = %s;
                """
            courier_values = (courier_name, courier_id)
            
            cursor.execute(sql, courier_values)
            connection.commit()
            cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)
    finally:
        close_connection()

def update_courier_number_db(courier_id, courier_number):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:

            sql = """
                UPDATE courier SET courier_number = %s WHERE courier_id = %s;
                """
            courier_values = (courier_number, courier_id)
            
            cursor.execute(sql, courier_values)
            connection.commit()
            cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)
    finally:
        close_connection()

def delete_courier_db(courier_id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:

            sql = """
                DELETE FROM courier WHERE courier_id = %s;
                """
            courier_values = courier_id
            
            cursor.execute(sql, courier_values)
            connection.commit()
            cursor.execute('SELECT courier_id FROM courier')

            rows = cursor.fetchall()
            cursor.close()
            if not rows:
                return
            last_product_number = rows[-1][0]
            return last_product_number
    except Exception as ex:
        print('Failed to open connection', ex)
    finally:
        close_connection()




# def print_menu(product_list):

#     for row in product_list:
#         print(f'product_id: {str(product[0])}, name: {row[1]}, price: £{row[2]}')

