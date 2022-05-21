# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote

#Assign a variable for the file to load and the path
import csv
import os
file_to_load = os.path.join("Resources","election_results.csv")
#create a file name variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_ analysis.txt")
#1.Initialize a total vote counter
total_votes = 0
candidate_options= []
candidate_votes = {}
#Winning candidate and winning count tracker
winning_candidate =""
winning_count = 0
winning_percentage = 0
#using the with statement open the file as a text file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    # print(headers)
    for row in file_reader:
        #2.Add to the total count
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        #Check if candidate name already exists on the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name]+= 1
    #print each row in the csv file
    # for row in headers:
    #     print(row)
#3. Print the total votes
    for candidate_name in candidate_votes:
        #Retrieve vote count for each candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
        #print the candidate name and percentage of votes
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote. ")
        #Determine winning vote count and candidate
        #Determine if the votes are greater than the winning count
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
        winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning vote: {winning_count:,}\n"
            f"Winning percentage: {winning_percentage:.1f}%\n"
            f"--------------------------\n"
        )
    print(winning_candidate_summary)
    
    





