# Election_Analysis

## Project Overview
This project is to create a Python script to perform analysis on a given election dataset and output the following resluts:

1. Total number of votes cast.
2. A complete list of counties.
3. Votes cast for each county.
4. Percentage of votes for each county.
5. Largest turnout for the counties.
6. A complete list of candidates.
7. Votes cast for each candidate.
8. Percentage of votes for each candidate.
9. Winner of the election.
10. Election results be saved in election_results.txt

## Resources
- Data Source: election_results.csv
- Software: Python 3.9, Visual Studio Code, 1.60.1

## Election-Audit Results
The results of the election are:
- There were 369,711 votes cast in this election.
- The list of counties and their results:
  - County Jefferson received 10.5% of the vote and 38,855 votes.
  - County Denver received 82.8% of the vote and 306,055 votes.
  - County Arapahoe received 6.7% of the vote and 24,801 votes.
- The largest turnout county was Denver.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette 
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
  - Diana DeGette: 73.8% (272,892)  
  
Election results are saved in election_results.txt in the analysis folder. A screenshot of the result on the command line is shown in Image 1 below:
###### Image 1: Election Results Printed on Command Line
![election results](https://github.com/kaylaisnomyname/Election_Analysis/blob/main/election_results.png?raw=true)

## Election-Audit Summary
This Python script can be reused to analysis any elections with some modifications:
1. Change the "County" and "Candidate" column indexes in the script respect to that in the provided resource file. For instant, in the resource file, election_result.csv, "County" and "Candidates" info are located in column 2 and 3. In the script they were referred to "row[1]" and "row[2]". If a provided resource election file has "County" and "Candidates" info in different locations, then the columns indexes must be changed respectively.
2. The path to the resource file should be changed properly.
 


