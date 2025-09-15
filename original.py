fare_per_ride = 5
fare_per_ride2 = 5

weekly_pass = 100
monthly_pass = 300


def user_balance(balance):
    print("-----------------Welcome To NYC Metro Service---------------------------")
    print(f'Your Current Balance is : {balance}')

def top_up(balance):
    amount = int(input("please enter the amount you want to top-up)"))
    while True:
        if amount <= 0:
            print("Please enter a valid amount to top-up")
            amount = int(input("please enter the amount you want to top-up)"))
        else:
            balance += amount
            print(f'You have successfully topped up your balance by ${amount}')
            break
    user_balance(balance)
    print("You can now buy a pass or a ticket for your journey")
    print("You can also buy a weekly or monthly pass")
    print(f'Your updated balance is : {balance}')
    return balance

def week_month(balance):
    want = int(input("\n1.Monthly    \n2. weekly"))
    while True:
        if want == 1:
            if balance < monthly_pass:
                print(f"Your balance is insufficient to buy a monthly pass. Please top-up your balance.")
                break
            elif balance >= monthly_pass:
                balance-= monthly_pass
                print(f"your monthly pass is activated")
        elif want == 2:
            if balance < weekly_pass:
                print(f"Your balance is insufficient to buy a weekly pass. Please top-up your balance.")
                break
            elif balance >= weekly_pass:
                balance-= weekly_pass
                print(f"your weekly pass is activated")
        print(f'Your updated balance is : {balance}')
        return balance

def from_to_station(balance):                 
    print("Selct a journey to know more about their details\n1. From A to B   \n2. From B to C" )
    journey_input = int(input("Please select the option: (1,2)"))
    
    while True:
        if journey_input == 1:
            print(f"\nJourney from A to B costs ${fare_per_ride} per ride")
            print (f"Enter BUY to buy a ticket for this journey Or Cancel to exit")
            buy_input = input("Please enter 'Buy' or 'cancel' ").strip().upper()
  
            if buy_input == "BUY":
                    while True:
                        if balance < fare_per_ride:
                            print(f"\nYour balance is insufficient to buy a ticket for this journey. Please top-up your balance.")
                            break
                        elif balance >= fare_per_ride:
                            print(f"\nTicket purchased successfully for journey from A to B. Your balance is now reduced by ${fare_per_ride}.")
                            balance-= fare_per_ride
                            print(f'\nYour updated balance is : {balance}')
                            return balance 
  
            elif buy_input =="CANCEL":
                break
                          
        elif journey_input == 2:
            print("\nJourney from B to C")
            print (f"\nEnter BUY to buy a ticket for this journey")
            buy_input = input("Please enter 'Buy' or 'cancel' ").strip().upper()
            if buy_input == "BUY":
                while True:
                        if balance < fare_per_ride:
                            print(f"\nYour balance is insufficient to buy a ticket for this journey. Please top-up your balance.")
                            break
                        elif balance >= fare_per_ride:
                            print(f"\nTicket purchased successfully for journey from A to B. Your balance is now reduced by ${fare_per_ride}.")
                            balance -= fare_per_ride2
                            print(f'\nYour updated balance is : {balance}')
                            return balance
            elif buy_input == 'CANCEL':
                break
           
        
    
    
        


def exit_program():
    print (f"Thank you for using the NYC Metro Service. Have a great day!")
    exit()

def main():
    balance = 0
    while True:
        print("\n1. Balance  \n2. Top up  \n3.Plan your journey   \n4. offer  \n5. exit"  )
        choice =int(input("Please select the option: (1,2,3,4,5)"))
        if choice == 1:
            user_balance(balance)
        if choice == 2:
            balance = top_up(balance)
        
        if choice == 5:
            exit_program()
        
        if choice == 4:
            balance = week_month(balance)
        
        if choice == 3:
            from_to_station(balance)
            
if __name__ == '__main__':
    main()