import os
import csv

with open("budget_data_1.csv", newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    next(csvreader)

    totalrows = 0
    totalrev = 0
    avgrev = 0

    prev_row = None
    revenue_items = []
    maxdictionary = {"date":"","revenue":0}
    mindictionary = {"date":"","revenue":0}
    revenue_changes = []


    for row in csvreader:
        this_revenue = int(row[1])
        revenue_items.append(this_revenue)
        if prev_row:
            revenue_changes.append(this_revenue - int(prev_row[1]))
        totalrows += 1
        totalrev += this_revenue
        #avgrev = totalrev / totalrows
        if this_revenue > maxdictionary["revenue"]:
            maxdictionary["revenue"] = this_revenue
            maxdictionary["date"] = row[0]
        if this_revenue < mindictionary["revenue"]:
            mindictionary["revenue"] = this_revenue
            mindictionary["date"] = row[0]
        prev_row = row
    
    avgrev = sum(revenue_changes) / len(revenue_changes)


print("Financial Analysis")
print("--------------------------------------")
print("Total Months: " + str(totalrows))
print("Total Revenue: " + "$" + str(totalrev))
print("Average Revenue Change: " + "$" + str(round(avgrev)))
print("Greatest Increase in Revenue: " + str(maxdictionary["date"]) + "  " + "$" + str(maxdictionary["revenue"]))
print("Greatest Decrease in Revenue: " + str(mindictionary["date"]) + "  " + "$" + str(mindictionary["revenue"]))


output_file = os.path.join("Financial_Analysis_Results.csv")

with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile, delimiter=',')

    datafile.write("Financial Analysis \n")
    datafile.write("-------------------------------------- \n")
    datafile.write("Total Months:    " + str(totalrows) + '\n')
    datafile.write("Total Revenue:    " + "$" + str(totalrev) + '\n')
    datafile.write("Average Revenue Change:    " + "$" + str(round(avgrev)) + '\n')
    datafile.write("Greatest Increase in Revenue:    " + str(maxdictionary["date"]) + "  " + "$" + str(maxdictionary["revenue"]) + '\n')
    datafile.write("Greatest Decrease in Revenue:    " + str(mindictionary["date"]) + "  " + "$" + str(mindictionary["revenue"]) + '\n')

    
    


