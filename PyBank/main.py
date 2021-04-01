# Import Data 
import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname,"Resources","budget_data.csv")

Total_Months = 0
#Total = 0
#Average_Change = 0


# Open csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    # Print Header
    csv_header = next(csv_file)
    print(f"Header:{csv_header}")

    #next(csv_reader, None)

    Total_Months = 0
    Profit_Loss = 0
    Average_Change = 0

    # Loop through data
    for row in csv_reader:
        
        Total_Months = Total_Months + 1
        Profit_Loss = int(row[1]) + Profit_Loss
        Average_Change = Profit_Loss / Total_Months

 
    print(f"Total Months:{Total_Months}")
    print(f"Profit Loss:{Profit_Loss}")
    print(f"Average Change:{Average_Change}")


  
    