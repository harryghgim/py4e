# budget app
# question: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app
# answer: https://replit.com/@harryghgim/boilerplate-budget-app#budget.py

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
            result += '{:<23}{:>7.2f}\n'.format(description, amount)
        result += 'Total: {:.2f}'.format(total)
        return result

def create_spend_chart(categories):
    import itertools
    import math
    result = 'Percentage spent by category\n'

    amounts = list() # list of integers
    for category in categories:
        percent = 0
        for dt in category.ledger:
            amt = dt["amount"] # withdraw, negative
            if amt < 0: percent += -amt
        amounts.append(percent)

    sm = sum(amounts)

    percents = list() # list of strings
    for amt in amounts:
        nb = math.floor( amt/sm * 10 ) + 1
        percent = ' ' * (11 - nb) + 'o' * nb
        percents.append(percent)
    
    labels = range(101)[::-10]
    chartpls = zip( *percents )
        
    for i, tp in zip( labels, chartpls ):
        result += f'{i:>3}| '
        for char in tp:            
            result += char + '  '
        result += '\n'

    names = [ category.name for category in categories ]
    lng = len(names)

    result += '{:<4}-{}\n'.format('', '---' * lng)
    for tp in itertools.zip_longest(*names, fillvalue=' '):
        result += ' ' * 5
        for char in tp:
            result += char + '  '
        result += '\n'
    result = result.rstrip('\n')
    return result
