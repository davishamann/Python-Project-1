#Davis Hamann       NetID: dch360
#Date: 2/10/2019    Due Date: 2/10/2019
#this prgoram keeps you on budget with how much you earn and how much you want to save

print("Hello!  Welcome to your budget buddy.")
print("We take in how much you make versus how much you spend and tell you whether you achieved a saving goal.")

make=float(input("How much do you make in a month?"))
save=float(input("How much do you want to save in a month?"))
budget=make-save
print("Your budget is $",format(budget,'.2f'),"for the month")

print("Now we'll see how much you spent this moth.")
rent=float(input("How much did you spend on rent?"))
utilities=float(input("How much did you spend on utilities?"))
food=float(input("How much did you spend on food?"))
otherPurchases=float(input("How much did you spend on other miscellaneous purchases?"))
spent=rent+utilities+food+otherPurchases
print("Calculating....")
print("You spent $",format(spent,'.2f'),"total this month.")
remainingBudget=budget-spent
if (remainingBudget <= 5 and  remainingBudget >= -5):
    print("Your on budget!")
elif (remainingBudget <= -6):
    print("You went over budget!")
    print("You went over budget by:$",format(abs(remainingBudget),'.2f'))
elif (remainingBudget >= 6):
    print("You came under budget!")
else:
    print("ERROR")
                
           
