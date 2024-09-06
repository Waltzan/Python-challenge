# Import dependencies
import os
import csv
from pathlib import Path

# Pull File location through pathlib
pypoll_db = Path("Python-challenge", "Starter_Code", "PyPoll", "Resources", "election_data.csv")

# Create Variables
total_votes = 0
Charles_votes = 0
Diana_votes = 0
Raymon_votes = 0

# Open and read csv file in default read mode
with open(pypoll_db,newline="", encoding="utf-8") as elections:

    # Store the contents of election_data.csv in a variable
    csvdata = csv.reader(elections,delimiter=",") 

    # Skip the header labels to repeat with values
    header = next(csvdata)  

    # Repeat through the rows
    for row in csvdata: 

        # Count the voter ID's and store it in the variable 'total_votes'
        total_votes +=1

    # Create if statements count total candidate votes
        if row[2] == "Charles Casper Stockham": Charles_votes +=1
        elif row[2] == "Diana DeGette": Diana_votes +=1
        elif row[2] == "Raymon Anthony Doane": Raymon_votes +=1
        
# Create list with candidate names
candidate = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_votes, Diana_votes, Raymon_votes]

# Zip the list of candidates(key) and the total votes
# Use the max function of the dictionary to select the winner 
dict_candidate_and_votes = dict(zip(candidate,votes))
key = max(dict_candidate_and_votes, key=dict_candidate_and_votes.get)

# Calculate percentages
Charles_percent = (Charles_votes/total_votes) * 100
Diana_percent = (Diana_votes/total_votes) * 100
Raymon_percent = (Raymon_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"------------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------------")
print(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_votes})")
print(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_votes})")
print(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_votes})")
print(f"------------------------------")
print(f"Winner: {key}")
print(f"------------------------------")

# Output files
summary_file = Path("Python-challenge", "Starter_Code", "PyPoll", "analysis", "Election_Results.txt")

with open(summary_file,"w") as file:
    
# Write methods to print to Election Results
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"------------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"------------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_votes})")
    file.write("\n")
    file.write(f"------------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"------------------------------")