#simple interest calculator
amount=int(input("Enter the amount of money: "))
interest_rate=float(input("Enter the interest rate: "))
time=int(input("Enter the time duration in months: "))
total_interest=amount*interest_rate*time*0.01
total_money=amount+total_interest
print("The total money is:",total_money)