from pprint import pprint
import csv

new_file = []
with open("hospitals.csv") as file:
    for row in csv.DictReader(file, delimiter=";"):
        new_file.append(dict(row))

pprint(new_file)