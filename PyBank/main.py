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

    #print(csvreader)

# read the header row first
    csv_header = next(csvreader)

# read each row of data after the header
    for row in csvreader:
        date.append(row[0])
        profit_losses.append(row[1])
# convert profit_losses from string to integer
    pl_numeric = list(map(int,profit_losses))

# loop to create values for monthly_change_pl list

    for ic in range (1, len(profit_losses)):
       monthly_change_pl.append(pl_numeric[ic]-pl_numeric[ic-1])

# calculate min and max values in table monthly_change_pl and their positions

    min_profit = min(monthly_change_pl)
    max_profit = max(monthly_change_pl)

    min_profit_position = monthly_change_pl.index(min_profit)
    max_profit_position = monthly_change_pl.index(max_profit)

# calculate variables for final data output
    average_change = sum(monthly_change_pl)/len(monthly_change_pl)
    months_total = len(date)
    sumof_pl = sum(pl_numeric)
    dateof_min_profit = date [min_profit_position + 1]
    dateof_max_profit = date [max_profit_position + 1]

# print final report

    final_report = (f"""Financial Analysis
-------------------
Total Months: {months_total}
Total Profit: ${sumof_pl}
Average Change: ${round(average_change, 2)}
Greatest Increase in Profits: {dateof_max_profit} (${max_profit})
Greatest Decrease in Profits: {dateof_min_profit} (${min_profit})
-------------------""")
    print (final_report)

    txt_file = open ("PyBank_txtfile.txt", "w")
    print (final_report, file = txt_file)
    txt_file.close()