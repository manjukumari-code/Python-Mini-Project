# QUESTION NO 3:- Project: Dynamic Pricing Engine

# Create a Python program for an e-commerce website.

# The program should take the following inputs:

# Product Price
# User Type (VIP / Normal)
# Festival Running (Yes / No)
# Stock Left
# Rules:
# If the user is VIP → apply 20% discount
# If a festival is running → apply an additional 10% discount
# If stock ≤ 5 → increase price by 15%
# If stock ≤ 10 → increase price by 8%
# Apply discount first, then apply price increase
# Output Should Include:
# Original Price
# Final Payable Price
# Total Discount (%)
# Stock Increase (%)
# Smart Messages:
# If total discount ≥ 30% → display "Best Deal Applied"
# If stock ≤ 5 → display "Hurry! Only Few Items Left"
# If final price ≥ 100000 → display "Premium Purchase Detected"
# After generating the bill → display "Thank You!"
    
print("=======Dynamic Pricing Engine=======")
# input
product_price=float(input("Enter Your Product Price"))
user_type=input("Enter Your User Type(VIP/Normal)").lower()
festival_running=input("Enter Your Festival Running Status(YES/NO)").lower()
stock_left=int(input("Enter Your Stock Left"))

# Base price
final_price=product_price
discount=0
increase=0

# VIP Customer Discount Logic

if user_type=="vip":
  discount+=20

# Festival Discount
if festival_running=="yes":
  discount+=10

# Stock Increase Logic
if stock_left<=5:
  increase+=15
elif stock_left<=10:
  increase+=8
# Apply discount first,then increase
discount_amount=(final_price*discount)/100
print(discount_amount)
stock_amount=(final_price*increase)/100
print(stock_amount)
final_price=final_price-discount_amount

# Output

print("===========Bill Summery===========")
print("Original Price: ",product_price)
print("Total Discount:",discount,"%")
print("Stock Increase:",increase,"%")
print("Final Payable Price",final_price)

# Messages

if discount>=30:
  print("Best Deal Applied")

if stock_left<=5:
  print("Hurry! Only Few Items Left")
if final_price>=100000:
  print("Premium Purchase Detected")
print("=============Thank You!===========================")

