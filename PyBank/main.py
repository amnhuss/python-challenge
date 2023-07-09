#imports
import os
import csv

#create lists (mnthpl = month profit and losses)
date = []
mnthpl = []

#create list that will hold changes made (mnth = month)
mnthchange = []

#direct path
csvpath = os.path.join('Resources', 'budget_data.csv')

#read in the csv 
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    # define integers
    total = 0
    totalmonths = 0

    #for loop 
    for row in csvreader:
        
        #add by 1 each loop
        totalmonths = totalmonths + 1
        #add by profit/loss 
        total = total + int(row[1])

        #go through file and make list
        date.append(row[0])
        mnthpl.append(int(row[1]))

#calculate the changes
mnthchange = [mnthpl[i+1]-mnthpl[i] for i in range (len(mnthpl)-1)]

#calculate the average 
avgmnthchange = round(sum(mnthchange)/len(mnthchange),2)

#find the index in the monthly change list associated with the maximum change and the minimum change
maxmonthlyprofit_index = mnthchange.index(max(mnthchange))
maxmonthlyloss_index = mnthchange.index(min(mnthchange))

#print
print(f"Financial Analysis \n -------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${total}")
print(f"Average Change: ${avgmnthchange}")

#print 
print(f"Greatest Increase in Profits: {date[maxmonthlyprofit_index+1]} (${mnthchange[maxmonthlyprofit_index]})")
print(f"Greatest Decrease in Profits: {date[maxmonthlyloss_index+1]} (${mnthchange[maxmonthlyloss_index]})")

#output path
output_path = os.path.join("analysis", "budget_text_file.txt")

#Open the txtfile
with open(output_path, 'w') as txtfile:
    txtwriter = txtfile.write
    txtfile.write("Financial Analysis \n-------------------------------\n")
    txtfile.write(f"Total Months: {totalmonths}\n")
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change: ${averagemnthchange}\n")
    txtfile.write(f"Greatest Increase in Profits: {date[maxmonthlyprofit_index+1]} (${mnthchange[maxmonthlyprofit_index]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {date[maxmonthlyloss_index+1]} (${mnthchange[maxmonthlyloss_index]})\n")



