import csv

def read_csv(file_name):
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=',')
        data = []
        for row in reader:
            data.append(row)
        return data