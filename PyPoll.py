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

# 1. Initialize the total vote counter.

total_votes =0

# 3. Declaring a new list 

candidate_options = []

candidate_votes = {}

winning_candidate = ""

winning_count = 0

winning_percentage = 0



# Open the election results and read the file.

with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.

    file_reader = csv.reader(election_data)

    # Read and print the header row.

    headers = next(file_reader)

    # Print each row in the CSV file.

    for row in file_reader:

       # Add to the total vote count.

       total_votes += 1

       # Print the candidate name for each row.

       candidate_name = row[2]


        #Add the candidate name to the candidate list.
    
    
        # If the candidate does not match any existing canditate...

       if candidate_name not in candidate_options:

            # Add it to the list of candidates.

            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.

            candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count.

       candidate_votes[candidate_name] +=1


with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (

        f"\nElection Results\n"

        f"-------------------------\n"

        f"Total Votes: {total_votes:,}\n"

        f"-------------------------\n")

    print(election_results, end="")

    # Save the final vote count to the text file.

    txt_file.write(election_results)


    # Iterate through the candidate list.

    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate.

        votes = candidate_votes[candidate_name]

        # Calculate the pec=rcentage of votes.

        vote_percentage = float(votes) / float(total_votes)* 100

        # Print the candidate name and percentage of votes.

        # print(f"{candidate_name}: recieved {vote_percentage:.1f}% of the vote.")

    

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.

        print(candidate_results)

        #  Save the candidate results to our text file.

        txt_file.write(candidate_results)


        # Winning candidate and winning count tracker


        # Determining winning vote count and candidate

        # 1. Determining if the votes are greater than the winning count.

        if (votes > winning_count) and (vote_percentage > winning_percentage):


            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name
        



    winning_candidate_summary = (

        f"----------------------------------------------------------------------\n"

        f"Winner: {winning_candidate}\n"

        f"Winning Vote Count: {winning_count}\n"

        f"Winning percentage: {winning_percentage:.1f}%\n"

        f"-----------------------------------------------------------------------\n"

    )

    print(winning_candidate_summary)

      # Save the winning candidate's results to the text file.

    txt_file.write(winning_candidate_summary)



