import os
import csv

#Run within /Resources Folder
csvpath = os.path.join('budget_data.csv')

#Create List
date = []
revenue = []
revenue_change = []

#Open and read CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        #print(row)
        date.append(row[0])
        revenue.append(row[1])

total_months = len(date)
#print(total_months)

revenue_float = [float(i) for i in revenue]
total_revenue = sum(revenue_float)
#print(total_revenue)

for i, rev in enumerate(revenue, start = 0):
    if i == total_months - 1:
        break
    else:
        change = revenue_float[i+1] - revenue_float[i]
        revenue_change.append(change)


avg_change = sum(revenue_change)/len(revenue_change)
inc_revenue = max(revenue_change)
dec_revenue = min(revenue_change)

print("Total Months: " + str(total_months), file=open("pybankoutput.txt", "a"))
print("Total: " + "$" + str(total_revenue), file=open("pybankoutput.txt", "a"))
print("Average Change: " + "$" + str(avg_change), file=open("pybankoutput.txt", "a"))
print("Greatest Increase in Profits: " + "$" + str(inc_revenue), file=open("pybankoutput.txt", "a"))
print("Greatest Decrease in Profits: " + "$" + str(dec_revenue), file=open("pybankoutput.txt", "a"))