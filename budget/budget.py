# budget.py

class Category:
    """
    e.g) food = Category("Food")    
    """

    def __init__(self, nm):
        # instance variables 
        self.name = nm
        self.ledger = list()
    
    def deposit(self, amount, description=""):
        """
        append {"amount": amount, "description": description} to ledge
        """
        dt = dict()
        dt["amount"] = amount
        dt["description"] = description
        self.ledger.append(dt)

    def withdraw(self, amount, description=""):
        """
        same as deposit, but amount should be negative number
        """
        dt = dict()
        dt["amount"] = -amount
        dt["description"] = description
        fund = self.get_balance()
        if fund - amount > 0: 
            self.ledger.append(dt)
            return True
        return False

    def get_balance(self):
        balance = sum( [ dt["amount"] for dt in self.ledger ] )
        return balance

    def transfer(self, amount, category):
        """
        take amount and category object
        """
        toname = category.name
        frmname = self.name

        dtfrm = dict()
        dtfrm["amount"] = -amount
        dtfrm["description"] = f"Transfer to {toname}"

        dtto = dict()
        dtto["amount"] = amount
        dtto["description"] = f"Transfer from {frmname}"
        
        fund = self.get_balance()

        if fund - amount > 0: 
            self.ledger.append(dtfrm)
            category.ledger.append(dtto)
            return True
        return False        

    def check_funds(self, amount):
        pass


def create_spend_chart(categories):
    pass