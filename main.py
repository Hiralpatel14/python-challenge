import os
import csv
print(os.chdir(os.path.dirname(__file__)))

#give the path to collect data from Resource folder
#Bfile_csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

BFile_csv = os.path.join("Resources/budget_data.csv")

#read csv file
with open(BFile_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # Read the header row first otherwise skip this if there is no header
    csv_header = next(csvfile)
   
    print("Header: " + str(csv_header))

    total_months = 0
    total_netAmount = 0
    prev_netAmount = 0
    avg_chng_list = []
    month_change = []
    inc_prof = ['',0]
    dec_loss = ['', 999999999]

    #loop through data and read each rows after the header 
    for row in csvreader:

        #count total months
        total_months = total_months + 1
        
        # calculate total net amount over entire period
        total_netAmount += int(row[1])
        print(total_netAmount)

        avg_change = int(row[1]) - prev_netAmount
        print(avg_change)

        prev_netAmount = int(row[1])

        avg_chng_list = avg_chng_list + [avg_change]
       # print([avg_chng_list])
        
        month_change = month_change + [row[0]]
       # print(month_change)

        #greatest increase profit
        if avg_change > inc_prof[1]:
            inc_prof[1] = avg_change
            inc_prof[0] = row[0]

        #greatest decrease losses
        if avg_change< dec_loss[1]:
            dec_loss[1]= avg_change
            dec_loss[0] = row[0]

#print rev_change list
rev_avg = sum(avg_chng_list)/ len(avg_chng_list)

#print on screen
print("Financial Analysis")
print("---------------------------------")
print("Total Months: " + str(total_months))
print("Total : $" + str(total_netAmount))
print("Average Change : $" + str(rev_avg ))
print("Greatest Increase in Profit : "+ str(inc_prof))
print("Greatest decrease in Profits: " + str(dec_loss))
#print(avg_change)







    

