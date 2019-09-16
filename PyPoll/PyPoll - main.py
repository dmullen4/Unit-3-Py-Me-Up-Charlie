import os
import csv

# CSVfile pathway
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Initializing the variables
total_votes = 0
vote_khan = 0
vote_correy = 0
vote_li = 0
vote_otooley = 0

# Open the CSV and read it in
with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        total_votes += 1

        # Calculate the number of votes for each candidate
        if (row[2] == "Khan"):
            vote_khan += 1
        elif (row[2] == "Correy"):
            vote_correy += 1
        elif (row[2] == "Li"):
            vote_li += 1
        else:
            vote_otooley += 1

    # Calculate the candidates' percentage of votes received 
    percent_khan = vote_khan / total_votes
    percent_correy = vote_correy / total_votes
    percent_li = vote_li / total_votes
    percent_otooley = vote_otooley / total_votes

    # Determine the winner of the election
    vote_leader = max(vote_khan, vote_correy, vote_li, vote_otooley)

    if vote_leader == vote_khan:
        winner = "Khan"
    elif vote_leader == vote_correy:
        winner == "Correy"
    elif vote_leader == vote_li:
        winner = "Li"
    else:
        winner = "O'Tooley"

# Print the results of the election
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print(f"Kahn: {percent_khan:.3%}({vote_khan})")
print(f"Correy: {percent_correy:.3%}({vote_correy})")
print(f"Li: {percent_li:.3%}({vote_li})")
print(f"O'Tooley: {percent_otooley:.3%}({vote_otooley})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Exports values to a text file
PyPoll = open("PyPollOutput.txt","w+")
PyPoll.write("Election Results")
PyPoll.write('\n' + f"-------------------------")
PyPoll.write('\n' + f"Total Votes: {total_votes}")
PyPoll.write('\n' + f"-------------------------")
PyPoll.write('\n' + f"Kahn: {percent_khan:.3%}({vote_khan})")
PyPoll.write('\n' + f"Correy: {percent_correy:.3%}({vote_correy})")
PyPoll.write('\n' + f"Li: {percent_li:.3%}({vote_li})")
PyPoll.write('\n' + f"O'Tooley: {percent_otooley:.3%}({vote_otooley})")
PyPoll.write('\n' + f"-------------------------")
PyPoll.write('\n' + f"Winner: {winner}")
PyPoll.write('\n' + f"-------------------------")