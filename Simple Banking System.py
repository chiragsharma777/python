balance = 10000

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance: ₹", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("₹", amount, "deposited successfully.")
            print("New Balance: ₹", balance)
        else:
            print("Invalid amount.")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance = balance - amount
            print("₹", amount, "withdrawn successfully.")
            print("Remaining Balance: ₹", balance)

    elif choice == 4:
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice. Please try again.")