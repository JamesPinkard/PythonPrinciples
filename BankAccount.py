class BankAccount:
    
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.currentBalance = initial_balance
        self.fees = 0
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.currentBalance += amount
        
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.currentBalance -= amount
        if self.currentBalance < 0:
            self.currentBalance -= 5
            self.fees += 5
        
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.currentBalance
        
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fees