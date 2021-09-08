# open/read/write : analysis csv file

# import needed dependencies
import csv
import os

# assign variable to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# assign variable to ouput file to hold analysis results
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the data file and read the file
with open(file_to_load) as election_data:
    # analysis actions starts from here 
    # to read and analyze data here
    file_reader = csv.reader(election_data)     # read file using reader function in csv
    
    # print each row in the csv file
#    for row in file_reader:
 #       print(row)
    # read and print the 1st row, header row
    headers = next(file_reader)
    print(headers)  # print to terminal
