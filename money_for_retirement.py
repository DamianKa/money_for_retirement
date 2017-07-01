#how much you need to retire
print ("The How Much You Need to Retire Calculator")
monthly_spend = int(input("How much money in terms of today's money will you need on retirement (per month)?  £"))
ir = int(input("What return from investments you can achieve in the long term?  %"))
inflation = int(input("What average real inflation should I include in the calculation?  %"))

real_ir = ir - inflation
that_much = monthly_spend /  (real_ir / (100 * 12))

print ("You need ", that_much, " £ to retire") 
