"""Generate sales report showing total melons each salesperson sold."""


salespeople = []    #create an empty list for salespeople (to add to later)
melons_sold = []    #create and empty list for melons_sold (to add to later)

f = open('sales-report.txt') #open the file sales-report.txt, save it to variable 'f'

for line in f: #iterate through each line in the sales report
    line = line.rstrip()    #trim away extra white spaces at the end of each line
    entries = line.split('|')   #split each line at the '|' (create a list of data)
    salesperson = entries[0]    #first entry of each line is the salesperson
    melons = int(entries[2])    #the third entry of each line is the number of melons (converted to and integer)

    if salesperson in salespeople: #condition set that if a salesperson is in the list salespeople
        position = salespeople.index(salesperson) #this will save the position of the first occurance of a salesperson to the position variable
        melons_sold[position] += melons #this adds melons to the melons_sold list if the salesperson was already in the list of salespeople once
        
    else:
        salespeople.append(salesperson) #if not, add the new salesperson to the list salespeople
        melons_sold.append(melons) #if not, add melons to the melons_sold list


for i in range(len(salespeople)): # for salesperson in the salespeople list:
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') #print salesperson at index i sold a number of melons at index i melons