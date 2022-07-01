# Get the data.
# Open the data file.
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.
#Percentage of votes for each canidate won.
# The winner of the election based on popular vote.

# Add our dependencies.

import csv
import os

# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")

   
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file.

with open(file_to_load) as election_data:


    # To do: read and analyze the data here.
    # Read the file object with the reader function.

    file_reader = csv.reader(election_data)

    # Read and print the header row.

    headers = next(file_reader)

    print(headers)


    
    