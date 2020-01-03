import os
import csv

filename = os.path.join("..", "Data_files", "pybank_data.csv") 

# Lists to store data
date = []
profit_losses = []
monthly_change_pl = []

with open(filename, newline="") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    #Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        date.append(row[0])
        profit_losses.append(row[1])
# convert profit_losses from string to integer
    pl_numeric = list(map(int,profit_losses))
    for i in range (1, len(profit_losses)):
       monthly_change_pl.append(pl_numeric[i]-pl_numeric[i-1])
    average_change = sum(monthly_change_pl)/len(monthly_change_pl)

    print ("Financial Analysis")
#create dimension to store total months
    months_total = len(date)
    print(f"Total Months: {months_total}")
    sumof_pl = sum(pl_numeric)
    print(f"Total: ${sumof_pl}")
    print(f"Average Change: ${round(average_change, 2)}")