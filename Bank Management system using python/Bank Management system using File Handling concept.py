import pathlib as p
import time as t 


name = input("Please Enter Your name: ")
an = input("Enter your Account Number: ")


 

while len(an) != 6 or not an.isdigit():
    print("Enter the valid 6 digit account number")
    an = input("Enter your Account Number: ")
 
acc = "SBI" + an    

folder = p.Path(acc)



balance_history = folder / f"balance_history_of_{acc}.txt"
transaction_history = folder / f"transaction_history_of_{acc}.txt"

current_time = t.localtime()
formatted_time = t.strftime("%d-%m-%Y , %H:%M:%S",current_time)



class BankAccount:
    def __init__(self,bal,amt):
        self.bal = bal
        self.amt = amt
    def withdraw(self):
        if self.amt > self.bal:
            print(f"Your Account Balance is {self.bal} so you cannot withdraw {self.amt}")
        else :
            
            self.bal = self.bal - self.amt
            
            f = open(balance_history,"a",encoding="utf-8")
            f.write(f"Available balance on {formatted_time} : {self.bal}\n")
            f.close()

            f = open(transaction_history,"a", encoding="utf-8")
            f.write(f"🔴 {self.amt} withdrawn on {formatted_time}\n")
            f.close()
            print(f"Amount {self.amt} Withdrawn")

    def deposit(self):

        self.bal = self.bal + self.amt

        f = open(balance_history,"a", encoding="utf-8")
        f.write(f"Available balance on {formatted_time} : {self.bal}\n")
        f.close()

        f = open(transaction_history,"a", encoding="utf-8")
        f.write(f"🟢 {self.amt} deposited on {formatted_time}\n")
        f.close()
        print(f"Amount {self.amt} Deposited")

def get_last_balance():
    if balance_history.exists():
        with open(balance_history,"r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1].strip()
                try:
                    return int(last_line.split(":")[-1].strip())
                except ValueError:
                    return 0 
                    
    return 0

if not folder.exists():
    print("Account Created")
    folder.mkdir()
    balance = 0
else: 
    balance = get_last_balance()
       

print("MENU")
print("Enter the desired Operation: ")
print("1. Deposit")
print("2. Withdraw")
print("3. Check balance")
print("4. Check Transaction History")

choice = int(input("Enter your choice: "))



match choice:
    case 1:
        
        amount = int(input("Enter the amount to be deposited: "))
        ba = BankAccount(balance,amount)
        ba.deposit()
    case 2: 
        
        amount = int(input("Enter the amount to be withdrawn: "))
        ba = BankAccount(balance,amount)
        ba.withdraw()
    case 3:

        print("Your Available balance is:  ")
        print("Account Balance: ",get_last_balance())
        
    case 4:

        print("your transaction history: ")
        f = open(transaction_history,"r")
        t_history = f.read()
        print(t_history)
    



