class Category:
  ledger = list()
  name = ""
  balance = 0.0
  
  def __init__(self, budget_category):
    self.name = budget_category
    self.ledger = list()
    self.balance = 0.0

  def __repr__(self):
    title = self.name.center(30, "*") + "\n"
    ledger = ""
    for item in self.ledger:
      description_str = "{:<23}".format(item["description"])
      amount_str = "{:>7.2f}".format(item["amount"])
      ledger += "{}{}\n".format(description_str[:23],amount_str[:7])
    total = "Total: {:.2f}".format(self.balance)
    return title + ledger + total
      
  def deposit (self, amount,description=""):
    self.ledger.append({"amount": amount, "description":description})
    self.balance += amount
  
  def withdraw (self, amount, description = ""):
    if self.balance >= amount:
      self.ledger.append({"amount": -amount, "description":description})
      self.balance -= amount
      return True
    else:
      return False
  
  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    str = "Trasfer to "+category.name
    if self.withdraw(amount, str):
      str = "Transfer from "+self.name
      category.deposit(amount, str)
      return True
    else:
      return False

  def check_funds(self, amount):
    if self.balance >= amount:
      return True
    else:
      return False

  
def create_spend_chart(categories):
  spent_list = list()
  names_length = list()
  names = list()
  
  for category in categories:
    spent = 0
    for item in category.ledger:
      if item["amount"] < 0:
        spent += abs(item["amount"])
    spent_list.append(spent)
    names_length.append(len(category.name))
    names.append(category.name)
    
  total_spent = sum(spent_list)
  spent_percentage = list()
  
  for spent in spent_list:
    percentage = (spent/total_spent) * 100
    spent_percentage.append(percentage)

  print("Percentage spent by category")
  chart = ""
  for percentage in range(100,-1,-10):
    chart += str(percentage).rjust(3) + '|'
    for i in spent_percentage:
      if i >= percentage:
        chart += " o "
      else:
        chart += "   "
    chart += "\n"
  print(chart)
  print("    " + "-" * ((3 * len(categories)) + 1))
  for i in range(max(names_length)):
    line = "     "
    for name in names:
      try:
        line += name[i]
      except:
        line += " "
      line += "  "
    print(line)
    
    