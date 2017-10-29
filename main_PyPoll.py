import os
import csv
import collections


with open("election_data_2.csv", newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    next(csvreader)

    dictionary = {}
    unique_names=set()
    total_votes = 0
    dictionary = {"name":"","vote":0}
    

    votes_list = [row[2] for row in csvreader]

    votes = len(votes_list)

    candidates = {p: 0 for p in votes_list}

    for k in votes_list:
        candidates[k] += 1
    
    percentages = {k: f"{v / votes:.2%}" for k,v in candidates.items()}
 
    max_value = max(percentages.values())
    winner = [k for k, v in percentages.items() if v == max_value]


print("Election Results")
print("--------------------------------------")
print("Total Votes: " + str(votes))
print("--------------------------------------")
dd = collections.defaultdict(list)

for d in (percentages, candidates):
    for key, value in d.items():
        dd[key].append(value)

for k, v in dd.items():
    print(k + ":", v)

print("--------------------------------------")
print("Winner: " + str(winner))
print("--------------------------------------")

output_file = os.path.join("Election_Results.csv")

with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile, delimiter=',')

    datafile.write("Election Results \n")
    datafile.write("-------------------------------------- \n")
    datafile.write("Total Votes:    " + str(votes) + '\n')
    datafile.write("-------------------------------------- \n")
    dd = collections.defaultdict(list)

    for d in (percentages, candidates):
        for key, value in d.items():
            dd[key].append(value)

    for k, v in dd.items():
        datafile.write(str(k) + ':')
        datafile.write(str(v) + '\n')
    datafile.write("-------------------------------------- \n")
    datafile.write("Winner: " + str(winner) + '\n')
    datafile.write("-------------------------------------- \n") 

         