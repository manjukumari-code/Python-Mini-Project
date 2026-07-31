# Question 2: Fraud Transaction Detection System
# Scenario:

# Determine whether a payment is suspicious or not.

# Inputs:
# Amount
# Location (mention the country name)
# Device Changed (Yes/No)
# OTP Verified (True/False)
# Rules:
# If Amount > 5000 and device is changed → mark as "Suspicious Transaction"
# If OTP is not verified (False) → mark as "Transaction Blocked"
# If the transaction is from a foreign location → mark as "Verify Manually"
# (Transactions from India are considered approved)

print("===================FRAUD TRANSACTION DETECTION===============")
amount=float(input("enter amount="))
location=input("mention here country name=").lower()
device_changed=input("device change? yes/no:").lower()
otp_verified=input("enter otp? true/false:").lower()
aproved_location="india"
if otp_verified=="false":
    print("block")
elif location!=aproved_location:
    print("verify manually")
elif amount>=5000 and device_changed=="yes":
    print("suspicious payment")
else:
    print("transaction aproved")

