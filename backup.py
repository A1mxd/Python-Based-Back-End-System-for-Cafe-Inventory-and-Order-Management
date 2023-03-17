# might not be needed 
# def empty_input_check(input):
#     while True:
#         if input == '':
#             print('Invalid empty input')
#             if check_input == 'delete':
#                 delete_order()
#             # ADD  MORE VARIABLES FOR EMPTY INPUT CHECKER
#             else:
#                 break
#         else :
#             break

#     return 

# # class
# # class customer():
# #     def __init__(name, customer_address, phone, status):
# #         pass

# #clearing previous input in terminal 
# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# # exit app
# def exit_app():
#     print('\t***Exiting App***')
#     exit()

# #order number
# def order_number():
#     global no
#     no += 1
#     return no

# long delay in code
# def long_pause():
#     time.sleep(4)
#     return

# #short delay in code
# def short_pause():
#     time.sleep(2)
#     return

# def return_main():
#     clear_screen()
#     print('\t***Returning to Main Menu***')
#     time.sleep(2)
#     return

# def print_orders():
#     global order_list
#     global key
#     for key, orders in order_list.items():
#         name = orders['customer_name']
#         status = orders['status']
#         address = orders['customer_address']
#         phone = orders['customer_phone']
#         print(f'Order Number: {key} - Name: {name}, address: {address}, Phone number: {phone}, Status: {status}')
    

# def new_order():
#     print('\tAdding new order')
#     global no
#     global order_valA
#     customer_name = input('Input your name: ')
#     customer_address = input('Input your address: ')
#     # TODO: need to make it 11 digit number
#     customer_phone = input('Input your phone number: ')
#     status = 'Preparing'
#     order_val = {'customer_name': customer_name,
#                 "customer_address": customer_address,
#                 "customer_phone": customer_phone,
#                 "status": status} 

#     order_list[no] = order_val
#     # customer_name = Customer()
#     # print(order_list)
#     return

# def save_order():
#         try:
#             new_order_number = sorted(order_list.keys())[-1]
#             new_order = order_list[new_order_number]
#             with open('orders.txt', 'a') as customer:

#                 for orders in order_list:
#                     customer.write(str(order_list) +': '+ str(new_order) + '\n')

#         except FileNotFoundError as e:
#             print(f'Cannot find file: {e}')
#         finally:
#             customer.close()    
#         return

    
# def update_order_status():
#     clear_screen()
#     global order_list
#     #prints order number and status of the orders
#     for key, orders in order_list.items():
#         status = orders['status']
#         print(f'Order Number: {key}, Status: {status}')
#     print('\t**Order Status***')
#     Customers_order =int(input('\n\n\nInput your order number: '))
#     if  key >= Customers_order and not Customers_order <= 0:
#         update_status_input = str(input('Input the new status: '))
#         order_list[Customers_order]['status']  = update_status_input
#     else: 
#         print(f'Invalid input')
#         print(f'The last order was {key}')
#     short_pause()
#     return

# def update_saved_order():

#     return

# def update_order():
#     global order_list
#     #prints order number and name of the orders
#     print_orders()
#     Customers_order =int(input('Input your order number: '))
#     if  key >= Customers_order and not Customers_order <= 0:
#         clear_screen()
#         print('\t***Update customer Information***')
#         customer_input = int(input('(1) to change your name \
#                                 \n(2) to change your address\
#                                 \n(3) to change your number \n\n\n\
#                                 \nType the number:'))
#         if customer_input == 1:
#             update_name_input = str(input('Input the new name: '))
#             order_list[Customers_order]['customer_name']  = update_name_input
#         elif customer_input == 2:
#             update_address_input = str(input('Input the new address: '))
#             order_list[Customers_order]['customer_address']  = update_address_input
#         elif customer_input == 3:
#             update_number_input = input('Input the new number: ')
#             order_list[Customers_order]['customer_phone']  = update_number_input
#         else:
#             print('Invalid Input')
#     else: 
#         print(f'Invalid input')
#         print(f'The last order is {key}')
#     short_pause()
#     return

# def delete_order():
#     global check_input
#     global order_list
#     print_orders()
#     check_input ='delete'
#     try:
#         Customers_order =int(input('Input the order number to delete: '))
#         confirmation()
#         if confirm == 'y' or confirm == 'yes':
#             if  key >= Customers_order and not Customers_order <= 0:
#                 print('Deleting the product...')
#                 short_pause()
#                 del order_list[Customers_order]
#                 print('Deleted')
#                 short_pause()
#             else: 
#                 print(f'Invalid input')
#                 print(f'The last order was {key}')
#         elif confirm == 'n' or confirm == 'no':
#             print('Cancelled the deletion...')
#             print('Back to main menu')
#         else:
#             print('Invalid input')
#     except ValueError:
#         print('Invalid Input')
#         clear_screen()
#         print('\t**Returning to order Menu**')
#         short_pause()
#     return


# def confirmation():
    # global confirm
    # print('Are you sure you want to delete this product?')
    # confirm = str(input('Confirm Y(yes)/N(no): ').lower())
    # empty_input_check(confirm)


## my_list = list(my_dict.keys()) - this is to changhe the dictionary keys so the product into a list 
# try:
#             new_order_number = sorted(order_list.keys())[-1]
#             new_order = order_list[new_order_number]
#             with open('orders.txt', 'a') as customer:

#                 for orders in order_list:
#                     customer.write(str(order_list) +': '+ str(new_order) + '\n')

#         except FileNotFoundError as e:
#             print(f'Cannot find file: {e}')
#         finally:
#             customer.close()   