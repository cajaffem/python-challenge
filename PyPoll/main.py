import os
import csv

filename = os.path.join("..", "Data_files", "election_data.csv")

# initialize lists to store data
voter_id = []
county = []
candidate = []

with open(filename, newline="") as csvfile:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

# Read out header
    csv_header = next(csvreader)

# Read each row of data after the header
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# create new list for unique candidates
    indv_cand = []

# create conditional to calculate unique candidates
    for x in candidate:
        if x not in indv_cand:
                indv_cand.append(x)
    #print(indv_cand) returns list of all candidates: Khan, Correy, Li, and O'Tooley

# create variable for total votes cast
    tot_votes = len(voter_id)

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

# Create If-statement to determine who won most votes 
    if votes_Khan > votes_Correy and votes_Li and votes_OTooley:
        winner = "Winner: Khan"
    elif votes_Correy > votes_Khan and votes_Li and votes_OTooley:
        winner = "Winner: Correy"
    elif votes_Li > votes_Khan and votes_Correy and votes_OTooley:
        winner = "Winner: Li"
    elif votes_OTooley > votes_Khan and votes_Correy and votes_Li:
        winner = "Winner: O'Tooley"

# print final poll report
    final_report = print(f"""Election Results
-------------------------
Total Votes: {tot_votes}
-------------------------
Khan: {round(percent_Khan, 2)}% ({votes_Khan})
Correy: {round(percent_Correy, 2)}% ({votes_Correy})
Li: {round(percent_Li, 2)}% ({votes_Li})
O'Tooley: {round(percent_OTooley, 2)}% ({votes_OTooley})
-------------------------
({winner})
-------------------------""")
    print (final_report)