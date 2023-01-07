import os
import csv

election_csv = os.path.join('..', "Resources", "election_data.csv")

#set variables
total_votes = 0
cand_votes = [0,0,0]
candidate = list()


#open and read file
with open(election_csv) as csvfile:
    election_csv = csv.reader(csvfile, delimiter=",")
    csv_header = next(election_csv)
    #print(f"CSV Header: {csv_header}")

    for row in election_csv:
        #calculate total votes
        total_votes += 1


        if row[2] not in candidate:
            candidate.append(row[2])
        
        #list of candidates
        #candidate.add(row[2])

        if(row[2] == 'Charles Casper Stockham'):
            cand_votes[0] = (cand_votes[0] + 1)
        if(row[2] == 'Diana DeGette'):
            cand_votes[1] = (cand_votes[1] + 1)
        if(row[2] == 'Raymon Anthony Doane'):
            cand_votes[2] = (cand_votes[2] + 1)

    
#change candidate set into list
#cand_list = list(candidate)

#calculate vote percentages
charles_perc = cand_votes[0] / total_votes
diana_perc = cand_votes[1] / total_votes
raymon_perc = cand_votes[2] / total_votes

#make list of candidate vote totals
most_votes = max(cand_votes)
winner = cand_votes.index(most_votes)

#print outputs
"""
print(total_votes)
print(candidate)
print(cand_votes)
print(cand_list[winner])
"""
print("Election Results")
print("------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------")
print(f'{candidate[2]}: {round((raymon_perc*100),3)}% ({cand_votes[2]})')
print(f'{candidate[0]}: {round((charles_perc*100),3)}% ({cand_votes[0]})')
print(f'{candidate[1]}: {round((diana_perc*100),3)}% ({cand_votes[1]})')
print("------------------------")
print(f'Winner: {candidate[winner]}')
print("------------------------")

# Specify the file to write to
output_path_poll = os.path.join("..", "Analysis", "PyPollAnalysis.txt")

# Write to txt file "PyPollAnalysis.txt"
with open(output_path_poll, 'w') as f:
    f.write("Election Results")
    f.write('\n')
    f.write("------------------------")
    f.write('\n')
    f.write(f'Total Votes: {total_votes}')
    f.write('\n')
    f.write("------------------------")
    f.write('\n')
    f.write(f'Raymon Anthony Doane: {round((raymon_perc*100),3)}% ({cand_votes[0]})')
    f.write('\n')
    f.write(f'Charles Casper Stockham: {round((charles_perc*100),3)}% ({cand_votes[1]})')
    f.write('\n')
    f.write(f'Diana DeGette: {round((diana_perc*100),3)}% ({cand_votes[2]})')
    f.write('\n')
    f.write("------------------------")
    f.write('\n')
    f.write(f'Winner: {candidate[winner]}')
    f.write('\n')
    f.write("------------------------")