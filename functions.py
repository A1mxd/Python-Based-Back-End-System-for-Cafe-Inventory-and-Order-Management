import os
import time
import csv
import json
# Beginning cafe menu #
# Product list storage
product_list = [{"name": "Chocolate Brownie",
                "price": 5.95},
                {"name": "Tea",
                "price": 1.20},
                {"name": "Decaffeinated Coffee",
                "price": 1.70},
                {"name": "Porridge",
                "price": 4.95}
                ]

# order number with customer info dictionary
order_list = []

# courier list
courier_list = []


no = 0

# Open the clean new file for orders
# order_file =open('orders.txt', 'w+')
# order_file.close

# # empty input checker for yes or no - delete option - TODO: try it out later
# def empty_input_check(input):
#     global check_input
#     global delete_couriers
#     while True:
#         if input == '':
#             print('Invalid empty input')
#             if check_input == 'order':
#                 delete_order()
#             elif check_input == 'courier':
#                 delete_courier(delete_couriers)
#             elif check_input == 'product':
#                 delete_product(delete_products)
#             # ADD  MORE VARIABLES FOR EMPTY INPUT CHECKER
#             else:
#                 break
#         else :
#             break
#     return 

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
def order_number():
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

                                     ############## Menu Input ###################
# Main menu input
def Main_menu_user_input():
    print('\t***Main Menu options***')
    try:
        m_user_input = int(input('(0) to exit \
                                \n(1) for products menu \
                                \n(2) for order menu \
                                \n(3) for courier\n\n\n\
                                \nType a number: '))
        return m_user_input
    except ValueError:
        m_user_input= 999999
        return m_user_input

#Product Menu Input
def Product_menu_input():
    print('\t***Product Menu Options***')
    try:
        pm_user_input =  int(input('(0) to return to main menu \
                                \n(1) for product list \
                                \n(2) to create new product \
                                \n(3) to update existing product \
                                \n(4) to delete a product \
                                \n(5) for the full menu with prices \n\n\n\
                                \nType the number: '))
        return pm_user_input
    except ValueError:
        pm_user_input = 999999
        return pm_user_input

#Order Menu Input
def Order_menu_function():
    print('\t***Order Menu Options***')
    try:
        om_user_input =  int(input('(0) to return to main menu \
                                \n(1) to print order \
                                \n(2) to order \
                                \n(3) to update existing order status \
                                \n(4) to update existing order \
                                \n(5) to delete order \n\n\n\
                                \nType the number: '))  
        return om_user_input
    except ValueError:
        om_user_input = 999999
        return om_user_input

#Courier Menu Input
def Courier_menu_function():
    print('\t***Courier Menu Options***')
    try:
        cm_user_input =  int(input('(0) to return to main menu \
                                    \n(1) to print courier list \
                                    \n(2) to add new courier \
                                    \n(3) to update existing courier \
                                    \n(4) to delete courier \n\n\n\
                                    \nType the number: '))  
        return cm_user_input
    except ValueError:
        cm_user_input = 999999
        return cm_user_input
    
                                         ############## Product Section ###################
def new_products(name, price):
    global product_list
    new_index = len(product_list)
    product_info = {"name": name,
                    "price": price }
    product_list.append(product_info)
    index= new_index + 1
    clear_screen()
    print(f'\t***Product number: {index}***')
    short_pause()
    return

# Print products    
def print_products(product_list):
    clear_screen()
    print('\t***List of products in the menu***')
    for products in product_list:
        print(products['name'])

#print products with index
def print_index_products(product_list):
    print('\t***Product List***')
    for index, products in enumerate(product_list):
        index += 1
        name = products['name']
        price = products["price"]
        print(f'Index Number: {index} -  Name: {name}, Price: {price:.2f}')

#specific update name or price
def customer_input_option():
    print('\t***Update existing Product***')
    customer_input = int(input('(1) to update product name \
                                \n(2) to update product price\
                                \n(3) to update both product price and name  \n\n\n\
                                \nType the number:'))
    return customer_input

def update_product(index_user_input):
    global product_list
    clear_screen()
    index_user_input -= 1
    old_product = product_list[index_user_input]
    customer_input = customer_input_option()
    if customer_input == 1:
        update_product_name = str(input('\nInput the new product name: '))
        old_product['name'] = update_product_name
    elif customer_input == 2:
        try:
            update_product_price = float(input('\nInput the new product price: £'))
        except ValueError:
            value_error()
            return
        old_product['price']  = update_product_price
    elif customer_input == 3:
        update_product_name = str(input('\nInput the new product name: '))
        old_product['name'] = update_product_name
        try:
            update_product_price = float(input('\nInput the new product price: £'))
        except ValueError:
            value_error()
            return
        old_product['price']  = update_product_price
    else:
        invalid_input()
        return
    

def delete_product(delete_products):
    global check_input
    global product_list
    check_input ='product'
    confirm = confirmation()
    if confirm == 'y' or confirm == 'yes':
        if  len(product_list) >= delete_products and not len(product_list) <= 0:
            print('Deleting the product...')
            short_pause()
            del product_list[delete_products]
            print('Deleted')
            short_pause()
        else: 
            if len(product_list) == 0:
                clear_screen()
                print('No couriers to delete')
                short_pause()
                return
            else:
                clear_screen()
                print('Invalid input')
                print(f'The last courier was {len(product_list)}')
                short_pause()
                return
    elif confirm == 'n' or confirm == 'no':
        print('Cancelled the deletion...')
        short_pause()
        print('Back to main menu')
        short_pause()
        return
    else:
        invalid_input()
        return   
    
def full_menu_product(product_list):
    print('\t***Full Product Menu***')
    for products in product_list:
        name = products['name']
        price = products["price"]
        print(f'Name: {name}, Price: {price:.2f}')

def save_product():
    with open('products.json', 'w+') as products_file:
        json.dump(product_list, products_file, indent=4)
        
    products_file.close()
    return

def update_saved_product():
    with open('products.json', 'w+') as products_file:
        json.dump(product_list, products_file, indent=4)
        
    products_file.close()
    return


                                         ############## Order Section ###################

def print_orders():
    global order_list
    clear_screen()
    for index, orders in enumerate(order_list):
        index += 1
        name = orders['customer_name']
        status = orders['status']
        address = orders['customer_address']
        phone = orders['customer_phone']
        print(f'Order Number: {index} - Name: {name}, address: {address}, Phone number: {phone}, Status: {status}')

def new_order(customer_name, customer_address, customer_phone):
    # print('\tAdding new order')
    global order_val
    new_index = len(order_list)
    status = 'Preparing'
    order_val = {'customer_name': customer_name,
                "customer_address": customer_address,
                "customer_phone": customer_phone,
                "status": status} 
    order_list.append(order_val)
    index= new_index + 1
    clear_screen()
    print(f'\t***Your Order number is {index}***')
    short_pause()
    return

def save_order():
        with open('orders.json', 'w+') as orders_file:
            json.dump(order_list, orders_file, indent=4)
            
        orders_file.close()

        return

def update_saved_order():
    with open('orders.json', 'w+') as orders_file:
        json.dump(order_list, orders_file, indent=4)
        
    orders_file.close()
    return
    
def update_order_status(order_list):
    clear_screen()
    print('\t**Order Status***')
    #prints order number and status of the orders
    for index, orders in enumerate(order_list):
        index += 1
        status = orders['status']
        print(f'Order Number: {index}, Status: {status}')

    last_order = len(order_list) + 1
    Customers_order =int(input('\n\n\nInput your order number: '))
    if  last_order >= Customers_order and not Customers_order <= 0:
        Customers_order -= 1
        update_status_input = str(input('Input the new status: '))
        order_list[Customers_order]['status']  = update_status_input
    else: 
        print(f'Invalid input')
        print(f'The last order was {last_order}')
    short_pause()
    return

def update_order(order_list):
    #prints order number and name of the orders
    print_orders()
    last_order = len(order_list) + 1
    Customers_order =int(input('Input your order number: '))
    if  last_order >= Customers_order and not Customers_order <= 0:
        Customers_order -= 1
        clear_screen()
        print('\t***Update customer Information***')
        customer_input = int(input('(1) to change your name \
                                \n(2) to change your address\
                                \n(3) to change your number \n\n\n\
                                \nType the number:'))
        if customer_input == 1:
            update_name_input = str(input('Input the new name: '))
            order_list[Customers_order]['customer_name']  = update_name_input
        elif customer_input == 2:
            update_address_input = str(input('Input the new address: '))
            order_list[Customers_order]['customer_address']  = update_address_input
        elif customer_input == 3:
            update_number_input = input('Input the new number: ')
            order_list[Customers_order]['customer_phone']  = update_number_input
        else:
            print('Invalid Input')
    else: 
        print(f'Invalid input')
        print(f'The last order is {last_order}')
    short_pause()
    return

def delete_order(order_list):
    global check_input
    print_orders()
    check_input ='order'
    try:
        last_order = len(order_list) + 1
        Customers_order =int(input('Input the order number to delete: '))
        confirm = confirmation()
        if confirm == 'y' or confirm == 'yes':
            Customers_order -= 1
            if  last_order >= Customers_order and not Customers_order <= -1:
                print('Deleting the product...')
                short_pause()
                del order_list[Customers_order]
                print('Deleted')
                short_pause()
            else: 
                print(f'Invalid input')
                print(f'The last order was {last_order}')
                short_pause()
        elif confirm == 'n' or confirm == 'no':
            print('Cancelled the deletion...')
            short_pause()
            print('Back to main menu')
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
def print_courier_list():
    global courier_list
    clear_screen()
    print('\t***Courier List***')
    for index, courier in enumerate(courier_list):
        index += 1
        name = courier['courier_name']
        number = courier["courier_number"]
        print(f'Courier number : {index} - Name: {name}, Number: {number}')
    

def new_courier(courier_name, courier_number):
    global courier_list
    new_index = len(courier_list)
    
    courier_info = {'courier_name': courier_name,
                "courier_number": courier_number
                }

    courier_list.append(courier_info)
    index = new_index + 1
    clear_screen()
    print(f'\t***Courier number {index}***')
    return

def update_courier_list(courier_index):
    global courier_list
    clear_screen()
    # courier = courier_list(courier_index)
    if courier_index >= 0 :
        print('\t***Update existing Courier***')
        courier_input = int(input('(1) to update Courier name \
                                    \n(2) to update Courier number\
                                    \n(3) to update both Courier name and number  \n\n\n\
                                    \nType the number:'))
        
        if courier_input == 1:
            update_courier_name = str(input('\nInput the new product name: '))
            courier_list[courier_index]['courier_name'] = update_courier_name
        elif courier_input == 2:
            update_courier_number = int(input('\nInput the new courier number: '))
            courier_list[courier_index]['courier_number'] = update_courier_number
        elif courier_input == 3:
            update_courier_name = str(input('\nInput the new product name: '))
            courier_list[courier_index]['courier_name'] = update_courier_name
            update_courier_number = int(input('\nInput the new courier number: '))
            courier_list[courier_index]['courier_number'] = update_courier_number
        else:
            return print('Invalid Input')
    else:
        return print('No couriers to update')
    return

def delete_courier(delete_couriers):
    global check_input
    global courier_list
    check_input ='courier'
    confirm = confirmation()
    if confirm == 'y' or confirm == 'yes':
        if  len(courier_list) >= delete_couriers and not len(courier_list) <= 0:
            print('Deleting the product...')
            short_pause()
            del courier_list[delete_couriers]
            print('Deleted')
            short_pause()
        else: 
            if len(courier_list) == 0:
                clear_screen()
                print('No couriers to delete')
                short_pause()
            else:
                clear_screen()
                print('Invalid input')
                print(f'The last courier was {len(courier_list)}')
                short_pause()
    elif confirm == 'n' or confirm == 'no':
        print('Cancelled the deletion...')
        short_pause()
        print('Back to main menu')
        short_pause()
    else:
        print('Invalid input')
        short_pause()
    
def save_courier():
    with open('couriers.json', 'w+') as couriers_file:
        json.dump(courier_list, couriers_file, indent=4)
        
    couriers_file.close()
    return

def update_courier():
    with open('couriers.json', 'w+') as couriers_file:
        json.dump(courier_list, couriers_file, indent=4)
        
    couriers_file.close()
    return   
