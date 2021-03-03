"""Generate sales report showing total melons each salesperson sold."""


sales_data = {} # dict datatype for better organization of associated data

# read in file & parse data:
f = open('sales-report.txt') 
for line in f:
    line = line.rstrip() # remove whitespace and end-line chars
    salesperson, sale_amt, melons = line.split('|') # parse line

    # update dict with this sale info:
    sales_data[salesperson] = sales_data.get(salesperson, 0) + int(melons)

# print out alphabetized report of salespeople and how many melons each sold:
for salesperson in sorted(sales_data): 
    print(f'{salesperson} sold {sales_data[salesperson]} melons')


# --- NTH improvements - ALL COMPLETE --- #
# store salespeople and their associated melons in a dict
#   keeps associated data together! removes possible errors related to indexing
#   easier to add/update melons in this format
# when reading in file: unpack each line directly into variables
#   mostly a style thing, but more elegant!
# alphabetize report 