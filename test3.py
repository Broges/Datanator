csv_rows = [
    ["29/09/2020 09:00","Isle of Wight","Paul Kifer","Regular Luxury hot chocolate - £2.40, Regular Flavoured hot chocolate - Hazelnut - £2.60",5.00,"CASH"],
    ["29/09/2020 09:00","Isle of Wight","Thomas Mcdermott", "Frappes - Strawberries & Cream - £2.75",2.75,"CARD","46975498282144910"]
]

transaction_id = 1
basket_id = 1
data = []

for row in csv_rows:
    if "," in row[3]:
        basket = (row[3]).split(", ")
        for i in range(len(basket)):
            basket[i] = basket[i].split(" - £")
        for i in range(len(basket)):
            data.append([basket_id, transaction_id, basket[i][0], float(basket[i][1])])
            basket_id += 1
        transaction_id += 1
    else:
        basket = (row[3]).split(" - £")
        data.append([basket_id, transaction_id, basket[0], float(basket[1])])
        basket_id += 1
        transaction_id += 1

all_basket_objects = []

class Basket:
    def __init__(self, basket_id, transaction_id, basket_item, price):
        self.basket_id = basket_id
        self.transaction_id = transaction_id
        self.basket_item = basket_item
        self.price = price

    def __repr__(self):
        return (f"{self.basket_id}, {self.transaction_id}, {self.basket_item}, £{self.price}")


for i in range(0,len(data)):
    basket_object = Basket(data[i][0], data[i][1], data[i][2], data[i][3])
    all_basket_objects.append(basket_object)

for obj in all_basket_objects:
    print(obj)