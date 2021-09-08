# open/read/write : analysis csv file

# import needed dependencies
import csv
import os

# assign variable to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# assign variable to ouput file to hold analysis results
file_to_save = os.path.join("analysis", "election_analysis.txt") # if no writing operation happen, then the new txt file won't be created

# initialize a vote counter before opening the file
total_votes = 0
# initialize candidate options as an empty list
candidate_options = []
# initialize candidate name:votes dictionary as an empty dictionary
candidate_votes = {}
# winning counts
winning_name = " "
winning_count = 0
winning_percentage = 0

# open the data file and read the file
with open(file_to_load) as election_data:
    # read and analyze data here
    file_reader = csv.reader(election_data)     # read file using reader function in csv, read all the data in the file
    
    # print each row in the csv file
#    for row in file_reader:
 #       print(row)
    # read and print the 1st row, header row
    headers = next(file_reader)     # next() skip the first row and return ready at the next row
#    print(headers)  # print to terminal

    # print each row in the csv file
    for row in file_reader:
        # add to the total vote count
        total_votes += 1    # increment total_vote by 1 each round
        # get the candidate name from each row
        candidate_name = row[2]
        # if the candidate does not match any existing candidate in candidate_options
        if candidate_name not in candidate_options:
            # add the new name to the candidate options list
            candidate_options.append(candidate_name)
            # begin to track the candidate's vote count 
            candidate_votes[candidate_name] = 0      
        # add a vote to the candidate's count
        candidate_votes[candidate_name] += 1    # no need to add else, if added "else" would miss 1 vote for each candidate
# save the results to the output file
with open(file_to_save, "w") as txt_file:
    election_results = (
         f"\nElection Results\n"
         f"----------------------------\n"
         f"Total Votes: {total_votes:,}\n"
         f"----------------------------\n")
    print(election_results, end= "")   # end="" empty string to make sure this will be the end of this line, anything new to print will be in next line. 
     # save the final vote count to the text file
    txt_file.write(election_results)

    # determine the percentage of votes for each name using a new for loop
    # iterate through the candidate list
    for candidate_name in candidate_votes:
        # get the vote count for the candidate
        vote_count = candidate_votes[candidate_name]
        # calculate the percentage, in float data type, since the votes were interger 
        vote_percentage = float(vote_count)/float(total_votes)*100
        # save the name and the percentage to the output file
        candidate_results = (f"{candidate_name} : {vote_percentage:.1f}% ({vote_count:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

         # deterimne winning vote count and candidate
        # check if the votes is greater than the winning count
        if (vote_count > winning_count) and (vote_percentage > winning_percentage):
            winning_count = vote_count
            winning_percentage = vote_percentage
            winning_name = candidate_name
    # todo for for-loop
    winning_summary = (
        f"----------------------------------------------\n"
        f"Winner: {winning_name}. \n"
        f"Winning Vote Count: {winning_count:,}. \n"
        f"Winning percentage: {winning_percentage:.1f}%. \n"
        f"-----------------------------------------------\n")        
    print(winning_summary)
    txt_file.write(winning_summary)

# print the total_votes after reading all data
#print(total_votes)  #369711,checked
#print(candidate_options)    # checked
#print(candidate_votes)


