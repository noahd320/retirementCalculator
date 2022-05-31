#Asking for users Full Name, Current Age, Desired Retirement Age, Current Retirement Savinds, and Amount needed to retire
fullName = input("What is your full name?: ")
currentAge = int(input("How old are you?: "))
 break
  except: 
    print ("Please input as a number")
desiredRetirementAge = int(input("What age do you want to retire at?: "))
 break
  except: 
    print ("Please input as a number")
currentRetirementSavings = int(input("How much do you currently have in savings for retirement?: "))
 break
  except: 
    print ("Please input as a number")
desiredRetirementSavings = int(input("How much money do you need to retire?: "))
 break
  except: 
    print ("Please input as a number")

#Calculate how many years until retirement age
yearsRemaining = int(desiredRetirementAge) - int(currentAge)

#Calculate how far away retirement savings goal is
retirementMoney =  int(desiredRetirementSavings) - int(currentRetirementSavings)

#Calculate savings amount per year to retire
perYear = int(retirementMoney) / int(yearsRemaining)

#Statement on years left until retirement and money needed to retire
print (fullName[0].uppercase + " you have", yearsRemaining, " until you can retire.")
print ("You need", retirementMoney, " in order to retire.")
print ("You should save", perYear, " per year to retire on time.")
