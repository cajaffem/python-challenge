import os
import csv

filename = ("C:\Users\cajaf\Documents\Repository\python-challenge\Data_files\pybank_data.csv")
#os.path.join("..", "Data_files", "pybank_data.csv") 

with open(filename, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first (skip this step if there is no header)

csv_header = next(csvfile)
print(f"Header: {csv_header}csvreader")