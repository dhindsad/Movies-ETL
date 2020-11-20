import csv
import os

file_to_load = os.path.join("Election_Analysis/Resources", "election_results.csv")

with open(file_to_load) as election_data:

    print(election_data)
