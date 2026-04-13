#Python slot machine program
import random,time
def spin_row():
    symbols = ['🍒', '🍉' ,'🍋' ,'🔔' ,'⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("-------------")
    print(" | ".join(row) )
    print("-------------")

def get_payout(row , bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet *10
        elif row[0] == '⭐':
            return bet * 20
    return 0
        

def main():
    print("-----------------------------------------------")
    print("WELCOME TO AKHIL'S SLOT MACHINE......🤑🤑🤑🤑🤑")
    print(" SLOT MACHINE SYMBOLS ARE:  🍒  🍉  🍋  🔔  ⭐ ")
    print("-----------------------------------------------")
    balance = int(input("Load your current amount into the machine: "))
    while balance>0:
        print(f"Your current balance is : {balance}/- ")
        bet = int(input("Enter the bet amount you want to play with: "))
        if bet > balance:
            print("You have in sufficient balance to play with.")
            continue
        elif bet<=0:
            print("The bet amount should be greater than 0.")
            continue
        balance -= bet
        print(f"Your balance after placing your bet : {balance}/-")
        print("Spinning.......😵‍💫")
        time.sleep(1)
        row = spin_row()
        print_row(row)
        payout = get_payout(row,bet)
        if payout > 0:
            print(f"Congratulations.....You won {payout}/-")
            print(f"Your balance after adding winning amount is {balance}/-")
        else:
            print("You lost..Better luck next time...")

        balance += payout 

        play_again = input("Do you want to play again? (Y/N):").upper()
        if play_again != 'Y':
            print("Thanks for playing our game...🫡 😊")
            break


    print("-----------")
    print(" GAME OVER ")
    print("-----------")
    print(f"YOUR TOTAL EARNINGS AFTER THE GAME WAS {balance}/- ")

if __name__ == '__main__':
    main()