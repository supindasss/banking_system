class BankAccount:

    def __init__(self,owner_name,starting_balance):

        self.name=owner_name

        self.__balance=starting_balance

    def deposit(self,amount):

        if amount<0:

            print("error")
        else:
            self.__balance+=amount
            
            print(f"deposited :{amount} current balance:{self.__balance}")    

    def withdrawal(self,amount):

        if amount>self.__balance:

            print("unsufficient balance")

        else:

            self.__balance-=amount

            print(f"withdrew:{amount} balance:{self.__balance}")        
class Bank:
    def __init__(self):
        self.accounts={}

    def add_account(self,acc_number,account_obj):

        self.accounts[acc_number]=account_obj 

        print(f"account {acc_number} added to the bank system")

my_bank=Bank()

supin_acc=BankAccount("Supindas",1000)

my_bank.add_account('999****6266',supin_acc)

my_bank.accounts['999****6266'].deposit(1000)