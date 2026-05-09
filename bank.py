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

My_account=BankAccount("supindas",1000) 



My_account.deposit(-10000)
My_account.withdrawal(5000)