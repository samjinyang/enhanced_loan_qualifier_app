# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(data):
    """Creating a new function called save_csv that saves a csv file

    Args:
        data (list of lists): The list of filtered loans that the user qualifies for
    
    Returns:
        A csv file with the saved data
    """   
    bank_data = data

    #Creating headers for the csv file
    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Max Credit Score", "Interest Rate"]

    #Creating output path of the CSV file
    csvpath = Path("./data/output/save_file.csv")

    #Opening the csv file in csvpath by using the open() method
    with open(csvpath, "w", newline='') as csvfile:

        csvwriter = csv.writer(csvfile, delimiter = ",")
        csvwriter.writerow(header)
        for row in bank_data:
            csvwriter.writerow(row)

    return data