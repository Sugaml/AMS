"""5. Write a program to calculate discount on the basis of following assumption:
a) If purchased amount is greater than or equal to 5000, discount is 10%
b) If purchased amount is greater than or equal to 4000 and less than 5000, discount is 7%
c) If purchased amount is greater than or equal to 3000 and less than 4000, discount is 5%
d) If purchased amount is greater than or equal to 2000 and less than 3000, discount is 3%
e) If purchased amount is less than 2000, discount is 2%"""

purchase_amount=float(input("Enter the purchase amount :: "))

discount=0.0
if (purchase_amount>=5000):
    discount=(purchase_amount*10)/100.0
    print("Discount Amount :: ",discount)
elif (purchase_amount>=4000):
    discount=(purchase_amount*7)/100.0
    print("Discount Amount :: ",discount)
elif (purchase_amount>=3000):
    discount=(purchase_amount*5)/100.0
    print("Discount Amount :: ",discount)
elif (purchase_amount>=2000):
    discount=(purchase_amount*3)/100.0
    print("Discount Amount :: ",discount)
else:
    discount=(purchase_amount*2)/100.0
    print("Discount Amount :: ",discount)