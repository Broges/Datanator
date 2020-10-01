csv_rows = [
    ["29/09/2020 09:00","Isle of Wight","Paul Kifer","Regular Luxury hot chocolate - 2.40, Regular Flavoured hot chocolate - Hazelnut - 2.60",5.00,"CASH"],
    ["29/09/2020 09:00","Isle of Wight","Thomas Mcdermott", "Frappes - Strawberries & Cream - 2.75",2.75,"CARD","46975498282144910"]
]

transaction_id = 1
basket_id = 1
clean_data = []

def func():
    for row in csv_rows:
        if "," in row[3]:
            transformed_data = (row[3]).split(", ")
            print(transformed_data)
            for i in range(len(transformed_data)):
                number = ""
                while type(int(transformed_data[i][-1])) == type(5)  or (transformed_data[i][-1] == "."):
                    print(transformed_data[i][-1])
                    number = str(transformed_data[i][-1]) + number
                    # transformed_data[i][-1] == ""
                    transformed_data[i] = transformed_data[i][:-1]
                print(number)




#             transformed_data[i] = transformed_data[i].split(" - ")
#         for i in range(len(transformed_data)):
#             clean_data.append([basket_id, transaction_id, transformed_data[i][0], float(transformed_data[i][1])])
#             basket_id += 1
#         transaction_id += 1
#     else:
#         transformed_data = (row[3]).split(" - ")
#         clean_data.append([basket_id, transaction_id, transformed_data[0], float(transformed_data[1])])
#         basket_id += 1
#         transaction_id += 1

# for lst in clean_data:
#     print(lst)

func()