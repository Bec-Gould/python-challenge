# Import Data 
import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname,"Resources","budget_data.csv")

Total_Months = 1
Profit_Loss = 0
Greatest_Date = "1900"
Greatest_Value = 0
Lowest_Date = "1900"
Lowest_Value = 999999999999

# Open csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    # Print Header
    csv_header = next(csv_reader)
    #print(f"Header:{csv_header}")

    #create variable for first row
    first_row = next(csv_reader)
    #print(first_row)
    
    Change = int(first_row[1])

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
            
        if Change > Greatest_Value:
            Greatest_Value = Change
            Greatest_Date = row[0]
        if Change < Lowest_Value:
            Lowest_Value = Change
            Lowest_Date = row[0]

        Change = int(row[1])

    #print(Greatest_Date)

    #print(Change_List)

    #print(sum(Change_List))

    #Calculate the average change
    Average_Change = (sum(Change_List)/(Total_Months -1))

    #print Financial Analysis
    Title = "Financial Analysis"
    print(Title)
    print("---------------------")
    print(f"Total Months:{Total_Months}")
    print(f"Profit Loss:{Profit_Loss}")
    print(f"Average Change:{Average_Change}")
    print("Greatest Increase in Profits: {} (${}) ".format(Greatest_Date, Greatest_Value)) 
    print("Greatest Decrease in Profits: {} (${}) ".format(Lowest_Date, Lowest_Value)) 
 
    #Write text file
    PyBank_Analysis = os.path.join(dirname,"PyBank_Analysis.txt")
    with open(PyBank_Analysis,'w') as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("---------------------\n")
        txtfile.write(f"Total Months:{Total_Months}\n")
        txtfile.write(f"Profit Loss:{Profit_Loss}\n")
        txtfile.write(f"Average Change:{Average_Change}\n")
        txtfile.write("Greatest Increase in Profits: {} (${})\n".format(Greatest_Date, Greatest_Value)) 
        txtfile.write("Greatest Decrease in Profits: {} (${})\n ".format(Lowest_Date, Lowest_Value)) 
 