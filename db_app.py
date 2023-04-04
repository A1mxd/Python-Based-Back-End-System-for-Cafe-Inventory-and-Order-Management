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
def short_pause():
    time.sleep(2)
    return

current_connection = None

def get_connection():
    global current_connection
    if current_connection == None:
        current_connection = pymysql.connect( 
        host = host_name, database = database_name,
        user = user_name, password = user_password )

    return current_connection

def close_connection():
    global current_connection
    if current_connection:
        current_connection.close()
        current_connection = None


                                         ############## Product Section ###################

def new_product_db(new_product, new_price):
    try:
        connection = get_connection()
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
        close_connection()
        return product_number
        
    except Exception as ex:
        print('Failed to open connection', ex)
        

def load_product_db():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute('SELECT product_id, product_name, product_price FROM product ORDER BY product_id ASC')

        rows = cursor.fetchall()
        cursor.close()
        close_connection()
        if not rows:
            return
        product_list = []
        for product in rows:
            product_info = {'product_id': product[0],
                            "name": product[1],
                            "price": product[2]}
            product_list.append(product_info)
        return product_list
    except Exception as ex:
        print('Failed to open connection', ex)
        time.sleep(4)

def update_product_both_db(product_id, product_name, product_price):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            UPDATE product SET product_name = %s, product_price = %s WHERE product_id = %s;
            """
        product_values = (product_name, product_price, product_id)
        
        cursor.execute(sql, product_values)
        connection.commit()
        cursor.close()
        close_connection()
    except Exception as ex:
        print('Failed to open connection', ex)

        
#todo try find the row 1 error
def update_product_name_db(product_id, product_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            UPDATE product SET product_name = %s WHERE product_id = %s;
            """
        product_values = (product_name, product_id)
        
        cursor.execute(sql, product_values)
        connection.commit()
        cursor.close()
        close_connection()
    except Exception as ex:
        print('Failed to open connection', ex)


def update_product_price_db(product_id, product_price):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            UPDATE product SET product_price = %s WHERE product_id = %s;
            """
        product_values = (product_price, product_id)
        
        cursor.execute(sql, product_values)
        connection.commit()
        cursor.close()
        close_connection()
    except Exception as ex:
        print('Failed to open connection', ex)



def delete_product_db(product_id):
    try:
        connection = get_connection()
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
        close_connection()
        if not rows:
            return
        last_product_number = rows[-1][0]
        return last_product_number
    except Exception as ex:
        print('Failed to open connection', ex)


                                     ############## Courier Section ###################

def new_courier_db(new_name, new_number):
    try:
        connection = get_connection()
        cursor = connection.cursor()

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
        close_connection()
        return courier_number
        
    except Exception as ex:
        print('Failed to open connection', ex)
        time.sleep(4)


def load_courier_db():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT courier_id, courier_name, courier_number FROM courier ORDER BY courier_id ASC')

        rows = cursor.fetchall()
        cursor.close()
        close_connection()
        if not rows:
            return
        courier_list = []
        for courier in rows:
            courier_info = {'courier_id': courier[0],
                            "courier_name": courier[1],
                            "courier_number": courier[2]}
            courier_list.append(courier_info)
        
        return courier_list
    except Exception as ex:
        print('Failed to open connection', ex)
9

def update_courier_both_db(courier_id, courier_name, courier_number):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            UPDATE courier SET courier_name = %s, courier_number = %s WHERE courier_id = %s;
            """
        courier_values = (courier_name, courier_number, courier_id)
        
        cursor.execute(sql, courier_values)
        connection.commit()
        cursor.close()
        close_connection()
    except Exception as ex:
        print('Failed to open connection', ex)


def update_courier_name_db(courier_id, courier_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            UPDATE courier SET courier_name = %s WHERE courier_id = %s;
            """
        courier_values = (courier_name, courier_id)
        
        cursor.execute(sql, courier_values)
        connection.commit()
        cursor.close()
        close_connection()
    except Exception as ex:
        print('Failed to open connection', ex)

def update_courier_number_db(courier_id, courier_number):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            UPDATE courier SET courier_number = %s WHERE courier_id = %s;
            """
        courier_values = (courier_number, courier_id)
        
        cursor.execute(sql, courier_values)
        connection.commit()
        cursor.close()
        close_connection()
    except Exception as ex:
        print('Failed to open connection', ex)
    # finally:
    #     close_connection()

def delete_courier_db(courier_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            DELETE FROM courier WHERE courier_id = %s;
            """
        courier_values = courier_id
        
        cursor.execute(sql, courier_values)
        connection.commit()
        cursor.execute('SELECT courier_id FROM courier')

        rows = cursor.fetchall()
        cursor.close()
        close_connection()
        if not rows:
            return
        last_product_number = rows[-1][0]
        return last_product_number
    except Exception as ex:
        print('Failed to open connection', ex)


                                     ############## Order Section ###################

def new_order_db(new_name, new_number, new_address, courier, status, items):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            INSERT INTO orders (customer_name, customer_phone, customer_address, courier_id, order_status_id, items)
            VALUES (%s, %s,%s,%s,%s,%s);
            """
        order_values = (new_name, new_number, new_address, courier, status, items)

        cursor.execute(sql, order_values)
        connection.commit()
        cursor.execute('SELECT order_id FROM orders')

        rows = cursor.fetchall()
        order_number = rows[-1][0]
        cursor.close()
        close_connection()
        return order_number
        
    except Exception as ex:
        print('Failed to open connection', ex)
        short_pause()

def load_order_db():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT o.order_id, o.customer_name, o.customer_phone, o.customer_address, o.courier_id, os.order_status, o.items \
                        FROM orders o \
                        INNER JOIN order_status os ON os.order_status_id = o.order_status_id \
                        ORDER BY o.order_id ASC')

        rows = cursor.fetchall()
        cursor.close()
        close_connection()
        order_list = []
        if not rows:
            return order_list
        for order in rows:
            order_info = {'order_id': order[0],
                        'customer_name': order[1],
                        "customer_phone": order[2],
                        "customer_address": order[3],
                        "courier_index": order[4],
                        "status": order[5],
                        "items": order[6]} 
            order_list.append(order_info)
        
        return order_list
    except Exception as ex:
        print('Failed to open connection', ex)
        short_pause()

def load_order_status_db():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT  order_status_id, order_status FROM order_status ORDER BY order_status_id ASC')

        rows = cursor.fetchall()
        cursor.close()
        close_connection()
        order_status_list = []
        if not rows:
            return order_status_list
        for order in rows:
            order_info = {'order_status_id': order[0],
                        'status_type': order[1]}
                        
            order_status_list.append(order_info)
        return order_status_list
    except Exception as ex:
        print('Failed to open connection', ex)
        short_pause()


def update_order_db(order_id, customer_input, column_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            UPDATE orders SET {} = %s WHERE order_id = %s;
            """.format(column_name)
        order_values = ( customer_input, order_id)
        
        cursor.execute(sql, order_values)
        connection.commit()
        cursor.close()
        close_connection()
    except Exception as ex:
        print('Failed to open connection', ex)
        short_pause()

def delete_order_db(order_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            DELETE FROM orders WHERE order_id = %s;
            """
        courier_values = order_id
        
        cursor.execute(sql, courier_values)
        connection.commit()
        cursor.execute('SELECT courier_id FROM courier')

        rows = cursor.fetchall()
        cursor.close()
        close_connection()
        if not rows:
            return
        last_product_number = rows[-1][0]
        return last_product_number
    except Exception as ex:
        print('Failed to open connection', ex)

def load_order_filter_db(column_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT o.order_id, o.customer_name, o.customer_phone, o.customer_address, o.courier_id, os.order_status, o.items \
                        FROM orders o \
                        INNER JOIN order_status os ON os.order_status_id = o.order_status_id \
                        ORDER BY {} ASC'. format(column_name) )

        rows = cursor.fetchall()
        cursor.close()
        close_connection()
        order_list = []
        if not rows:
            return order_list
        for order in rows:
            order_info = {'order_id': order[0],
                        'customer_name': order[1],
                        "customer_phone": order[2],
                        "customer_address": order[3],
                        "courier_index": order[4],
                        "status": order[5],
                        "items": order[6]} 
            order_list.append(order_info)
        
        return order_list
    except Exception as ex:
        print('Failed to open connection', ex)
        short_pause()

    

