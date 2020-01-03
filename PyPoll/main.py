import os
import csv

filename = os.path.join("..", "Data_files", "pypoll_test_data.csv")

# initialize lists to store data
voter_id = []
county = []
candidate = []

with open(filename, newline="") as csvfile:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    print (csv_header)

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    print (voter_id [0], len(voter_id))
    print (county [0])
    print (candidate [0])

    # create new list of unique candidates
    indv_cand = []

    for x in candidate:
        if x not in indv_cand:
                indv_cand.append(x)
    print(indv_cand)
    print (candidate)