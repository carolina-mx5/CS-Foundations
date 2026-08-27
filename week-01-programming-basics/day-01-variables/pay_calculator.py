# takes user string input
hr_worked = input("Hours worked: ")
hr_rate = input ("Hourly rate: ")

# converts string input into float
hr_worked = float(hr_worked)
hr_rate = float(hr_rate)

# calculates gross pay and roounds to 2 decimal places
gross_pay = hr_worked * hr_rate
gross_pay = round(gross_pay, 2)

# calculates tax and rounds to 2 decimal places
tax = gross_pay * 0.15
tax = round(tax, 2)

# calculates take home pay and rounds to 2 decimal places
take_home = gross_pay - tax
take_home = round(take_home, 2)

# prints calculations 
print("\n----- PAY SUMMARY -----")
print("\nGross Pay:       $" + f"{gross_pay:.2f}")
print("Tax:             $" + f"{tax:.2f}")
print("Take-Home Pay:   $" + f"{take_home:.2f}")