import os
import csv

#Run within /Resources Folder
csvpath = os.path.join("election_data.csv")

#List
votes = []
candidates = []
winner = []
vote_total = 0
vote_percent_candidate = 0
vote_total_candidate = 0
li = 0
khan = 0
correy = 0
tooley = 0

#Dictionary of candidates
candidate_dic = {"Candidates":["Li","Khan","Correy","O'Tooley"]}

#Read and open CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    for row in csvreader:
         votes.append(row)
         candidates.append(row[2])
         if row[2]=="Li":
             li = li + 1
         elif row[2]=="Khan":
             khan = khan + 1
         elif row[2]=="Correy":
             correy = correy + 1
         elif row[2]=="O'Tooley":
             tooley = tooley + 1
votetotal = len(votes)



khan_percent = format((khan/votetotal)*100,'.3f')
li_percent = format((li/votetotal)*100,'.3f')
correy_percent = format((correy/votetotal)*100,'.3f')
tooley_percent = format((tooley/votetotal)*100,'.3f')


highest_vote_count = max(candidate_dic.values())
winner = [i for i, k in candidate_dic.items() if k == highest_vote_count]

    
 
print("Election Results")   
print("-------------------------")
print("Total Votes:" + str(vote_total), file=open("pypolloutput.txt", "a"))    
print("-------------------------")
print(f'{candidate_dic["Candidates"][1]}: ' + khan_percent + "% (" + str(khan) + ")", file=open("pypolloutput.txt", "a"))
print(f'{candidate_dic["Candidates"][2]}: ' + correy_percent + "% (" + str(correy) + ")", file=open("pypolloutput.txt", "a"))
print(f'{candidate_dic["Candidates"][0]}: ' + li_percent + "% (" + str(li) + ")", file=open("pypolloutput.txt", "a"))
print(f'{candidate_dic["Candidates"][3]}: ' + tooley_percent + "% (" + str(tooley) + ")", file=open("pypolloutput.txt", "a"))
print("-------------------------")
print("Winner: " + winner, file=open("pypolloutput.txt", "a"))
print("-------------------------")