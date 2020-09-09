
import csv

users = []
orders = []

with open('users_202002181303.csv', 'r') as csvfile:
    reader_users = csv.DictReader(csvfile)
    for user in reader_users:        
        users.append(user)

with open('orders_202002181303.csv', 'r') as csvfile:
    reader_orders = csv.DictReader(csvfile) 
    for order in reader_orders:        
        orders.append(order)

        
for order in orders: 
    orders_with_users_data = []
    
    for user in users: 
        if order['user_id'] == user['user_id']:       
            updated_order = order         
            updated_order['first_name'] = user['first_name']      
            updated_order['last_name'] = user['last_name'] 

            orders_with_users_data.append(updated_order)      

with open("another_file.csv", 'w') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(orders_with_users_data)

print("Process finished: \n", "Initial number of orders: ", len(orders))
print("Returned number of orders with users: ", len(orders_with_users_data))





                
                
            



    

    

 
