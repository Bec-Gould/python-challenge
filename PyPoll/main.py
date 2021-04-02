# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# Import Data 
import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname,"Resources","election_data.csv")

Total_Votes = 1
Candidate = 0

# Open csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    # Print Header
    csv_header = next(csv_reader)
    #print(f"Header:{csv_header}")

    #create variable for first row
    first_row = next(csv_reader)
    #print(first_row)

    #Create empty list
    Candidates_List = []
    Candidate_Vote = {}

    # Loop through data
    for row in csv_reader:    
        
        Total_Votes = Total_Votes + 1
      
        #Create list with candidates
        Candidate = str(row[2]) 
        if not Candidate in Candidates_List:
            Candidates_List.append(Candidate)
            Candidate_Vote[Candidate]=1
         
        else: 
            Candidate_Vote[Candidate]+=1
            
    #print(Candidate_Vote)

    Khan_Votes = round(Candidate_Vote["Khan"]/Total_Votes*100,3)
    Correy_Votes = round(Candidate_Vote["Correy"]/Total_Votes*100,3)
    Li_Votes = round(Candidate_Vote["Li"]/Total_Votes*100,3)
    OTooley_Votes = round(Candidate_Vote["O'Tooley"]/Total_Votes*100,3)
    
    #Find Winner
    Winner =max(Candidate_Vote,key=Candidate_Vote.get)
    
    # print(Khan_Votes)
    # print(Correy_Votes)
    # print(Li_Votes)
    # print(OTooley_Votes)
    # print(Candidates_List)
    # #print(Candidate_Vote["Khan"])
    # print(Candidate_Vote) 

    #print Election Results
    Title = "Election Results"
    print(Title)
    print("---------------------")
    print(f"Total Votes: {Total_Votes}")
    print("Khan: {}% ({}) ".format(Khan_Votes, Candidate_Vote["Khan"])) 
    print("Correy: {}% ({}) ".format(Correy_Votes, Candidate_Vote["Correy"])) 
    print("Li: {}% ({}) ".format(Li_Votes, Candidate_Vote["Li"])) 
    print("O'Tooley: {}% ({}) ".format(OTooley_Votes, Candidate_Vote["O'Tooley"])) 
    print("---------------------")
    print(f"Winner: {Winner}")
    print("---------------------")
 
    #Write text file
    PyPoll_Analysis = os.path.join(dirname,"PyPoll_Analysis.txt")
    with open(PyPoll_Analysis,'w') as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("---------------------\n")
        txtfile.write(f"Total Votes: {Total_Votes}\n")
        txtfile.write("Khan: {}% ({})\n".format(Khan_Votes, Candidate_Vote["Khan"])) 
        txtfile.write("Correy: {}% ({})\n".format(Correy_Votes, Candidate_Vote["Correy"])) 
        txtfile.write("Li: {}% ({})\n".format(Li_Votes, Candidate_Vote["Li"])) 
        txtfile.write("O'Tooley: {}% ({})\n".format(OTooley_Votes, Candidate_Vote["O'Tooley"]))
        txtfile.write("---------------------\n")
        txtfile.write(f"Winner: {Winner}\n")
        txtfile.write("---------------------\n") 