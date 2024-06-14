"""3. Write a program to calculate discount on the basis of following assumption:
a) If purchased amount is greater than or equal to 1000, discount is 5%"""

purchase_amount=float(input("Enter the purchase amount :: "))

discount=0.0
if (purchase_amount>=1000):
    discount=(purchase_amount*5)/100.0
    print("Discount Amount :: ",discount)
else:
    print("Discount is not available")
