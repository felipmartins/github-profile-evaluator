import csv


def csv_to_list(csv_file):
    with open(csv_file) as file:
        return list(csv.DictReader(file))


def check_usernamekey_in_csv(csv_object, csv_list):
    
    if "github_username" in csv_list[0]:
        return True
    else:
        csv_object.file.delete()
        csv_object.delete()
        return False