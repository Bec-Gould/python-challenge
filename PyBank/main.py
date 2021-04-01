# Import Data 
import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname,"Resources","budget_data.csv")

Total_Months = 1
Profit_Loss = 0
Change = 867884

# Open csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    # Print Header
    csv_header = next(csv_reader)
    print(f"Header:{csv_header}")

    #create variable for first row
    first_row = next(csv_reader)
    #print(first_row)


    Profit_Loss = int(first_row[1])
    
    #Create empty list
    Change_List = []
    
    # Loop through data
    for row in csv_reader:    
        
        Total_Months = Total_Months + 1
        Profit_Loss = int(row[1]) + Profit_Loss       
        
        #Create list with changes
        Change = int(row[1]) - Change 
        Change_List.append(Change)
        Change = int(row[1])

    #print(Change_List)

    #print(sum(Change_List))

    #Calculate the average change
    Average_Change = (sum(Change_List)/(Total_Months -1))

    #Find min/max value
    max_value = max(Change_List)
    min_value = min(Change_List)
   

    for row in csv_reader:

        if int(row[1]) == max_value:
            print(row)

    #print Financial Analysis
    Title = "Financial Analysis"
    print(Title)
    print("---------------------")
    print(f"Total Months:{Total_Months}")
    print(f"Profit Loss:{Profit_Loss}")
    print(f"Average Change:{Average_Change}")
    print(f"Greatest Increase in Profits:{max_value}")
    print(f"Greatest Decrease in Profits:{min_value}")
 
    #Write text file
    PyBank_Analysis = os.path.join(dirname,"PyBank_Analysis.txt")
    with open(PyBank_Analysis,'w') as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("---------------------\n")
        txtfile.write(f"Total Months:{Total_Months}\n")
        txtfile.write(f"Profit Loss:{Profit_Loss}\n")
        txtfile.write(f"Average Change:{Average_Change}\n")
        txtfile.write(f"Greatest Increase in Profits:{max_value}\n")
        txtfile.write(f"Greatest Decrease in Profits:{min_value}\n")