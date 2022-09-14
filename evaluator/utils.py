import csv


def csv_to_list(csv_file):
    with open(csv_file) as file:
        return list(csv.DictReader(file))
