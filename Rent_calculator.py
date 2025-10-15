# Inputs we need from the user
# Total rent
# Total food ordered for snacking
# electricity units spend
# cahrge per unit
# persons living room/flat

# ouput
# Total amount you've to pay is 

rent = int(input("Enter your hostel/flat rent ="))
food  = int(input("Enter the amount of food ordered = " ))
electricity_spend = int(input("Enter the total electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("enter the no of persons living  in room :"))

total_bill = electricity_spend*charge_per_unit

output = (food+rent+total_bill)//persons

print("Each person will pay = " , output)
