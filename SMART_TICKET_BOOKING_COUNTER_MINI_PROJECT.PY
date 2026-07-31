print("*****************************SMART TICKET BOOKING COUNTER***************************")

# base system
total_seats=50
ticket_price=500
sold_tickets=0
total_amount=0

# loop for multiple ticket booking
while total_seats>0:
    print("\n Available seats=",total_seats)           # check remaining seats 
    user_input=int(input("enter number of tickets to book:"))
    
    
    #invalid input handling
    if user_input<=0:
        print("enter valid number of tickets.")
        continue
    elif user_input>total_seats:
        print("not enough seats available")
        continue
    
    # price calculation
    ticket_amount=user_input*ticket_price
    print("booking successfull")
    print("your booking ticket amount=",ticket_amount)
    
    #update data
    total_seats=total_seats-user_input
    sold_tickets=sold_tickets+user_input
    total_amount=total_amount+ticket_amount

# booking closed final sales report 
print("===========BOOKING CLOSED============")
print("total sold ticket=",sold_tickets)
print("total amount after sold all tickets=",total_amount)
print("remaining seats=",total_seats)