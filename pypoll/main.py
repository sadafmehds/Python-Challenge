import os
import csv

#write a get the names of the candidates and place them in a list
#in other words remove the duplicates from the candidate names column
def duplicate_remover(candidate_name_column):
    unique_candidates=[]
    for i in candidate_name_column:
        if i not in unique_candidates:
            unique_candidates.append(i)
    return(unique_candidates)

#Initial empty lists:
list_candid=[]      #candidate names column list
votes_per_candidate=[]  #list of number of votes counted for each candidate

#give csv path and read file
csvpath=os.path.join("..","Resources","election_data_2.csv")
with open(csvpath,newline="") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    next(csv_reader) #skip header/title row of csv

    #convert the reader to a list to be able to loop several times in csv.reader and manuver over csv columns seperately
    csv_reader=list(csv_reader)

    #get length of the reader list of lists to get total number of votes
    total_votes=len(csv_reader)

    #Make candidate names column a list by filling the empty list list_candid
    for i in csv_reader:
        list_candid.append(i[2])
    
    #count number of votes for each candidate that participated by counting how many times a candidate's name appeared in candidate names column list
    # candidates that participate come from unique_candidates list via calling duplicate_remover function 
    for word in duplicate_remover(list_candid):
        candid_votes=list_candid.count(word)
        votes_per_candidate.append(candid_votes)

    #Make the list containing the name of candidates (unique_candidates list) and the list containing number of votes per candidate (votes_per_candidate list) into one dictionary
    name_vote_dicti=dict(zip(duplicate_remover(list_candid),votes_per_candidate))
    
    #identify the maximum number of votes the winnder received, from list containing number of votes per each candidate
    maximum_vote=max(votes_per_candidate)
    #get the index of maximum number of votes of potential winner
    winner_index=votes_per_candidate.index(maximum_vote)
    #use that index to get the name of the winner from the list containing the names of each candidate
    winner=duplicate_remover(list_candid)[winner_index]

print("---\n    Election Results")
print("Total Votes: "+str(total_votes))
print("----------------------------------")
#Iterate over keys and values of the candidate name and number of votes received dictionary to print each candidate name, percentage of votes and number of votes received
for i,j in name_vote_dicti.items():
    rounded_percent=round((j/total_votes)*100,1)    #round percentage of votes to 1 decimal place
    print(str(i) +": "+ str(rounded_percent) +"%"+" ("+str(j)+")")
print("----------------------------------")
print("Winner: "+str(winner))
print("---")
