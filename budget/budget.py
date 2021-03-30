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

        if self.check_funds(amount):
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
            
        if self.check_funds(amount): 
            self.ledger.append(dtfrm)
            category.ledger.append(dtto)
            return True
        return False        

    def check_funds(self, amount):
        balance = self.get_balance()
        return balance - amount >= 0

    def __str__(self):
        result = ''
        result += self.name.center(30, "*") + "\n"
        total = self.get_balance()
        for dt in self.ledger:
            description = dt["description"][:23]
            amount = dt["amount"]
            result += '{:<23} {:.2f}\n'.format(description, amount)
        result += 'Total: {:.2f}'.format(total)
        return result


def create_spend_chart(categories):
    import itertools
    import math
    result = 'Percentage spent by category\n'
    names = [ category.name for category in categories ]
    lng = len(names)
    amounts = [ -dt["amount"] for category in categories for dt in category.ledger if dt["amount"] < 0] 
    sm = sum(amounts)
    
    percents = [ math.floor( amt/sm * 10) * 10  for amt in amounts ]
    
    print( percents )
    
    
    for i in range(101)[::-10]:
        result += '{:>3}|'.format(i)    
        result += '\n'

    result += '{:<4}-'.format('') + '---' * lng + '\n'
    for tp in itertools.zip_longest(*names, fillvalue=' '):
        result += ' ' * 5
        for char in tp:
            result += char + '  '
        result += '\n'
    return result
