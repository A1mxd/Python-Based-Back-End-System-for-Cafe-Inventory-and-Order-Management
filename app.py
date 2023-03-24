import time
import csv
import json

from functions import * 
     
#order number variable start
#order number (doesn't work in the function files cos of global)
def order_number():
    global no
    no += 1

# need to try for all the input ones 
if __name__ == '__main__':
    
#TODO: 
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
                    save_product()
                    print_products(product_list)
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
                    new_products(new_product, new_price)
                    save_product()
                    print_products(product_list)
                    short_pause()
                    continue

                # UPDATE existing product
                elif pm_user_input == 3:
                    clear_screen()
                    # cafe_products = cafe_product.keys()
                    print_index_products(product_list)
                    try:
                        index_user_input = int(input('\nInput the index value of the product: '))
                        if index_user_input <= len(product_list) and not index_user_input<= 0:  
                            try:
                                update_product(index_user_input)
                            except ValueError:
                                value_error()
                                continue
                            update_saved_product()
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
                    print_index_products(product_list)
                    try:
                        delete_products = int(input('\n\nInput the index value of the product to delete: '))
                    except ValueError:
                        value_error()
                        continue
                    delete_products -= 1
                    delete_product(delete_products)
                    update_saved_product()
                    continue

                # Full menu with prices
                elif pm_user_input == 5:
                    clear_screen()
                    save_product()
                    full_menu_product(product_list)
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
                    print_orders()
                    long_pause()
                    continue

                # New order
                elif om_user_input == 2:
                    clear_screen()
                    order_number()
                    print('\t***Input New Order***')
                    new_order()
                    save_order()
                    clear_screen()
                    print(f'\t***Your Order number is {no}***')
                    long_pause()
                    continue

                elif om_user_input == 3:
                    update_order_status()
                    update_saved_order()
                    continue
                elif om_user_input == 3:
                    update_order()
                    update_saved_order()
                    continue

                elif om_user_input == 4:
                    update_order()
                    update_saved_order()
                    continue
                # DELETE order
                elif om_user_input == 5:
                    delete_order()
                    update_saved_order()
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

        #TODO: need to start on the courier option
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
                    print('\t***Courier List***')
                    print_courier_list()
                    short_pause()
                    continue

                # CREATE new courier
                elif cm_user_input == 2:
                    clear_screen()
                    courier_name = input('Input your name: ')
                    courier_number = int(input('Input the number: '))
                    new_courier(courier_name, courier_number)
                    short_pause()
                    continue

                # UPDATE existing courier
                elif cm_user_input == 3:
                    clear_screen()
                    print_courier_list()
                    update_courier = int(input('Input the index value of the courier: '))
                    update_courier -= 1
                    update_courier_list(update_courier)
                    short_pause()
                    continue

                # DELETE courier
                elif cm_user_input == 4:
                    clear_screen()
                    print_courier_list()
                    try:
                        delete_couriers = int(input('\n\nInput the index value of the courier to delete: '))
                    except ValueError:
                        value_error()
                        continue
                    delete_couriers -= 1
                    delete_courier(delete_couriers)

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
                    
        
        
       

        






