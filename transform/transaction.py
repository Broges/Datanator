from transaction_class import Transaction

def clean_transaction_data(data):
    
    if "Pont-y-p" in data[0][1]:
        location = "Pontypool"
    else:
        location = data[0][1].strip(' ')
    
    code_location = location.replace(' ', '')
    date = data[0][0]
    date = date[0:10]
    transaction_id = (f"{code_location}_{date}_trans")
    transaction_number = 1
    
    lst = []
    

    for line in data:
        new_transaction_id = f"{transaction_id}_{transaction_number}"
        lst.append([new_transaction_id, location, line[2], line[0], float(line[-3])])
        transaction_number += 1
    return lst