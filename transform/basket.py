from basket_class import Basket

def clean_basket_data(data):
    lst = []
    
    if "Pont-y-p" in data[0][1]:
        location = "Pontypool"
    else:
        location = data[0][1].strip(' ')
    
    code_location = location.replace(' ', '')
    date = data[0][0]
    date = date[0:10]
    basket_id = (f"{code_location}_{date}_bask")
    transaction_id = (f"{code_location}_{date}_trans")
    basket_number = 1
    transaction_number = 1
    
    for row in data:
        combined_data = (row[3]).split(", ")
        for i in range(len(combined_data)):
            string = combined_data[i]
            product_name = ''.join([i for i in string if not (i.isdigit() or i == ".")])
            price = combined_data[i].strip(product_name)
            product_name = product_name[:-3]
            new_basket_id = f"{basket_id}_{basket_number}"
            new_transaction_id = f"{transaction_id}_{transaction_number}"
            
            lst.append([basket_number, new_transaction_id, product_name.strip(' '), float(price)])
            basket_number += 1
        transaction_number += 1
    return lst