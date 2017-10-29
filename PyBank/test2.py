import os
import csv

with open("budget_data_1.csv", newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    next(csvreader)

    dictionary =  {row[0]:int(row[1]) for row in csvreader}
    combo_maxrev_date = max(zip(dictionary.values(), dictionary.keys()))
    print(dictionary)   
    print(combo_maxrev_date)    

    totalrows = 0
    totalrev = 0

    revenue_items = []

    for row in csvreader:
        this_revenue = row[1]
        revenue_items.append(int(this_revenue))
        totalrows += 1
        totalrev += int(this_revenue)
        avgrev = totalrev / totalrows
        max_revenue_item = max(revenue_items)
        min_revenue_item = min(revenue_items)


    

print("Financial Analysis")
print("--------------------------------------")
print("Total Months: " + str(totalrows))
print("Total Revenue: " + str(totalrev))
print("Average Revenue: " + str(round(avgrev)))
print("Greatest Increase in Revenue: " + str(max_revenue_item))
print("Greatest Decrease in Revenue: " + str(min_revenue_item))
#print(str(combo_maxrev_date))

output_file = os.path.join("Financial_Analysis_Results.csv")

with open(output_file, "w", newline="") as datafile:
    #csvwriter = csv.writer(datafile, delimiter=',')
    #csvwriter.writerow("Date,Revenue")

    datafile.write("Financial Analysis \n")
    datafile.write("-------------------------------------- \n")
    datafile.write("Total Months:    " + str(totalrows) + '\n')
    datafile.write("Total Revenue:    " + str(totalrev) + '\n')
    datafile.write("Average Revenue:    " + str(round(avgrev)) + '\n')
    datafile.write("Greatest Increase in Revenue:    " + str(max_revenue_item) + '\n')
    datafile.write("Greatest Decrease in Revenue:    " + str(min_revenue_item) + '\n')

    
    


