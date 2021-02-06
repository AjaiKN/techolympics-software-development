#**
# *  RaffleBuggy - calculates statistics for the 5th grade bike raffle
# * 
# *

import math
	
bikeCost = float(input("Enter the cost of the bike: "))
overheadCost = float(input("Enter any overhead costs (e.g., printing, incentives): ")) 
ticketPrice = float(input("Enter the ticket price: "))
		
numChildren = 0
totalTickets = 0
maxSold = 0
maxName = ""

print()		
studentName =input("Enter the name of the first student (\"stop\" to quit): ")

while studentName != "stop": 
	ticketsSold = int(input("tickets sold? ")) 
	numChildren = numChildren + 1
	totalTickets += ticketsSold
	if ticketsSold > maxSold:                          
		maxSold = ticketsSold
		maxName = studentName
	studentName = input("Enter the name of the next student (or \"stop\" to quit) ")  

print()
print("To break even you should have sold at least ",end='')
print(math.ceil((bikeCost + overheadCost) / ticketPrice),end='')
print(" tickets ")
                                                                      
print("Average number of tickets sold per child: ",end='')
print(totalTickets/numChildren)
print("Most tickets sold by one child: ",end='')
print(maxSold,end='')
print(" by " + maxName)
print("The class sold " + str(totalTickets) + " tickets worth: $" + str(round(totalTickets * ticketPrice,2)))
print("Total profit from the raffle: $" + str(round(totalTickets * ticketPrice - bikeCost - overheadCost,2)))
