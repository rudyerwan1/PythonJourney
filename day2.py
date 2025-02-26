#Tips calculator
print(" Hey buddy my name is layana let me be your next tips calculator")

bill_amount= float(input("What is the total bill? \n"))

tips_amount =int(input("How much tips would you like to give ? 10,12,15 \n"))
if tips_amount == 15 :
    print(" Waouh you so generous!")
else :
    print("Thank you buddy ")
people_shared = int(input("How many people will shared the bill?\n"))

total_to_pay =  (bill_amount * (1+ (tips_amount/100))) / people_shared

#remeber how to around float number with f string class
print(f"Each person would have to pay $ {total_to_pay:.2f}")