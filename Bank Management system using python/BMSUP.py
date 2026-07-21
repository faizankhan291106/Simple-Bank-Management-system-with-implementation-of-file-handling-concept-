name = input("Enter your Name: ")
acc_no = int(input("Enter your Account Number: "))
bal = int(input("Enter your Account balance: "))
print("Your account Balence is: ", bal)

print("Enter the operation which you want to perform: ")
print("1. Deposit")
print("2. Withdraw")
choice = input("Enter your choice: ")

class Account:
    def __init__(self,dep,wit):
        self.dep = dep
        self.wit = wit 
    def deposit(self,bal):
        print(bal)
        return f"Your Total balance after adding {self.dep} to {self.wit} is: {(self.dep + self.wit)}"
    def withdraw(self,bal):
        if self.wit > self.dep: 
            print( f"Balence is too low so you can not withdraw {self.wit} from {self.dep}")
        else:
            return f"After Wthdrawing {self.wit} form {self.dep} is {(self.dep - self.wit)}"


if choice == "Deposit":
    amt = int(input("Enter the amount you want to deposit: "))
    a = Account(amt,bal)
    print(a.deposit(amt))
elif choice == "Withdraw":
    wid = int(input("Enter the amount you want to withdraw: "))
    a = Account(bal,wid)
    print(a.withdraw(wid))
else: 
    print("Invalid choice!!")
    
    
