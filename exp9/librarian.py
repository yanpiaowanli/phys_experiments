import os


def find_csv_files(directory):
    """ Recursively find all CSV files in the given directory """
    csv_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    return csv_files
