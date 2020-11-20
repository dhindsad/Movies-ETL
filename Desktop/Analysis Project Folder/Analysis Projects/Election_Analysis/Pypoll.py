# The data we need to retrieve .
#1. the total number of votes
#2 a complete list of candidates who received votes
#3. the percentage of votes each candidate won
#4. total number of votes each candidate received.
#5. the winner of the election based on popular vote



import csv
import os
#Assign a variable to load a file from the path
file_to_load= os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save=os.path.join("analysis","election_analysis.txt")

#initialize a total vote counter
total votes = 0

# candidate options
candidate_options =[]

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #reader and print the header now
    headers=next(file_reader)
 

    #print each row in CSV file
    for row in file_reader:
        #add to the total vote count"
        total_votes +=1

        #print the candidate name from each row.
        candidate_name = row[2]

        #if the candidate does not match any existing candidate
    if candidate_name not in candidate_options:
        #add it to the list of candidates.
        candidate_options.append(candidate_name)

        #add the candidate name to the candidate list
        #candidate_options.append(candidate_name)

#print the candidate list
print(candidate-options)
        
    

    #to do: read and analyze the data here.


