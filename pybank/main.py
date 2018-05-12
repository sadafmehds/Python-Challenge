import os
import csv
#maxi function identified to get the maximum number in a list and give its index in the list together as a list
def maxi(any_list):
    s=any_list[0]
    for i in any_list:
        if i>s:
            maxi=i
            date_index=any_list.index(i)
    return([date_index,maxi])

#min function identified to get the minimum number in a list and give its index in the list together as a list
def min(any_list):
    s=any_list[0]
    for i in any_list:
        if i<s:
            min=i
            date_index=any_list.index(i)
    return([date_index,min])

#initiating lists
list_date=[]
list_rev=[]
list_change=[]

csv_path=os.path.join("..","Resources","budget_data_1.csv")
with open(csv_path,newline="") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    next(csv_reader)               # skip title line
    csv_reader = list(csv_reader)  # turn the reader into a list
    count = len(csv_reader)        # since we converted reader to list, now we can use len method to get total months from length of csv observations

    # compute total by summing every second col of each row
    total = sum(int(mylist[1]) for mylist in csv_reader)
    
    #turn each column into its own separate list, store into date and revenue lists (list_date and list_rev)
    for i in csv_reader:
        list_date.append(str(i[0]))
        list_rev.append(float(i[1]))

    #create a difference list as list_change by differencing the revenues in list_rev
    for i in range(0,len(list_rev)-1):
        list_change.append(list_rev[i+1]-list_rev[i])

    #compute average change from the computed differences in list_change
    for j in list_change:
        average_diff=sum(list_change)/len(list_change)

    print("             Financial Analysis\n-------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Revenue: " + str(total))
    print("Average Revenue Change: "+str(average_diff))
    #predefined maxi,mini functions return max and min values and the index of values in the same list
    #slice dates list (list_date) via the returned index
    #get max/min values via index 1 of both maxi/min functions
    print("Greatest Increase in Revenue: "+str(list_date[maxi(list_change)[0]])+" ("+ str(maxi(list_change)[1])+")")
    print("Greatest Decrease in Revenue: "+str(list_date[min(list_change)[0]])+" ("+ str(min(list_change)[1])+")")
