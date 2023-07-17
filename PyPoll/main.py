#imports
import os
import csv

#Create lists 
ballotid = []
county = []
candidate = []

#locate csv
csvpath = os.path.join('Resources', 'election_data.csv')

#read the csv file
with open(csvpath, 'r', encoding = 'UTF-8', newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    #for each row in the csv file, store the information in each column as a separate list
    for row in csvreader:
        ballotid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#ballots cast is equal to list length
totalballots = len(ballotid)

#identify unique candidates
candidate_names = []
for x in candidate:
    if x not in candidate_names:
        candidate_names.append(x)


#create lists to define candidates to number and %
candidate_votes_number = []
candidate_votes_percent = []

#for loop for counting candidate names appearing in list, then turn to %
for i in range(len(candidate_names)):
    count = candidate.count(candidate_names[i])
    candidate_votes_number.append(count)
    candidate_votes_percent.append(round((count/totalballots)*100, 3))


#calculate winning index
winning_index = 0
for i in range(len(candidate_votes_number)):
    if candidate_votes_number[i] > candidate_votes_number[winning_index]:
        winning_index = i

#print results
print("Election Results\n-------------------------")
print(f"Total Votes: {totalballots}")
print("-------------------------")

#print info for candidate
for i in range(len(candidate_names)):
    print(f"{candidate_names[i]}: {candidate_votes_percent[i]}% ({candidate_votes_number[i]})")

#print winner
print("-------------------------")
print(f"Winner: {candidate_names[winning_index]}")
print("-------------------------")

#output path
output_path = os.path.join("analysis", "election_results_text_file.txt")

#Open the txtfile
with open(output_path, 'w') as txtfile:
    txtwriter = txtfile.write
    txtfile.write("Election Results \n-------------------------\n")
    txtfile.write(f"Total Votes: {totalballots}\n")
    txtfile.write("-------------------------\n")
    for i in range(len(candidate_names)):
        txtfile.write(f"{candidate_names[i]}: {candidate_votes_percent[i]}% ({candidate_votes_number[i]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {candidate_names[winning_index]}\n")
    txtfile.write("-------------------------")