csv_rows = [
    ["29/09/2020 09:00","Isle of Wight","Paul Kifer","Regular Luxury hot chocolate - 2.40, Regular Flavoured hot chocolate - Hazelnut - 2.60",5.00,"CASH"],
    ["29/09/2020 09:00","Isle of Wight","Thomas Mcdermott", "Frappes - Strawberries & Cream - 2.75",2.75,"CARD","46975498282144910"]
]



def func():
    transaction_id = 1
    basket_id = 1
    clean_data = []

    for row in csv_rows:
        combined_data = (row[3]).split(", ")
        for i in range(len(combined_data)):
            s = combined_data[i]
            product_name = ''.join([i for i in s if not (i.isdigit() or i == ".")])
            price = combined_data[i].strip(product_name)
            product_name = product_name[:-3]
            clean_data.append([basket_id, transaction_id, product_name, float(price)])
            basket_id += 1
        transaction_id += 1
    return clean_data

data = func()

for line in data:
    print(line)