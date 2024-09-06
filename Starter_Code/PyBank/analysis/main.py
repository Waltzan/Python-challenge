# Import dependencies
import os
import csv
from pathlib import Path

# Pull File location through pathlib
pybank_db = Path("Python-challenge", "Starter_Code", "PyBank", "Resources", "budget_data.csv")

# Create empty lists
total_months = []
total_profit = []
monthly_profit= []
 
# Open and read csv file in default read mode
with open(pybank_db,newline="", encoding="utf-8") as budget:

    # Store the contents of budget_data.csv in a variable
    csvdata = csv.reader(budget,delimiter=",") 

    # Skip the header labels to repeat with values
    header = next(csvdata)  

    # Repeat through the rows
    for row in csvdata: 

        # Append the total months and total profit to their lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Create a loop through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit
        monthly_profit.append(total_profit[i+1]-total_profit[i])
        
# Calculate the max and min of the montly profit change list
max_increase = max(monthly_profit)
max_decrease = min(monthly_profit)

# Correlate max and min to the proper month using month list and index from max and min
max_increase_month = monthly_profit.index(max(monthly_profit)) + 1
max_decrease_month = monthly_profit.index(min(monthly_profit)) + 1 

# Print Statements
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_profit)/len(monthly_profit),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")

# Output files
summary_file = Path("Python-challenge", "Starter_Code", "PyBank", "analysis", "Financial_Analysis_Summary.txt")

with open(summary_file,"w") as file:
    
# Write methods to print to Financial Analysis Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit)/len(monthly_profit),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")