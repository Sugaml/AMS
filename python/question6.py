amount=int(input("Enter Principal Amount :: "))
# print("Enter amount is {}".format(amount))

def interest_calculate(p):
    if (p>99999):
        si=((p*1*7)/1000)
        return si
    elif (p>=50000 and p<100000):
        si=((p*1*5)/100)
        return si
    elif(p<50000):
        si=((p*1*3)/100)
        return si
    
interest=interest_calculate(amount)
print("Calculated Rate :: ",interest)

