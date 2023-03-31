import time
import csv
import json

from functions import * 
from db_app import *    

# need to try for all the input ones 
if __name__ == '__main__':
    
#TODO: need to do options in string rather than integer for less errors and problem if i am not using it or to store 
# Main Menu #
    while True:
        clear_screen()
        m_user_input = Main_menu_user_input()
        if m_user_input == 1:
    
        #Products Menu#
            while True:
                clear_screen()
                pm_user_input = Product_menu_input()
                if pm_user_input == 0:
                    clear_screen()
                    print('\t***Returning to main menu***')
                    short_pause()
                    break

                elif pm_user_input == 1:
                    clear_screen()
                    product_list = load_product_db()
                    print_products(product_list)
                    if product_list == None:
                        continue
                    short_pause()
                    continue

                # CREATE new product
                elif pm_user_input == 2:
                    clear_screen()
                    print('\t***Input New Product***')
                    try:
                        new_product = input('Input the new product: ')
                        new_price = float(input('\nInput the new product price: £'))
                    except:
                        clear_screen()
                        print('\t***Invalid price inputted***')
                        short_pause()
                        continue
                    #todo
                    new_products(new_product, new_price)
                    product_list = load_product_db()
                    print_products(product_list)
                    short_pause()
                    continue

                # UPDATE existing product
                elif pm_user_input == 3:
                    clear_screen()
                    product_list = load_product_db()
                    print_index_products(product_list)
                    if product_list == None:
                        continue
                    try:
                        index_user_input = int(input('\nInput the index value of the product: '))
                        if index_user_input <= product_list[-1][0] and not index_user_input<= 0:  
                            try:
                                update_product(index_user_input)
                            except ValueError:
                                value_error()
                                continue
                            product_list = load_product_db()
                            short_pause()
                            clear_screen()
                            full_menu_product(product_list)
                            short_pause()
                            continue
                        else :
                            invalid_input()
                            continue
                    except ValueError:
                        value_error()
                        continue
                    
                # DELETE product
                elif pm_user_input == 4:
                    clear_screen()
                    product_list = load_product_db()
                    print_index_products(product_list)
                    if product_list == None:
                        continue
                    try:
                        delete_products = int(input('\n\nInput the index value of the product to delete: '))
                    except ValueError:
                        value_error()
                        continue
                    delete_product(product_list, delete_products)
                    continue

                # Full menu with prices
                elif pm_user_input == 5:
                    clear_screen()
                    product_list = load_product_db()
                    full_menu_product(product_list)
                    if product_list == None:
                        continue
                    short_pause()
                    continue

                #Not an integer
                elif pm_user_input == 999999:
                    clear_screen()
                    print('\t***That was not a number***')
                    short_pause()
                    clear_screen()
                    continue

                else:
                    clear_screen()
                    print('\t***Invalid Input***')
                    short_pause()
                    clear_screen()
                continue

        # Orders Menu ##    
        elif m_user_input == 2:
            clear_screen()
            # Returns to main menu from order menu
        
            while True:
                clear_screen()
                om_user_input = Order_menu_function()  
                # return to main menu     
                if om_user_input == 0:
                    return_main()
                    break

                # Print orders
                elif om_user_input == 1:
                    print_orders(order_list)
                    long_pause()
                    continue

                # New order
                elif om_user_input == 2:
                    clear_screen()
                    print('\t***Input New Order***')
                    customer_name = input('Input your name: ')
                    customer_address = input('Input your address: ')
                    # TODO: need to make it 11 digit number
                    customer_phone = input('Input your phone number: ')
                    clear_screen()
                    product_list=load_product_db()
                    print_index_products(product_list)
                    if product_list == None:
                        continue
                    items_chosen = input('Input all the product items index with comma separating (eg. 3, 2, 1) \
                                         \n\nInput the product index: ')
                    clear_screen()
                    courier_list = load_courier_db()
                    print_courier_list(courier_list)
                    if courier_list == None:
                        continue
                    try:
                        courier_index = int(input(f'\nInput the courier index: '))
                    except ValueError:
                        value_error()
                        continue
                    new_order(customer_name, customer_address, customer_phone, courier_index, items_chosen)
                    save_order(order_list)
                    clear_screen()
                    print_orders(order_list)
                    long_pause()
                    continue

                elif om_user_input == 3:
                    update_order_status(order_list)
                    update_saved_order(order_list)
                    continue

                elif om_user_input == 4:
                    update_order(order_list)
                    update_saved_order(order_list)
                    continue
                
                # DELETE order
                elif om_user_input == 5:
                    delete_order(order_list)
                    update_saved_order(order_list)
                    continue
                
                #Not an integer
                elif om_user_input == 999999:
                    clear_screen()
                    print('\t***That was not a number***')
                    short_pause()
                    clear_screen()
                    continue

                else:
                    clear_screen()
                    print('\t***Invalid Input***')
                    short_pause()
                    clear_screen()
                    continue
        

        elif m_user_input == 3:
            clear_screen()
            while True:
                clear_screen()
                cm_user_input =Courier_menu_function()  
                # return to main menu     
                if cm_user_input == 0:
                    return_main()
                    break

                # PRINT couriers list
                elif cm_user_input == 1:
                    clear_screen()
                    courier_list = load_courier_db()
                    if courier_list == None:
                        print_courier_list(courier_list)
                        continue
                    print('\t***Courier List***')
                    print_courier_list(courier_list)
                    short_pause()
                    continue

                # CREATE new courier
                elif cm_user_input == 2:
                    clear_screen()
                    print('\t***Input New Courier***')
                    courier_name = input('Input your name: ')
                    courier_number = input('Input the number: ')
                    new_courier(courier_name, courier_number)
                    courier_list = load_courier_db()
                    save_courier(courier_list)
                    short_pause()
                    continue

                # UPDATE existing courier
                elif cm_user_input == 3:
                    clear_screen()
                    courier_list = load_courier_db()
                    print_courier_list(courier_list)
                    if courier_list == None:
                        continue
                    update_courier = int(input('Input the index value of the courier: '))
                    update_courier_list(update_courier)
                    update_saved_courier(courier_list)
                    clear_screen()
                    print('\t***Updated Courier***')
                    short_pause()
                    continue

                # DELETE courier
                elif cm_user_input == 4:
                    clear_screen()
                    courier_list = load_courier_db()
                    print_courier_list(courier_list)
                    if courier_list == None:
                        continue
                    try:
                        delete_couriers = int(input('\n\nInput the index value of the courier to delete: '))
                    except ValueError:
                        value_error()
                        continue
                    delete_courier(courier_list, delete_couriers)
                    update_saved_courier(courier_list)
                    continue
                
                #Not an integer
                elif cm_user_input == 999999:
                    clear_screen()
                    print('\t***That was not a number***')
                    short_pause()
                    clear_screen()
                    continue
                    
                else:
                    clear_screen()
                    print('\t***Invalid Input***')
                    short_pause()
                    clear_screen()
                    continue
        
        #Not an integer
        elif m_user_input == 999999:
            clear_screen()
            print('\t***That was not a number***')
            short_pause()
            clear_screen()
            continue

        # Ending the whole code and loop 
        elif m_user_input == 0:
            exit_app()

        # Incorrect inputs and return back to while loop
        else :
            clear_screen()
            print('\t***Invalid Input***')
            short_pause()
            clear_screen()
            continue
                    
        
        
       

        






