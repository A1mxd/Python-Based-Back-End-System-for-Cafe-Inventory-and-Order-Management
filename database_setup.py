'TABLES'
'''
CREATE TABLE courier(
courier_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
courier_name VARCHAR(50)
courier_number VARCHAR(20)
);
'''

'''
CREATE TABLE courier(
product_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
product_name VARCHAR(50)
product_price VARCHAR(20)
);
'''

'''
CREATE TABLE order_status(
order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
order_status VARCHAR(20)
);
'''

'''
CREATE TABLE orders(
order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
customer_name VARCHAR (20) NOT NULL,
customer_phone VARCHAR(20) NOT NULL,
customer_address VARCHAR (50) NOT NULL,
courier_id INT,
order_status_id INT, 
items VARCHAR(50) NOT NULL,
FOREIGN KEY (courier_id) REFERENCES courier(courier_id),
FOREIGN KEY (order_status_id) REFERENCES order_status(order_status_id)
);
'''


#todo| a setup to create tables if there isnt one 
#todo| do this after unit testing and order database ting
