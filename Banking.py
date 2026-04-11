#Python banking program

def show_balance():
    global balance
    print(f"Your current balance is {balance:.2f}/-")

def Deposit_money():
    global balance
    dm = float(input("Enter the amount you need to deposit: "))
    if dm < 0:
        print("That's not a valid amount.Insufficient funds to deposit")
        return 0
    else:
        balance += dm
        print("The amount had been added succesfully.")
        print(f"Your updated balance is {balance:.2f}/- now")

def Withdraw_money():
    global balance
    wm = float(input("Enter the money you need to withdraw: "))
    if wm < 0:
        print("Amount must be greater than 0 to withdraw")
        return 0
    elif wm > balance:
        print(f"You have a low balance to withdraw.Your current balance is {balance}")
    else:
        balance -= wm
        print("Withdrawel succefully executed..")
        print(f"Your updated balance after withdrawel of money is {balance:.2f}")

balance = 0
is_running = True
print("Welcome to SBI BANK....")
print("Which operation you would like to perform?")
while is_running:
    print(" 1.Check Balance\n 2.Deposit Money\n 3.Withdraw Money\n 4.Exit the bank")
    Op = (input("Enter your operation to perform (1-4):"))
    if Op == '1':
        show_balance()
    elif Op == '2':
        Deposit_money()
    elif Op == '3':
        Withdraw_money()
    elif Op == '4':
        print("YOU EXITED")
        again = input("Do you want to perform another operation? (y/n):").lower()
        if again == 'y':
            print("Thank you")
            print("You will be redirecting to operation page once again..")
            is_running = True
        else:
            is_running = False
    else:
        print("You picked incorrect option..Try again")

print("Thank you for visiting our bank..Please visit again..")
