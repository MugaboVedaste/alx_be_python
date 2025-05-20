salary = int(input("Enter your monthly income:"))
expense = int(input("Enter your total monthly expenses:"))
msaving = salary - expense
asaving = msaving * 12 + (msaving * 12 * 0.05)
print("Your monthly savings are $",msaving)
print("Projected savings after one year, with interest, is: $",asaving)