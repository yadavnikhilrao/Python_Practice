class Atm:
    
# __init__ (Its a Constructor - Constractor is a special function/method that can excute the code automatically)
    
    def __init__(self):
        
        self.pin = ''     # data1
        self.balance = 0  # data2
        
        self.menu()   # calling the function
        
    def menu(self):
        user_input = int(input('''
        Hello, how would you like to proceed?
        - Enter 1 to create pin
        - Enter 2 to deposit
        - Enter 3 to withdraw
        - Enter 4 to check balance
        - Enter 5 to exit
        '''))
        
        if user_input==1:
            self.create_pin()
        elif user_input==2:
            self.deposit()
        elif user_input==3:
            self.withdraw()
        elif user_input==4:
            self.check_balance()
        else:
            print("Bye")
            
    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin set successfully")
        
    def deposit(self):
        temp = input("Enter your pin")
        if temp==self.pin:
            amount = int(input("Enter the amount: "))
            self.balance = self.balance+amount
        else:
            print("Invalid Pin")
            
    def withdraw(self):
        temp = input("Enter your pin")
        if temp==self.pin:
            amount = int(input("Enter the amount: "))
            if amount<self.balance:
                self.balance = self.balance-amount
            else:
                print("Insufficient funds")
        else:
            print("Invalid Pin")
            
        
    def check_balance(self):
        temp = input("Enter your pin")
        if temp==self.pin:
            print("Your amount is: ", self.balance)
        else:
            print("Invalid Pin")
