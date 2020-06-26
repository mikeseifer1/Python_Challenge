import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
election_csv_path = os.path.join("..", "Resources", "election_data.csv")

votes = []
khan_votes =[]
correy_votes = []
li_votes = []
otooley_votes = []
winner = []




with open(election_csv_path,'r') as csvfile:
    election = csv.reader(csvfile, delimiter=",")
    csv_header = next(election)
    #print(f"CSV Header: {csv_header}")

    for row in election:
        votes.append(row[0])
        if row[2]=="Khan":
            khan_votes.append([2])
        elif row[2]=="Correy":
            correy_votes.append([2])
        elif row[2]=="Li":
            li_votes.append([2])
        elif row[2]=="O'Tooley":
            otooley_votes.append([2])
    
    print("Election Results")
    print("-----------------------------------")
    print(f"Total votes:  {len(votes)}")
    print("-----------------------------------")
    total_votes = (len(votes))
    
    
    total_khan_votes = (len(khan_votes))
    khan_pct = round(int(total_khan_votes)/int(total_votes),2)*100
    print(f"Khan: {khan_pct:.3f}% {total_khan_votes}")
    
    total_correy_votes = (len(correy_votes))
    correy_pct = (total_correy_votes/total_votes)*100
    print(f"Correy: {correy_pct:.3f}% {total_correy_votes}")
    
    total_li_votes = (len(li_votes))
    li_pct = (total_li_votes/total_votes)*100
    print(f"Li: {li_pct:.3f}% {total_li_votes}")
    
    total_otooley_votes = (len(otooley_votes))
    otooley_pct = (total_otooley_votes/total_votes)*100
    print(f"O'Tooley: {otooley_pct:.3f}%  {total_otooley_votes}")
    print("-----------------------------------")
    #winner = (max(khan_pct,correy_pct,li_pct,otooley_pct))
    #print(winner)
    if khan_pct > .5:
        print("Khan is the winner")
    elif correy_pct >.5:
        print("Correy is the winner")
    elif li_pct >.5:
        print("Li is the winner")
    elif otooley_pct>.5:
        print("O'Tooley is the winner")
    else:
        print("We need to have a runoff election")
print("-----------------------------------")

output_file = os.path.join("election.txt")
result = (
    f"Election Results\n"
    f"-----------------------------------\n"
    f"Total votes:  {len(votes)}\n"
    f"-----------------------------------\n"
    f"Khan: {khan_pct:.3f}% {total_khan_votes}\n"
    f"Correy: {correy_pct:.3f}% {total_correy_votes}\n"
    f"Li: {li_pct:.3f}% {total_li_votes}\n"
    f"O'Tooley: {otooley_pct:.3f}%  {total_otooley_votes}\n"
    f"Khan is the winner\n"
)
with open(output_file, "w") as datafile:
    datafile.write(result)