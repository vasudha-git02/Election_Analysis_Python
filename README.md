# Election_Analysis_Python

## Project Overview
 A Colarado Board of Election employee Tom has gives us certain tasks to complete the election audit of a recent local congressional election. Below are the tasks that are given to us
 1. Calculate the total number of votes cast.
 2. Get a complete list of candidates who received votes.
 3. Calculate the total number of votes each candidate received.
 4. Calculate the percentage of votes each candidate won.
 5. Determine the winner of the election based on the popular vote.

## Resources
- Data Source : election_results.csv
- Software    : Python 3.8, Visual studio code, 1.67.2

## Summary
The analysis of election show that :
- There were a total of 369,711 votes cast in the election
- The counties were:
  - Jefferson
  - Denver
  - Arapahoe
- The count and percentage of votes for each counties were:
  - Jefferson : 38,855 number of votes (10.5%)
  - Denver    : 306,055 number of votes (82.8%)
  - Arapahoe  : 24,801 number of votes (6.7%)
- The county results were:
  - County Denver recieved the largest turonover of votes which is 306,055 number of votes
- The candidate were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes.
  - Diana DeGette recieved 73.8% of the votes and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette who received a total of 272,892 number of votes which is 73.8% of the total votes.

## Challenge Overview
The challenge is to determine the winner of the congressional election in a US presinct Colarado. We were tasked to in reporting a total number of votes cast,the total number of votes cast for each candidate, the percentage of votes for each candidate and the winner
of the election based on the most popular vote. This is generally done in excel but to automate the process we have done this in python so that we can use the same code not only in the districts but also senitorial districts and local elections.

## Challenge Summary
After the analysis i.e., counting the total votes cast, the votes each candidate and county received and the percentage of votes each candidate and county received we can say that Diana Degette is the  winner of the election who received the majority of the votes which is 73% of the total votes. Also we can say that Denver county recived the largest turnover of votes, Below is the image of the output printed into the terminal based on which the above conclusion is made


<img width="683" alt="python result" src="https://user-images.githubusercontent.com/104597335/169707025-3ece11af-6237-49ef-a90a-1345a24dfeab.png">


This script can be re-used for any election by just changing the input csv file and output text file in place of the below code snippet i.e., change the input to the file_to_load and output of the file_to_save .


<img width="388" alt="Code_snippet" src="https://user-images.githubusercontent.com/104597335/169707105-9db845a0-8a5e-4cf8-a1b9-bac3e17b428e.png">

