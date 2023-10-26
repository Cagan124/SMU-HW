import os
import csv

# attach csv
csvpath = "Resources/budget_data.csv"

#variables
months = 0
profit_loss = 0


# need new variable
changes = []
last_profit_loss = 0

# add max/min values
max_change = -999999999
min_change = 999999999
max_month = ""
min_month = ""

# add encoding to filter out foreign characters
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # header is first row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # add for loop
    for row in csvreader:
        print(row)

        #add if statement
        if months != 0:
            change = int(row[1]) - last_profit_loss
            changes.append(change)
            
            #add another if statement
            if change > max_change:
                max_change = change
                max_month = row[0]
            elif change < min_change:
                min_change = change
                min_month = row[0]
            else:
                pass
        #get last loss
        last_profit_loss = int(row[1])

        months = months + 1

        profit_loss = profit_loss + int(row[1])

# get the results of months and total

print(months)
print(profit_loss)

# need the average change
mean_change = sum(changes)/len(changes)
print(mean_change)

# now get the max and min
print(max_change)
print(min_change)
print(max_month)
print(min_month)

# convert results to text file

with open("pybank_results_abney.txt", "w") as txt_file:
    analysis = f"""
    Financial Analysis

    Total Months: {months}
    Total: ${profit_loss}
    Average Change: ${round(mean_change, 2)}
    Greatest Increase in Profits: {max_month} (${max_change})
    Greatest Decrease in Profits: {min_month} (${min_change})"""

    txt_file.write(analysis)


