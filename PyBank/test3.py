import os
import csv


with open("budget_data_1.csv", newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    next(csvreader)

    totalrows = 0
    totalrev = 0

    revenue_items = []

    for row in csvreader:
        this_revenue = row[1]
        this_date = row[0]
        #revenue_change = ((row[1]+row)-row[1])
        dictionary =  {row[0]:int(row[1]) for row in csvreader}
        combo_maxrev_date = max(zip(dictionary.values(), dictionary.keys()))
        #print(revenue_change) 

        #join("{}: {}".format(k, v)
        #for k, v in dictionary.items():
            #format(key, value) = "{}: {}"
            #combo_maxrev_date = max(zip(dictionary.values(), dictionary.keys()))
            #combo_maxrev_date = max(zip(dictionary.keys(), dictionary.values()))
    print(dictionary)

    print(str(combo_maxrev_date))





        #revenue_items.append(int(this_revenue))
        #totalrows += 1
        #totalrev += int(this_revenue)
        #avgrev = totalrev / totalrows
        #max_revenue_item = max(revenue_items)
        #min_revenue_item = min(revenue_items)
        #if max_revenue_item == max(revenue_items):
            #date_of_max_rev = row[0]
    