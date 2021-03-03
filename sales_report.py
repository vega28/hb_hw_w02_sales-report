"""Generate sales report showing total melons each salesperson sold."""

# initialize lists to store info for salespeople and their melons sold:
salespeople = []
melons_sold = []

f = open('sales-report.txt') # open report file
for line in f:
    line = line.rstrip() # remove whitespace and end-line chars
    entries = line.split('|') # parse line: split at |s and put in a list
    # assign variables for specific data:
    salesperson = entries[0] 
    melons = int(entries[2])

    # check if the salesperson is already listed
    if salesperson in salespeople:
        # determine the index of that entry to compare to melons_sold
        position = salespeople.index(salesperson)
        # add the new melons sold to the melons list
        melons_sold[position] += melons
    else: 
        # add salesperson and melon count to the end of their respective lists
        salespeople.append(salesperson)
        melons_sold.append(melons)

# print out report of salespeople and how many melons each sold:
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
