import os
import csv

# CSVfile pathway
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#Initializing the variables    
total_months = 0
total_revenue = 0
changes = []
date_tally = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Open the CSV and read it in
with open(budget_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)

    #Total months and total revenue calculations
    previous_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    for row in csvreader:

        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        # Compare monthly performance to prior months
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_tally.append(row[0])

        # Greatest Increase Calculations
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        # Greatest Decrease Calculations
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

    # Calculating the average and date
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    # Prints the values in terminal
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total_revenue))
    print("Average Change: $" + str(average_change))
    print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${high})")
    print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${low})")

    # Exports values to a text file
    PyBank = open("PyBankOutput.txt","w+")
    PyBank.write("Financial Analysis")
    PyBank.write('\n' + "----------------------------")
    PyBank.write('\n' + "Total Months: " + str(total_months))
    PyBank.write('\n' + "Total: $" + str(total_revenue))
    PyBank.write('\n' + "Average Change: $" + str(average_change))
    PyBank.write('\n' + f"Greatest Increase in Profits: {greatest_increase_month}, (${high})")
    PyBank.write('\n' + f"Greatest Decrease in Profits: {greatest_decrease_month}, (${low})")