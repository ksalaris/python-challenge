import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #testing that it is open print(csvreader)
    csv_header = next(csvreader, None)
    
    #The total number of months included in the dataset
    data = list(csvreader)
    total_months = len(data)
   
    #The net total amount of "Profit/Losses" over the entire period
    total_net = 0.0
    for row in data:
        total_net += (float(row[1]))
            
    #The average of the changes in "Profit/Losses" over the entire period
    all_nets = []
    average_change = []
    change = 0
    for column in data:
        all_nets.append(int(column[1]))
    for i in range(1,86,1):
        change = all_nets[i] - all_nets[i-1]
        average_change.append(change)
    avg_change = round((sum(average_change)/len(average_change)),2)
    
    #The greatest increase in profits (date and amount) over the entire period
    max_net = 0.0
    max_mo = []
    for i in range(0,86,1):
        if all_nets[i] > max_net:
            max_net = average_change[i]
            max_mo = data[i+1]
    #The greatest decrease in losses (date and amount) over the entire period
    min_net = 0.0
    min_mo = []
    for i in range(0,85,1):
        if average_change[i] < min_net:
            min_net = average_change[i]
            min_mo = data[i+1]



#print answers
print("Financial Analysis")
print("-----------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit: {total_net}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_mo[0]}, ${max_net}")
print(f"Greatest Decrease in Profits: {min_mo[0]}, ${min_net}")

file = open("output","w")
file.write("Financial Analysis"+ '\n')
file.write("-----------------------------------------------------"+ '\n')
file.write(f"Total Months: {total_months}"+ '\n')
file.write(f"Total Profit: {total_net}"+ '\n')
file.write(f"Average Change: ${avg_change}"+ '\n')
file.write(f"Greatest Increase in Profits: {max_mo[0]}, ${max_net}"+ '\n')
file.write(f"Greatest Decrease in Profits: {min_mo[0]}, ${min_net}"+ '\n')

file.close()