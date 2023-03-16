import time
import csv
import json

from functions import * 
     
#order number variable start
#order number (doesnt work in the function files cos of global)
def order_number():
    global no
    no += 1

def Main_menu_user_input():
    global m_user_input
    print('\t***Main Menu options***')
    m_user_input = int(input('(0) to exit \
                             \n(1) for products menu \
                             \n(2) for order menu \
                             \n(3) for courrier\n\n\n\
                             \nType a number: '))

def Product_menu_input():
    global pm_user_input
    print('\t***Product Menu Options***')
    pm_user_input =  int(input('(0) to return to main menu \
                                \n(1) for product list \
                                \n(2) to create new product \
                                \n(3) to update existing product \
                                \n(4) to delete a product \
                                \n(5) for the full menu with prices \n\n\n\
                                \nType the number: '))

def Order_menu_function():
    global om_user_input
    print('\t***Order Menu Options***')
    om_user_input =  int(input('(0) to return to main menu \
                                \n(1) to print order \
                                \n(2) to order \
                                \n(3) to update existing order status \
                                \n(4) to update existing order \
                                \n(5) to delete order \n\n\n\
                                \nType the number: '))  

def print_index_products():
    global product_list
    global indx
    cafe_products = cafe_product.keys()
    product_list = {     
                    }
    for indx, products in enumerate(cafe_products):
                        print(f'{indx} : {products}')   
                        product_list[indx] = products

def full_menu_order():
    cafe_products = cafe_product.keys()
    cafe_price = cafe_product.values()
    for i, products in enumerate(cafe_products):
        for indx, price in enumerate(cafe_price):
            if i == indx:
                print(f'{products}: £{price:.2f}')
            else:
                continue
# need to try for all the input ones 

#TODO: fix my main menu into function and also check if the dictionary is fine for the order menu
# Main Menu #
while True:
    clear_screen()
    Main_menu_user_input()
    if m_user_input == 1:

        #Products Menu#
        while True:
            clear_screen()
            Product_menu_input()
            if pm_user_input == 0:
                clear_screen()
                print('\t***Returning to main menu***')
                short_pause()
                break

            elif pm_user_input == 1:
                clear_screen()
                print_products()
                continue

            # CREATE new product
            elif pm_user_input == 2:
                clear_screen()
                print('\t***Input New Product***')
                try:
                    new_product = input('Input the new product: ')
                    new_price = float(input('Input the new product price: £'))
                except:
                    print('Invalid Input')
                cafe_product[new_product] = new_price
                print_products()
                short_pause()
                continue

            # UPDATE existing product
            elif pm_user_input == 3:
                clear_screen()
                print('\t***Product List***')
                cafe_products = cafe_product.keys()
                print_index_products()
                indx_user_input = int(input('Input the index value of the product: '))
                if indx_user_input <= indx and not indx_user_input<= 0:  
                    #TODO: new menu for price update or name update  - below example
                    clear_screen()
                    old_product = str(product_list[indx_user_input])
                    print('\t***Update exisiting Product***')
                    customer_input = int(input('(1) to update product name \
                                                \n(2) to update product price\
                                                \n(3) to update both product price and name  \n\n\n\
                                                \nType the number:'))
                    
                    if customer_input == 1:
                        update_product_name = str(input('\nInput the new product name: '))
                        cafe_product[update_product_name] = cafe_product.pop(old_product)
                    elif customer_input == 2:
                        update_product_price = float(input('\nInput the new product price: '))
                        cafe_product[old_product]  = update_product_price
                    elif customer_input == 3:
                        update_product_name = str(input('\nInput the new product name: '))
                        cafe_product[update_product_name] = cafe_product.pop(old_product)
                        update_product_price = float(input('Input the new product price: £'))
                        cafe_product[old_product]  = update_product_price
                    else:
                        print('Invalid Input')
                    short_pause()
                    clear_screen()
                    full_menu_order()
                    short_pause()
                    continue
                else :
                    print('Invalid index')
                    continue
                
            # DELETE product
            elif pm_user_input == 4:
                cafe_products = cafe_product.keys()
                print_index_products()
                indx_user_input = int(input('Input the index value of the product: '))
                if indx_user_input <= indx:  
                    old_product = str(product_list[indx_user_input])
                    print(f'You chose the product {old_product} to delete.')
                    del cafe_product[old_product]
                    for products in cafe_product.keys():
                        print(products)
                    short_pause()             
                    continue
                else :
                    print('Invalid index')
                    continue

            # Full menu with prices
            elif pm_user_input == 5:
                full_menu_order()
                short_pause()
                continue
            
            else:
                print('Invalid Input')
            continue

    # Orders Menu ##    
    elif m_user_input == 2:
        clear_screen()
        # Returns to main menu from order menu
       
        
        while True:
            clear_screen()
            Order_menu_function()  
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
                continue
            elif om_user_input == 3:
                update_order()
                continue

            elif om_user_input == 4:
                update_order()
                continue

            elif om_user_input == 5:
                delete_order()
                continue
            else:
                print('Invalid Input')
                clear_screen()
                continue
    #TODO: need to start on the courier option
    elif m_user_input == 3:
        continue


                



    # Ending the whole code and loop 
    elif m_user_input == 0:
        exit_app()
    # Incorrect inputs and return back to while loop
    else :
        print('Invalid Input')
        continue






