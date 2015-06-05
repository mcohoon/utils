def sum(lhs, rhs):
    return lhs + rhs

prices = [2800,2300,3000,3300,5000,1890,2600,2400]

print "the average price is: ",

average = reduce(sum,prices)/len(prices)

print str(average)

print "Damn thats high!"
