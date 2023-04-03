import os
import time
import csv
import json
from db_app import *

# Beginning cafe menu #

# Product list storage
# product_list = [{"name": "Chocolate Brownie",
#                 "price": 5.95},
#                 {"name": "Tea",
#                 "price": 1.20},
#                 {"name": "Decaffeinated Coffee",
#                 "price": 1.70},
#                 {"name": "Porridge",
#                 "price": 4.59}
#                 ]



                            ##############  Extra helpful function Section ###################
def invalid_input():
    clear_screen()
    print('\t***Invalid Input***')
    short_pause()
    clear_screen()

def value_error():
    clear_screen()
    print('\t***That was not a number***')
    short_pause()
    clear_screen()

#clearing previous input in terminal 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# exit app
def exit_app():
    print('\t***Exiting App***')
    exit()
#order number
def customer_number():
    global no
    no += 1

# long delay in code
def long_pause():
    time.sleep(4)
    return

#short delay in code
def short_pause():
    time.sleep(2)
    return

def return_main():
    clear_screen()
    print('\t***Returning to Main Menu***')
    time.sleep(2)
    return

def confirmation():
    print('Are you sure you want to delete it?')
    confirm = str(input('Confirm Y(yes)/N(no): ').lower())
    # empty_input_check(confirm)
    return confirm

                                     ############## Integer Input ###################
# get integer input
def get_int_input(text_input, num_options):
    while True:
        try:
            clear_screen()
            int_input =int(input(text_input))
            if int_input> num_options or int_input < 0:
                clear_screen()
                print('\t***That was an invalid option***')
                short_pause()
            else:
                return int_input
        except ValueError:
            value_error()
                                     ############## Menu Text ###################
# Main menu text
def Main_menu_text():
    m_user_input = '\t***Main Menu options***\t \
                            \n(0) to exit \
                            \n(1) for products menu \
                            \n(2) for order menu \
                            \n(3) for courier\n\n\n\
                            \nType a number: '
    return m_user_input

#Product Menu text
def Product_menu_text():
    pm_user_input =  '\t***Product Menu Options***\t \
                            \n(0) to return to main menu \
                            \n(1) for product list \
                            \n(2) to create new product \
                            \n(3) to update existing product \
                            \n(4) to delete a product \
                            \n(5) for the full menu with prices \n\n\n\
                            \nType the number: '
    return pm_user_input

#Order Menu text
def Order_menu_text():
    om_user_input = '\t***Order Menu Options***\t \
                        \n(0) to return to main menu \
                        \n(1) to print order \
                        \n(2) to create new order \
                        \n(3) to update existing order status \
                        \n(4) to update existing order \
                        \n(5) to delete order \n\n\n\
                        \nType the number: '
    return om_user_input

#Courier Menu text
def Courier_menu_text():
    cm_user_input = '\t***Courier Menu Options***\t \
                            \n(0) to return to main menu \
                            \n(1) to print courier list \
                            \n(2) to add new courier \
                            \n(3) to update existing courier \
                            \n(4) to delete courier \n\n\n\
                            \nType the number: '
    return cm_user_input

    
                                         ############## Product Section ###################

def new_products(name, price):
    index =new_product_db(name, price)
    clear_screen()
    print(f'\t***Product number: {index}***')
    short_pause()
    return

# Print products    
def print_products(product_list):
    clear_screen()
    if product_list == None:
        clear_screen()
        print('\t***No Product found in database***')
        short_pause()
        clear_screen()
        return
    print('\t***List of products in the menu***')

    for products in product_list:
        print(products['name'])

#print products with index
def print_index_products(product_list):
    if product_list == None:
        clear_screen()
        print('\t***No Product found in database***')
        short_pause()
        clear_screen()
        return
    print('\t***Product List***')
    for products in product_list:
        index = products['product_id']
        name = products['name']
        price = products["price"]
        print(f'Product id : {index} -  Name: {name}, Price: £{price:.2f}')
    


#specific update name or price
def customer_text_options():
    customer_input = '\t***Update Existing Product Options***\t \
                        \n(0) to cancel\
                        \n(1) to update product name\
                        \n(2) to update product price\
                        \n(3) to update both product price and name  \n\n\n\
                        \nType the number:'
    return customer_input

def update_product(product_id):
    product_list = load_product_db()
    if product_list == None:
        clear_screen()
        print('\t***No Product found in database***')
        short_pause()
        clear_screen()
        return
    clear_screen()
    c_text = customer_text_options()
    customer_input = get_int_input(c_text, 3)
    if customer_input == 0:
        return 21
    if customer_input == 1:
        update_product_name = str(input('\nInput the new product name: '))
        if update_product_name == '':
            invalid_input()
            return
        update_product_name_db(product_id, update_product_name)
    elif customer_input == 2:
        try:
            update_product_price = float(input('\nInput the new product price: £'))
        except ValueError:
            value_error()
            return
        update_product_price_db(product_id, update_product_price)
        

    elif customer_input == 3:
        update_product_name = str(input('\nInput the new product name: '))
        if update_product_name == '':
            invalid_input()
            return
        try:
            update_product_price = float(input('\nInput the new product price: £'))
        except ValueError:
            value_error()
            return
        update_product_both_db(product_id, update_product_name, update_product_price)
    else:
        invalid_input()
        return
    

def delete_product(product_list, delete_products):
    if product_list == None:
        clear_screen()
        print('\t***No Product found in database***')
        short_pause()
        clear_screen()
        return
    confirm = confirmation()
    if confirm == 'y' or confirm == 'yes':
        if  product_list[-1]['product_id'] >= delete_products and not delete_products <= 0:
            print('Deleting the product...')
            short_pause()
            last_delete =delete_product_db(delete_products)
            print('Deleted')
            short_pause()
            if last_delete == None:
                clear_screen()
                print('\t***No more products found in database***')
                short_pause()
                clear_screen()
                return
        else: 
            if product_list[-1]['product_id'] == 0:
                clear_screen()
                print('No product to delete')
                short_pause()
                return
            else:
                clear_screen()
                print('Invalid input')
                print(f'The last product was {product_list[-1]["product_id"]}')
                short_pause()
                return
    elif confirm == 'n' or confirm == 'no':
        print('Cancelled the deletion...')
        short_pause()
        print('Back to product menu')
        short_pause()
        return
    else:
        invalid_input()
        return   
    
def full_menu_product(product_list):
    product_list = load_product_db()
    if product_list == None:
        clear_screen()
        print('\t***No Product found in database***')
        short_pause()
        clear_screen()
        return
    print('\t***Full Product Menu***')
    for products in product_list:
        index = products['product_id']
        name = products['name']
        price = products["price"]
        print(f'Name: {name}, Price: £{price:.2f}')

def save_product(product_list):
    try:
        with open('products.json', 'w+') as products_file:
            for product in product_list:
                product['price'] = float(product['price'])
            json.dump(product_list, products_file, indent=4)
            
        products_file.close()
    except:
        clear_screen()
        print('File json error')
        short_pause()
        return
    return


                                         ############## Order Section ###################
def specific_orders(order_list):
    if order_list == []:
        clear_screen()
        print('\t***No orders to show***')
        short_pause()
        clear_screen()
        return 50
    c_text =  '\t***Sort Orders List Options***\t \
                        \n(0) to cancel\
                        \n(1) to sort by status(preparing first)\
                        \n(2) to sort by courier\
                        \n(3) to show  all orders information\n\n\n\
                        \nType the number:'
    customer_input = get_int_input(c_text, 3)
    clear_screen()
    if customer_input == 0:
        return 50
    elif customer_input == 1:
        column_name = 'os.order_status_id'
        order_filtered_list = load_order_filter_db(column_name)
        print('\t***List of Orders***')
        for orders in order_filtered_list:
            index = orders['order_id']
            name = orders['customer_name']
            status = orders['status']
            courier = orders['courier_index']
            items = orders['items']
            print(f'Order Number: {index} -Name: {name}, Courier number: {courier}, Status: {status}, items: {items}')
    elif customer_input == 2:
        column_name = 'o.courier_id'
        order_filtered_list =load_order_filter_db(column_name)
        print('\t***List of Orders***')
        for orders in order_filtered_list:
            index = orders['order_id']
            name = orders['customer_name']
            status = orders['status']
            courier = orders['courier_index']
            items = orders['items']
            print(f'Order Number: {index} -Name: {name}, Courier number: {courier}, Status: {status}, items: {items}')


    elif customer_input == 3:
        print_orders(order_list)




def print_orders(order_list):
    clear_screen()
    order_list = load_order_db()
    print('\t***List of Orders***')
    if order_list == []:
        clear_screen()
        print('\t***No orders to show***')
        short_pause()
        clear_screen()
        return 50
    for orders in order_list:
        index = orders['order_id']
        name = orders['customer_name']
        status = orders['status']
        address = orders['customer_address']
        phone = orders['customer_phone']
        courier = orders['courier_index']
        items = orders['items']
        print(f'Order Number: {index} - Name: {name}, address: {address}, Phone number: {phone}, Courier number: {courier}, Status: {status}, items: {items}')

def print_orders_status():
    clear_screen()
    order_status_list = load_order_status_db()
    
    if order_status_list == []:
        clear_screen()
        print('\t***No status type in Table***')
        short_pause()
        clear_screen()
        return
    print('\t**Status Type***')
    for status in order_status_list:
        index = status['order_status_id']
        status_type = status['status_type']
        print(f'Status id: {index} - Status type: {status_type}')

def phone_number_checker():
    while True: 
        try:
            customer_phone = input('Input your phone number: ')
            if len(customer_phone) == 11:
                try:
                    int_test = int(customer_phone)
                except ValueError:
                    value_error()
                    continue
                break
            else:
                clear_screen()
                print('\t***That was not 11 digits***')
                short_pause()
                continue
        except ValueError:
            value_error()
            continue
    return customer_phone

def item_chosen(product_list):
    while True:
        clear_screen()
        print_index_products(product_list)
        update_items_input = input('Input the chosen product items id with comma separating (eg. 3, 2, 1) \
                                    \n\nInput the product id: ')
        if update_items_input == '':
            invalid_input()
            continue
        try:
            update_items = [int(item.strip()) for item in update_items_input.split(',')]
            found = 0
            for items in update_items:
                for products in product_list:
                    if items == products['product_id']:
                        found = 1
                        continue
                continue
            if found != 1:
                clear_screen()
                print('\t***Invalid product id***\t')
                short_pause()
                continue
            else:
                return update_items_input
        except ValueError:
            invalid_input()
            short_pause()
            clear_screen()
            print('\t**Returning to order Menu**')
            short_pause()
            return 21

def new_order(customer_name, customer_address, customer_phone, courier_index, items_chosen):
    status = 1
    index= new_order_db(customer_name,  customer_phone, customer_address, courier_index,status, items_chosen)
    clear_screen()
    print(f'\t***Your Order number is {index}***')
    short_pause()
    return

def save_order(order_list):
    try:
        with open('orders.json', 'w+') as orders_file:
            json.dump(order_list, orders_file, indent=4)
            
        orders_file.close()
    except:
        clear_screen()
        print('File json error')
        short_pause()
        return
    return

    
def update_order_status(order_list):
    order_list= load_order_db()
    if order_list == []:
        return 50
    clear_screen()
    print('\t**Order Status***')
    #prints order number and status of the orders
    for orders in order_list:
        index = orders['order_id']
        status = orders['status']
        print(f'Order Number: {index}, Status: {status}')
    last_order = order_list[-1]['order_id']
    try:
        while True:
                clear_screen()
                print_orders(order_list)
                Customers_order =int(input('\nInput your order number: '))
                found = 0
                for order in order_list:
                    if Customers_order == order['order_id']:
                        found = 1
                        continue 
                if found != 1:
                    clear_screen()
                    print('\t***Invalid order number***\t')
                    short_pause()
                    continue
                else:
                    break
    except ValueError:
        invalid_input()
        short_pause()
        clear_screen()
        print('\t**Returning to order Menu**')
        short_pause()
        return 21
    if  last_order >= Customers_order and not Customers_order <= 0:
        print_orders_status()
        try:
            update_status_input = int(input('\nInput the index of the type of status: '))
        except ValueError:
            value_error()
            return 21
        if update_status_input == '':
            invalid_input()
            return 21
        column_name = 'order_status_id'
        update_order_db(Customers_order,update_status_input,column_name)
        # order_list[Customers_order]['status']  = update_status_input
    else: 
        print(f'Invalid input')
        print(f'The last order was {last_order}')
    short_pause()
    return

def update_order(order_list):
    order_list= load_order_db()
    #prints order number and name of the orders
    if order_list == []:
        return 50
    try:
        while True:
                clear_screen()
                print_orders(order_list)
                Customers_order =int(input('\nInput your order number: '))
                found = 0
                for order in order_list:
                    if Customers_order == order['order_id']:
                        found = 1
                        continue 
                if found != 1:
                    clear_screen()
                    print('\t***Invalid order number***\t')
                    short_pause()
                    continue
                else:
                    break
    except ValueError:
        invalid_input()
        short_pause()
        clear_screen()
        print('\t**Returning to order Menu**')
        short_pause()
        return
    print_orders(order_list)
    last_order = order_list[-1]['order_id']
    
    if  last_order >= Customers_order and not Customers_order <= 0:
        clear_screen()
        customer_text_options = '\t***Update customer Information Options****\t \
                                \n(0) to cancel \
                                \n(1) to change your name \
                                \n(2) to change your address\
                                \n(3) to change your number \
                                \n(4) to change your product items \
                                \n(5) to change your courier \n\n\n\
                                \nType the number: '
        customer_input = get_int_input(customer_text_options, 5)
        if customer_input == 0:
            return 21
        if customer_input == 1:
            update_name_input = str(input('\nInput the new name: '))
            if update_name_input == '':
                invalid_input()
                return
            column_name = 'customer_name'
            update_order_db(Customers_order,update_name_input,column_name)
        elif customer_input == 2:
            update_address_input = str(input('\nInput the new address: '))
            if update_address_input == '':
                invalid_input()
                return
            column_name = 'customer_address'
            update_order_db(Customers_order,update_address_input,column_name)
        elif customer_input == 3:
            update_number_input = phone_number_checker()
            # update_number_input = input('\nInput the new number: ')
            if update_number_input == '':
                invalid_input()
                return
            column_name = 'customer_phone'
            update_order_db(Customers_order,update_number_input,column_name)
        elif customer_input == 4:
            product_list = load_product_db()
            clear_screen()
            while True:
                clear_screen()
                print_index_products(product_list)
                update_items_input = input('\nInput the updated product items index with comma separating (eg. 3, 2, 1) \
                                            \n\nInput the updated product index: ')
                if update_items_input == '':
                    invalid_input()
                    continue
                try:
                    update_items = [int(item.strip()) for item in update_items_input.split(',')]
                    found = 0
                    for items in update_items:
                        for products in product_list:
                            if items == products['product_id']:
                                found = 1
                                continue
                        continue
                    if found != 1:
                        clear_screen()
                        print('\t***Invalid product id***\t')
                        short_pause()
                        continue
                    else:
                        break
                except ValueError:
                    invalid_input()
                    short_pause()
                    clear_screen()
                    print('\t**Returning to order Menu**')
                    short_pause()
                    return

            
            column_name = 'items'
            update_order_db(Customers_order,update_items_input,column_name)
        elif customer_input == 5:
            courier_list = load_courier_db()
            print_courier_list(courier_list)
            try:
                while True:
                    print_courier_list(courier_list)
                    update_courier_input = int(input(f'\nInput the courier index to change to: '))
                    if update_courier_input == '':
                        invalid_input()
                        continue
                    found = 0
                    for courier in courier_list:
                        if update_courier_input == courier['courier_id']:
                            found = 1
                            continue
                    # if found in the table the id then quit the function from the for loop
                    if found != 1:
                        clear_screen()
                        print('\t***Invalid Courier id***\t')
                        short_pause()
                        continue
                    # if found in the table the id then quit the function from the while loop
                    else:
                        break
            except ValueError:
                invalid_input()
                short_pause()
                clear_screen()
                print('\t**Returning to order Menu**')
                short_pause()
                return
            column_name = 'courier_id'
            update_order_db(Customers_order,update_courier_input,column_name)
        else:
            print('Invalid Input')
    else: 
        print(f'Invalid input')
        print(f'The last order is {last_order}')
    short_pause()
    return

def delete_order(order_list):
    order_list =load_order_db()
    print_orders(order_list)
    if order_list == []:
        return 50
    
    try:
        last_order = order_list[-1]['order_id']
        while True:
            clear_screen()
            print_orders(order_list)
            Customers_order =int(input('\nInput the order number to delete: '))
            found = 0
            for order in order_list:
                if Customers_order == order['order_id']:
                    found = 1
                    continue 
            if found != 1:
                clear_screen()
                print('\t***Invalid order number***\t')
                short_pause()
                continue
            else:
                break
        confirm = confirmation()
        if confirm == 'y' or confirm == 'yes':
            if  last_order >= Customers_order and not Customers_order <= -1:
                print('Deleting the order...')
                short_pause()
                delete_order_db(Customers_order)
                print('Deleted')
                short_pause()
            else: 
                print(f'Invalid input')
                print(f'The last order was {last_order}')
                short_pause()
        elif confirm == 'n' or confirm == 'no':
            print('Cancelled the deletion...')
            short_pause()
            print('Back to order menu')
            short_pause()
        else:
            print('Invalid input')
            short_pause()
    except ValueError:
        invalid_input()
        short_pause()
        clear_screen()
        print('\t**Returning to order Menu**')
        short_pause()
        return
    return


                                     ############## Courier Section ###################


def print_courier_list(courier_list):
    clear_screen()
    print('\t***Courier List***')
    if courier_list == None:
        clear_screen()
        print('\t***No couriers found in database***')
        short_pause()
        clear_screen()
        return 

    for courier in courier_list:
        index = courier['courier_id']
        name = courier['courier_name']
        number = courier["courier_number"]
        print(f'Courier id : {index} - Name: {name}, Number: {number}')
    

def new_courier(courier_name, courier_number):
    index = new_courier_db(courier_name, courier_number)
    clear_screen()
    print(f'\t***Courier number {index}***')
    short_pause()
    return

def update_courier_list(courier_index):
    courier_list = load_courier_db()
    clear_screen()
    if courier_list == None:
        clear_screen()
        print('\t***No couriers found in database***')
        short_pause()
        clear_screen()
        return 
    
    if courier_index <= courier_list[-1]['courier_id'] and not courier_index <= 0:
        found = 0
        for courier in courier_list:
            if courier_index == courier['courier_id']:
                found = 1
                continue
        # if found in the table the id then quit the function from the for loop
        if found != 1:
            clear_screen()
            print('\t***Invalid Courier id***\t')
            short_pause()
            return 21
        courier_text_options = '\t***Update existing Courier***\t \
                                    \n(0) to cancel \
                                    \n(1) to update Courier name \
                                    \n(2) to update Courier number\
                                    \n(3) to update both Courier name and number  \n\n\n\
                                    \nType the number: '
        courier_input = get_int_input(courier_text_options, 3)
        if courier_input == 0:
            return 50
        if courier_input == 1:
            update_courier_name = str(input('\nInput the new product name: '))
            if update_courier_name == '':
                invalid_input()
                return 21
            update_courier_name_db(courier_index, update_courier_name)
        elif courier_input == 2:

            try:
                update_courier_number = int(input('\nInput the new courier number: '))
                if update_courier_number == '':
                    invalid_input()
                    return 21
            except ValueError:
                value_error()
                return
            update_courier_name_db(courier_index, update_courier_number)
        elif courier_input == 3:
            update_courier_name = str(input('\nInput the new product name: '))
            if update_courier_name == '':
                invalid_input()
                return 21
            try:
                update_courier_number = int(input('\nInput the new courier number: '))
                if update_courier_number == '':
                    invalid_input()
                    return 21
            except ValueError:
                value_error()
                return
            update_courier_both_db(courier_index, update_courier_name, update_courier_number)
        else:
            return print('Invalid Input')
        courier_list = load_courier_db()
    else:
        clear_screen()
        print('\t***Invalid Courier Id chosen***')
        short_pause()
        return 21
    return

def delete_courier(courier_list, delete_couriers):
    if courier_list == None:
        clear_screen()
        print('\t***No couriers found in database***')
        short_pause()
        clear_screen()
        return 
    confirm = confirmation()
    if confirm == 'y' or confirm == 'yes':
        if  delete_couriers <= courier_list[-1]['courier_id'] and not delete_couriers <= 0:
            print('Deleting the courier...')
            short_pause()
            last_delete= delete_courier_db(delete_couriers)
            print('Deleted')
            short_pause()
            if last_delete == None:
                clear_screen()
                print('\t***No more couriers found in database***')
                short_pause()
                clear_screen()
                return
        else: 
            if courier_list[-1]['courier_id'] == 0:
                clear_screen()
                print('No couriers to delete')
                short_pause()
            else:
                clear_screen()
                courier_list = load_courier_db()
                print('Invalid input')
                print(f'The last courier was {courier_list[-1]["courier_id"]}')
                short_pause()
    elif confirm == 'n' or confirm == 'no':
        print('Cancelled the deletion...')
        short_pause()
        print('Back to courier menu')
        short_pause()
    else:
        print('Invalid input')
        short_pause()
    
def save_courier(courier_list):
    try:
        
        with open('couriers.json', 'w+') as couriers_file:
            json.dump(courier_list, couriers_file, indent=4)
            
        couriers_file.close()
    except:
        clear_screen()
        print('File json error')
        short_pause()
        return
    return

