import os
import csv

#joining path
PyBank_BudgetData = os.path.join("Resources", "PyBank_BudgetData.csv")

# open and read csv
with open(PyBank_BudgetData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header=next(csvreader)
    print (f"CSV Header: {csv_header}")



    # find net amount of profit and loss
    Profit = []
    Months = []

    #read through each row of data after header
    for rows in csvreader:
        Profit.append(int(rows[1]))
        Months.append(rows[0])

    # find revenue change
    RevChange = []

    for x in range(1, len(Profit)):
        RevChange.append((int(Profit[x]) - int(Profit[x-1])))
    
    # calculate average revenue change
    RevAvg = sum(RevChange) / len(RevChange)
    
    # calculate total length of Months
    TotMonths = len(Months)

    # greatest increase in revenue
    GIIP = max(RevChange)
    # greatest decrease in revenue
    GDIP = min(RevChange)


    # print the Results
    print("                    ")

    print("                    ")

    print("                    ")

    print("Financial Analysis")

    print("-------------------------------------")

    print("Total Months: " + str(TotMonths))

    print("Total: " + "$" + str(sum(Profit)))

    print("Average Change: " + "$" + str(RevAvg))

    print("Greatest Increase in Profits: " + str(Months[RevChange.index(max(RevChange))+1]) + " " + "$" + str(GIIP))

    print("Greatest Decrease in Profits: " + str(Months[RevChange.index(min(RevChange))+1]) + " " + "$" + str(GDIP))


    # output to a text file

    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("Total Months: " + str(TotMonths) + "\n")

    file.write("Total: " + "$" + str(sum(Profit)) + "\n")

    file.write("Average Change: " + "$" + str(RevAvg) + "\n")

    file.write("Greatest Increase in Profits: " + str(Months[RevChange.index(max(RevChange))+1]) + " " + "$" + str(GIIP) + "\n")

    file.write("Greatest Decrease in Profits: " + str(Months[RevChange.index(min(RevChange))+1]) + " " + "$" + str(GDIP) + "\n")

    file.close()
