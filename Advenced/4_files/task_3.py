from pprint import pprint
import csv

new_file = []
with open("hospitals.csv") as file:
    for row in csv.DictReader(file, delimiter=";"):
        new_file.append(dict(row))

for i in range(len(new_file)):
    jami = 0
    count = 8
    for j in range(2, count):
        jami += int(new_file[i][f'201{j}'])

    new_file[i]['jami'] = jami

pprint(sorted(new_file, key=lambda row: row['jami'], reverse=True))