import os
import csv
# attach csv
csvpath = "Resources/election_data.csv"
#variables
total_votes = 0
candidate = {}
# dictionary is most dynamic approach
# open csv
# encoding blocks out foreign characters
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    print(f"CSV Header:{csv_header}")
# start reading after header

    for row in csvreader:
        
        total_votes = total_votes + 1

        # need the name
        names = row[2]
#add if statement
        if names in candidate.keys():
            candidate[names] += 1
        else: candidate[names] = 1

print(total_votes)
print(candidate)

#loop through all names
# need to find winner

# more variables
winning_votes = 0
winner = ""
#add loop
for fullname in candidate.keys():
    votes = candidate[fullname]

    if votes > winning_votes:
        winning_votes = votes
        winner = fullname

print(winner, winning_votes)
# boom, winner winner chicken dinner

#need to add percentage of votes
results = f"""
Election Results

Total Votes: {total_votes}
"""
for key in candidate.keys():
    percentage = round(100*candidate[key]/total_votes,3)
    newline = f"{key}: {percentage}% ({candidate[key]})"
    results += newline

lastline = f"""

Winner: {winner}

"""

results += lastline
print(results)

#create text file
with open("pypoll_results_abney.txt", "w") as txt_file:
    txt_file.write(results)


