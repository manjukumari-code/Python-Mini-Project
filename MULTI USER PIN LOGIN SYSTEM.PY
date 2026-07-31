print("=====================MULTI USER PIN LOGIN SYSTEM=========================")
user=1
while user<=3:
    print(f"\n User {user}")
    attempts=1
    while attempts<=3:
        pin=int(input("Enter your PIN: "))
        if pin==pins[user]:
            print("LOGIN SUCCESSFULLY")
            print("User Attempts:", attempts)
            break
        else:
            print("Wrong PIN Entered")
            print(f"You have {3-attempts} chances left")
        attempts+=1
    if attempts>3:
        print("Your Account has been blocked for 24 hours")
    user+=1
