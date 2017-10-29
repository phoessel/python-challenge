import os
import csv

csvpath = os.path.join('c:/','hwk','hwk3','budget_data_1.csv')

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    next(csvreader)
	
    totalrev = 0

    #totalrows = len(list(csvfile)) - 1

    for row in csvreader:
	    totalrev += int(row[1])
	

    print("Financial Analysis")
    print("--------------------------------------")
    print("Total Months: " + str(totalrows))
    print(totalrev)