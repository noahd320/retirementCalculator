#Asking for users Full Name, Current Age, Desired Retirement Age, Current Retirement Savinds, and Amount needed to retire
fullName = input("What is your full name?: ") 
currentAge = input("How old are you?: ")
desiredRetirementAge = input("What age do you want to retire at?: ")
currentRetirementSavings = input("How much do you currently have in savings for retirement?: ")
desiredRetirementSavings = input("How much money do you need to retire?: ")

#Calculate how many years until retirement age
yearsRemaining = int(desiredRetirementAge) - int(currentAge)

#Calculate how far away retirement savings goal is
retirementMoney =  int(desiredRetirementSavings) - int(currentRetirementSavings)

#Calculate savings amount per year to retire
perYear = int(retirementMoney) / int(yearsRemaining)

#Statement on years left until retirement and money needed to retire
print (fullName + " you have", yearsRemaining, " until you can retire.")
print ("You need", retirementMoney, " in order to retire.")
print ("You should save", perYear, " per year to retire on time.")
