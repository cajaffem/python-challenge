import os
import csv

filename = os.path.join("..", "Data_files", "pybank_data.csv") 

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

with open(filename, newline="") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(sum(row))