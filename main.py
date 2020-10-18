import csv
import os

# Path to collect data from the Resources folder
bank_csv = os.path.join("PyBank","Budget_Data.csv")

def PL_Bank(data):

    # Variables
    month_count = 0
    Profit = 0
    Months = []
    Total_Profit = 0
    AverageChange = 0
    Sum_AvgChange = []
    
    for row in csvreader:
        # The total number of months in the dataset.
        month_count = month_count + 1
        
        # The net total amount of "Profits/Losses" over the entire period.
        Total_Profit = Total_Profit + int(row[1])
        Months.append(str(row[0]))
        
        # The average of the changes in the "Profit/Losses" over the entire period.
        if AverageChange != 0:
            # 1st Profit
            Profit = int(row[1])

            AverageChange = Profit - AverageChange
            # Store Average Change
            Sum_AvgChange.append(AverageChange)
            # Reset
            AverageChange = int(row[1])

        elif AverageChange ==0:
            AverageChange = int(row[1])

    Months.pop(0)

    # The greatest increase in profits (Date and Amount) over the entire period.
    Greatest_Increase = Sum_AvgChange.index(max(Sum_AvgChange))
    Greatest_Decrease = Sum_AvgChange.index(min(Sum_AvgChange))

    # For Months
    MonthIncrease = (Months[int(Greatest_Increase)], max(Sum_AvgChange))
    MonthDecrease = (Months[int(Greatest_Decrease)], min(Sum_AvgChange))

    Average = sum(Sum_AvgChange)/len(Sum_AvgChange)
    # Print the results
        
    print("  Fianancial Analysis")
    print("-----------------------------------")
    print(f"Total months is: {month_count}" )
    print(f"The total is: {Total_Profit}" )
    print(f"The average change is: {round(Average,2)} ")
    print(f"The greatest increase in profit is: {MonthIncrease}" )
    print(f"The greatest decrease in profit is: {MonthDecrease}")

    # This will let us write the picked records in a new file.
    with open("PyBanktxt",'w') as txtfile:
        txtfile.write("      Fianancial Analysis")
        print("\n--------------------------------------")
        txtfile.write(f'\n Total months is: {month_count}')
        txtfile.write(f'\n The total is: {Total_Profit}')
        txtfile.write(f'\n The average change is: {round(Average,2)}')
        txtfile.write(f'\n The greatest increase in profit is: {MonthIncrease}')
        txtfile.write(f'\n The greatest decrease in profit is: {MonthDecrease}')    

with open(bank_csv, 'r') as csvfile:    # This will open the file
    csvreader = csv.reader(csvfile)    # Reading file after opening.
    header = next(csvreader)          # Skip header

    PL_Bank(csvreader)
  
   
#PyPoll

import csv
import os

# Path to collect data from the Resources folder
poll_csv = os.path.join("PyPoll" , "Election_Data.csv")

V_Count = 0
candList = []
candtotal = []

with open(poll_csv, 'r') as csvfile:    # This will open the file
    csvreader = csv.reader(csvfile)    # Reading file after opening.
    header = next(csvreader)          # Skip header

    for row in csvreader:
        # The total number of votes cast.
        V_Count = V_Count + 1
    

# A complete list of candidates who recieved votes.
        candidate = row[2]
        # Votes per candidate
        if candidate in candList:
            candidate_index = candList.index(candidate)
            candtotal[candidate_index] = candtotal[candidate_index] + 1
        else:
            candList.append(candidate)
            candtotal.append(1)
# The percentage of votes each candidate won.
    most_votes = candtotal[0]
    percentage = []
    most_candidate = 0
    for count in range(len(candList)):
        vote_percentage = (candtotal[count]/V_Count)*100
        percentage.append(vote_percentage)
# The winner of the election based on the popular vote.
        if candtotal[count] > most_votes:
            most_candidate = count
    winner = candList[most_candidate]



print("Election Results")
print("---------------------------------")
print(f"Total Votes: {V_Count}")
print("---------------------------------")
for count in range(len(candList)):
    print(f"{candList[count]} : {round(percentage[count],2)} % {candtotal[count]}")
print("---------------------------------")
print (f"Winner : {winner} ")
print("---------------------------------")

# This will let us write the picked records in a new file.
with open("PyPolltxt",'w') as txtfile:
    txtfile.write("         Election Results")
    txtfile.write(f"\n ---------------------------------")
    txtfile.write(f"\n Total Votes: {V_Count}")
    txtfile.write("\n---------------------------------")
    for count in range(len(candList)):
        txtfile.write(f"\n{candList[count]} : {round(percentage[count],2)} % {candtotal[count]}")
    txtfile.write("\n---------------------------------")
    txtfile.write(f"\n Winner : {winner} ")
    txtfile.write("\n---------------------------------")
         