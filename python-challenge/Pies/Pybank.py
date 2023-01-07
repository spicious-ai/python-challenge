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
output_path = os.path.join("..", "Analysis", "PyBankAnalysis.txt")

#lines = []
with open(output_path, 'w') as f:
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

