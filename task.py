print("Bill splitter And Tip Calculator")
bill = float(input("What was the total bill? rs"))
tip = int(input("What percentage tip would you like to give?0 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percentage = tip/100
total_tip = bill * tip_percentage
total_bill = round(bill + total_tip,2)
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
print(f"Your final bill+tip is rs{total_bill}")
print(f"each person should pay:rs{final_amount}")
print("thank you have a great day!!")
