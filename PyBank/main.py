import os
import csv

filename = os.path.join("..", "Data_files", "pybank_data.csv") 

# initialize lists to store data
date = []
profit_losses = []
monthly_change_pl = []

with open(filename, newline="") as csvfile:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

# read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# read each row of data after the header
    for row in csvreader:
        date.append(row[0])
        profit_losses.append(row[1])
# convert profit_losses from string to integer
    pl_numeric = list(map(int,profit_losses))

# loop to create values for monthly_change_pl list

    for ic in range (1, len(profit_losses)):
       monthly_change_pl.append(pl_numeric[ic]-pl_numeric[ic-1])

# calculate variables for final data output
    average_change = sum(monthly_change_pl)/len(monthly_change_pl)
    months_total = len(date)
    sumof_pl = sum(pl_numeric)

# print final report

    print ("Financial Analysis")
    print(f"Total Months: {months_total}")
    print(f"Total: ${sumof_pl}")
    print(f"Average Change: ${round(average_change, 2)}")