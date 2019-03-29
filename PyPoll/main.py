import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader,None)
    
    data = list(csvreader)
   
    
    #The total number of votes cast
    total_votes = len(data) 
    
    #A complete list of candidates who received votes
    candidates = []
    for row in data:
        if row[2] not in candidates:
            candidates.append(row[2])
    
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    
    for row in data:
        if row[2] == candidates[0]:
            khan += 1
        if row[2] == candidates[1]:
            correy += 1
        if row[2] == candidates[2]:
            li += 1
        if row[2] == candidates[3]:
            otooley += 1
    
                
    #The percentage of votes each candidate won
    pk = 0
    pc = 0
    pl = 0
    po = 0
    
    pk = round(((khan/total_votes)*100),2)
    pc = round(((correy/total_votes)*100),2)
    pl = round(((li/total_votes)*100),2)
    po = round(((otooley/total_votes)*100),2)
    

    #The winner of the election based on popular vote.
    votes = [khan, correy, li, otooley]
    candidates_votes = dict(zip(candidates,votes))
    
    winner = max(candidates_votes.keys(),key=lambda v: candidates_votes[v]) 
    print(winner)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {pk}% ({khan})")
print(f"Correy: {pc}% ({correy})")
print(f"Li: {pl}% ({li})")
print(f"O'Tooley: {po}% ({otooley})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")



file = open("output.txt","w")
file.write("Election Results"+ '\n')
file.write("-------------------------"+ '\n')
file.write(f"Total Votes: {total_votes}"+ '\n')
file.write("-------------------------"+ '\n')
file.write(f"Khan: {pk}% ({khan})"+ '\n')
file.write(f"Correy: {pc}% ({correy})"+ '\n')
file.write(f"Li: {pl}% ({li})"+ '\n')
file.write(f"O'Tooley: {po}% ({otooley})"+ '\n')
file.write("-------------------------"+ '\n')
file.write(f"Winner: {winner}"+ '\n')
file.write("-------------------------"+ '\n')

file.close()