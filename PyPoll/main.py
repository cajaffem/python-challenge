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

# create new list for unique candidates
    indv_cand = []

# create conditional to calculate unique candidates
    for x in candidate:
        if x not in indv_cand:
                indv_cand.append(x)
    print(indv_cand)

# create variable for total votes cast
    tot_votes = len(voter_id)
    print(tot_votes)

# determine total number of votes per candidate
    votes_Khan = candidate.count("Khan")
    votes_Correy = candidate.count("Correy")
    votes_Li = candidate.count("Li")
    votes_OTooley = candidate.count("O'Tooley")

# divide each candidate's vote count by length of list voter_id * 100 to find percent
    percent_Khan = votes_Khan/len(voter_id) * 100
    percent_Correy = votes_Correy/len(voter_id) * 100
    percent_Li = votes_Li/len(voter_id) * 100
    percent_OTooley = votes_OTooley/len(voter_id) * 100

# write conditional using the votes_ variable to find candidate with most votes
# for mostvotes in candidate
# if votes_khan > votes_correy and votes_li and votes_otooley then
# print mostvotes
