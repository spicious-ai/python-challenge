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

        #create list of candidates
        if row[2] not in candidate:
            candidate.append(row[2])

        #count votes of candidates
        if(row[2] == 'Charles Casper Stockham'):
            cand_votes[0] = (cand_votes[0] + 1)
        if(row[2] == 'Diana DeGette'):
            cand_votes[1] = (cand_votes[1] + 1)
        if(row[2] == 'Raymon Anthony Doane'):
            cand_votes[2] = (cand_votes[2] + 1)


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

print('\n')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('\n')

import os
import csv
from statistics import mean

budget_csv = os.path.join('..', "Resources", "budget_data.csv")

#set variables
total_months = int(0)
profits = int(0)
change = []
holder = int(0)
months_list = []

#open and read file
with open(budget_csv) as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(budget_csv)
    #print(f"CSV Header: {csv_header}")
    


    for row in budget_csv:
        #count months
        total_months += 1
        #count total profits
        profits = profits + int(row[1])
        #make a list of month names
        months_list.append(row[0])
        
        #list try
        change.append((int(row[1])) - int(holder))
        
        #store last months profit/losses for change calculation
        holder = row[1]
        
#calculate largest profit and loss in profits
max_profit = max(change)
max_loss = min(change)

#find location of max change in list
max_profit_index = change.index(max_profit)
max_loss_index = change.index(max_loss)

#print results
print("Financial Analysis")
print("---------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${profits}')
print(f'Average Change: ${mean(change)}')
print(f'Greatest Increase in Profits: {months_list[max_profit_index]} ${max_profit}')
print(f'Greatest Decrease in Profits: {months_list[max_loss_index]} ${max_loss}')

"""
#create a list to write to file
output = []
output.append("Financial Analysis")
output.append("---------------------------")
output.append(f'Total Months: {total_months}')
output.append(f'Total: ${profits}')
output.append(f'Average Change: ${mean(change)}')
output.append(f'Greatest Increase in Profits: {months_list[max_profit_index]} ${max_profit}')
output.append(f'Greatest Decrease in Profits: {months_list[max_loss_index]} ${max_loss}')
"""

# Specify the file to write to
output_path_bank = os.path.join("..", "Analysis", "PyBankAnalysis.txt")

# Write to txt file "PyBankAnalysis.txt"
with open(output_path_bank, 'w') as f:
    f.write("Financial Analysis")
    f.write('\n')
    f.write("---------------------------")
    f.write('\n')
    f.write(f'Total Months: {total_months}')
    f.write('\n')
    f.write(f'Total: ${profits}')
    f.write('\n')
    f.write(f'Average Change: ${mean(change)}')
    f.write('\n')
    f.write(f'Greatest Increase in Profits: {months_list[max_profit_index]}  ${max_profit}')
    f.write('\n')
    f.write(f'Greatest Decrease in Profits: {months_list[max_loss_index]} ${max_loss}')

