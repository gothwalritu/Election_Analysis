## Module 3

# Election Analysis

# 1. Overview of Election Audit: 

In this project we are asked to assist Colorado Board of Employee for local congressional election. Our job is to generate a vote count report with the following items:

•	The total voter count for each county

•	The percentage of votes from each county out of the total count

•	The county with the highest number of votes

•	The total vote counts

•	The list of candidates who received votes in the election

•	The total number of votes received by each candidate

•	The percentage of votes for each candidate

•	The winner of the election who received largest number of votes

# 2. Election-Audit Results: 

- Total votes in this congressional election were 369,711
- The results for the following items are mentioned in the screenshots of election_analysis.txt file (Picture 1) and Visual Studio Code terminal (Picture 2): 

**a.**	The number of votes and the percentage of total votes for each county in the precinct.

**b.**	The county which had the largest number of votes.

**c.**	Breakdown of the number of votes and the percentage of the total votes received by each candidate.

**d.**	 Candidate who won the congressional election and his vote count, and the percentage of the total votes.


## Picture 1: Screenshot of the txt file 
![Screenshot of the txt file](https://github.com/gothwalritu/Election_Analysis/blob/main/Resources/terminal%20election%20analysis.png)





## Picture 2: Screenshot of the Visual Studio Code Terminal 
![Screenshot of the Visual Studio Code Terminal](https://github.com/gothwalritu/Election_Analysis/blob/main/Resources/txt_file_election_analysis.png)
 

# 3.	Election-Audit Summary: 

We have developed a code which reads the CSV file and look for the details which are required to generate a vote count report in text file in order to certify the winner of the congressional election. We have automated the entire process of generating the vote count report using python and, and it can be used with a few modifications for any election. A CSV file will be needed which contains the data for Ballot ID, County, and Candidate name. The script could be tweaked at few places in accordance with the given data file in order to obtain an election report. The following modification could be made to make the given script applicable for any election:

**A.**	We just need to modify the path of the stored CSV file.
“file_to_load = os.path.join("Resources", "election_results.csv")"

**B.**	The CSV file could be a bit different in ways of saving its information and not as same as in the present CSV file i.e., Ballot ID in the first row, County in the second row, and candidate name in the third row. However, the row numbers could be changed according to the given data file. The lines of codes are given below where it can be changed, read and stored.

for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

**C.**	Sometimes, it is required to generate the election analysis report in certain format for different elections which can also be modified according to the requirement in the following lines of the script:


           # Print the winning candidate (to terminal)
           
            winning_candidate_summary = (
                    f"-------------------------\n"
                    f"Winner: {winning_candidate}\n"
                    f"Winning Vote Count: {winning_count:,}\n"
                    f"Winning Percentage: {winning_percentage:.1f}%\n"
                    f"-------------------------\n")
                print(winning_candidate_summary)


