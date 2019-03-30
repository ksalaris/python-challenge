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
    
    percentages = []
    vote_counts=[]
    all_votes=[]
    for row in candidates:
        for i in range(0,total_votes,1):
            if row == data[i][2]:
                vote_counts.append(data[0])
        all_votes.append(len(vote_counts))
        percentages.append(round(((len(vote_counts))/total_votes)*100,3))
        vote_counts.clear()
        
    candidates_votes = dict(zip(candidates,all_votes))
    winner = max(candidates_votes.keys(),key=lambda v: candidates_votes[v]) 

file = open("output.txt","w")
file.write("Election Results"+ '\n')
file.write("-------------------------"+ '\n')
file.write(f"Total Votes: {total_votes}"+ '\n')
file.write("-------------------------"+ '\n')
for i in range(0,len(candidates),1):
    file.write(f"{candidates[i]}: {percentages[i]}% ({all_votes[i]}) "+ '\n')
file.write("-------------------------"+ '\n')
file.write(f"Winner: {winner}"+ '\n')
file.write("-------------------------"+ '\n')

file.close()

with open("output.txt","r") as textfile:
    print(textfile.read())