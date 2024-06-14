"""4. Write a program to calculate discount on the basis of following assumption:
a) If purchased amount is greater than or equal to 1000, discount is 5%
b) If purchased amount is less than 1000, discount is 3%"""

purchase_amount=float(input("Enter the purchase amount :: "))

discount=0.0
if (purchase_amount>=1000):
    discount=(purchase_amount*5)/100.0
    print("Discount Amount :: ",discount)
else:
    discount=(purchase_amount*3)/100.0
    print("Discount Amount :: ",discount)