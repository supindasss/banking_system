class BankAccount:

    def __init__(self,owner_name,starting_balance):

        self.name=owner_name

        self.__balance=starting_balance

    def deposit(self,amount):

        if amount<0:

            print("error")

        else:

            self.__balance+=amount

            print(f"Deposit:{amount} balance:{self.__balance}")             
    def withdrawal(self,amount):

        if amount>self.__balance:

            print(f"you have only {self.__balance}")

        else:

            self.__balance-=amount

            print(f"withdwal:{amount} balance: {self.__balance}")    

class Bank():

    def __init__(self):

        self.accounts={}

    def add_account(self,account_num,account_obj):    
        
        self.accounts[account_num]=account_obj

        print(f"account {account_num} added to the bank system")

my_account=Bank()

supin_acc=BankAccount("supindas",1000)

my_account.add_account('9996266',supin_acc)


