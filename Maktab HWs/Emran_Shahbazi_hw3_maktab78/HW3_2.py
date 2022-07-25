class BankAccount:
    
    _min_balance = 0
    
    def __init__(self , account_owner_name , balance , minimum_balance):
        
        self.account_owner_name = account_owner_name
        self.balance = balance
        self.__clas__._minimum_balance = minimum_balance
        

    def deposit(self  , amount):
        
        self.b += amount
        
    def withdraw(self , amount):
        
        self.b -= amount
        
    def transfer(self , amount , transfer_bank_account):
        
        if self.balance - amount < self.__class__._minimum_balance:
            return('This transaction is not possible !!')
        
        else:
            self.balance -= amount
            transfer_bank_account.balance += amount
            return ('Transaction completed')