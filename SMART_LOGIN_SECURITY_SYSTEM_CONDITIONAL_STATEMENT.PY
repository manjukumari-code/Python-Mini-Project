# Question 1:- Smart Login Security System

# A company wants to build a login system.

# When a user tries to log in, they must provide the following details:

# Username
# Password
# OTP (One-Time Password)
# Number of wrong attempts
# Whether the account is active or not
# Rules:
# If the account is inactive → display "Contact Admin"
# If wrong password attempts are 3 or more → display "Account Locked"
# If username and password are correct and OTP is also correct → display "Login Successful"
# If OTP is incorrect → display "Wrong OTP"
# If username or password is incorrect → display "Invalid Credentials"

print("==================SMART LOGIN SECURITY SYSTEM===================")
username=input("enter your username=")
password=int(input("enter password="))
otp=int(input("enter otp="))
wrong_attempt=int(input("enter wrong attempt count="))
is_active=input("is acount active yes/no=").lower()
correct_username="manju"
correct_password=1234
correct_otp=9999
if is_active=="no":
    print("contact admin.")
elif wrong_attempt>=3:
    print("your account is locked.")
elif username==correct_username and password==correct_password:
    if otp==correct_otp:
        print("login successfully!")
    else:
        print("wrong otp.")
else:
    print("invalid credentials")

