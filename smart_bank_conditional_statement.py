print("======WELCOME TO SMART BANK==========")
# USER DATA SAVED
saved_username="manju"
saved_pin="1234"
# Take User Input
username=input("Enter Username")
pin=input("Enter Your PIN")
 
# Account Setup
balance=50000
account_active=True
kyc_done=True
is_premium=True
salary=45000
# cibil=760
# age=24
wrong_attemps=1
foreign_login=False


# Login Check
if not account_active:
  print("Account Blocked Contact to Bank")
elif wrong_attemps>=3:
  print("Too Many Attempts .Account Locked")
elif username==saved_username and pin==saved_pin:
  print("Login Successful")

  # Security Check
  if foreign_login:
    print("Suspicious Login detected")

  # Customer Type
  if is_premium:
    print("Premium Customer")
  else:
    print("Normal Customer")

  # KYC CHECK
  if not kyc_done:
    print("KYC Pending Complete KYC First")
  else:
    print("=======================Choose Option From Menu===================")
    print("\n1.Balance Check")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Fast Cash")
    print("5.Loan Check")
    print("6.Credit Card")
    print("7.Exit")

    choice=int(input("Enter Your Choice "))
    # Balance Check
    if choice==1:
      print("Your Balance is ",balance)
    # Deposit
    elif choice==2:
      deposit=float(input("Enter Deposit Amount"))
      # print("Deposit Successfully Deposit Amount is ",deposit)
      if deposit>0:
        balance+=deposit
        print("Deposit Successfully Deposit Amount is ",deposit)
        print("===========Thank You For Using Smart Bank============================")
      else:
        print("Please Enter Valid Deposit Amount")
        print("===========Thank You For Using Smart Bank============================")
    # Withdraw
    elif choice==3:
      withdraw=float(input("Enter Your Withdrawal Amount"))
      if withdraw<=balance:
        if withdraw>0:
          balance-=withdraw
          print(f"Withdraw Successfully Withdraw Amount is {withdraw} and Remaining Balance is {balance}")
          print("===========Thank You For Using Smart Bank============================")
        else:
          print("Please Enter Valid Withdrawal Amount")
    # Fast Cash
    elif choice==4:
      print("Select Withdraw Amount Option")
      print("1. 500.00")
      print("2.1000.00")
      print("3.2000.00")
      print("4.5000.00")
      option=int(input("Enter Your Option"))
      if option==1:
        if 500<=balance:
          balance-=500
          print("Withdraw Successfully Withdraw Amount is 500 and Remaining Balance is ",balance)
          print("===========Thank You For Using Smart Bank============================")
        else:
          print("Insufficient Balance")
      elif option==2:
        if 1000<=balance:
          balance-=1000
          print("Withdraw Successfully Withdraw Amount is 1000 and Remaining Balance is ",balance)
          print("===========Thank You For Using Smart Bank============================")
        else:
          print("Insufficient Balance")
      elif option==3:
        if 2000<=balance:
          balance-=2000
          print("Withdraw Successfully Withdraw Amount is 2000 and Remaining Balance is ",balance)
          print("===========Thank You For Using Smart Bank============================")
        else:
          print("Insufficient Balance")
      elif option==4:
        if 5000<=balance:
          balance-=5000
          print("Withdraw Successfully Withdraw Amount is 5000 and Remaining Balance is ",balance)
          print("===========Thank You For Using Smart Bank============================")
        else:
          print("Insufficient Balance")
  # Loan Eligibility Check
    elif choice==5:
      enter_salary=float(input("Enter Your Salary"))
      enter_age=int(input("Enter Your Age"))
      enter_cibil=int(input("Enter Your Cibil Score"))
      if enter_salary>=salary and enter_age>=18 and enter_age<= 60 and enter_cibil>=700:
        print("Congratulations 🎉👍 Loan Approved")
        print("===========Thank You For Using Smart Bank============================")
      else:
        print("Your Are Not Eligible For Loan")
        print("===========Thank You For Using Smart Bank============================")
    elif choice==6:
      if is_premium and balance>=50000 and age>=18:
        print("You are Eligible For Applying Credit Card")
        print("===========Thank You For Using Smart Bank============================")
      else:
        print("Your Are Not Eligible For Credit Card")
        print("===========Thank You For Using Smart Bank============================")
    elif choice==7:
      print("===========Thank You For Using Smart Bank============================")
else:
  print("Invalid Credentials")