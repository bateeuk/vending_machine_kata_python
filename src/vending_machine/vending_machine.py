
''' Valid coins '''
NICKEL = "nickel"
DIME = "dime"
QUARTER = "quarter"

''' Valid products '''
CANDY = "candy"
CHIPS = "chips"
COLA = "cola"

class VendingMachine:

  def __init__(self):
    self.valid_coins = {NICKEL : .05, DIME : 0.1, QUARTER : 0.25}
    self.products = {CANDY : 0.65, CHIPS : 0.50, COLA : 1.00}
    self.coins = []
    self.invalid_coins = []
    self.selected_product = None
  
  def accept(self, coin):
    if (self.valid_coins.has_key(coin)):
      self.coins.append(self.valid_coins[coin])
    else:
      self.invalid_coins.append(coin)

  def display(self):
    total_coins = sum(self.coins)
    
    if self.selected_product:
        return self.display_with_selected_product(total_coins)
    else:
        return self.display_without_selected_product(total_coins)
    
  def display_without_selected_product(self, total):
    if (total > 0.0):
      return self.format_amount(total)

    return "INSERT COIN"

  def display_with_selected_product(self, total):
    return "PRICE %s" % self.format_amount(self.products[self.selected_product])

  def format_amount(self, amount):
    return "%s" % "{:.2f}".format(amount)

  def check_return_slot(self):
    return self.invalid_coins

  def clear_return_slot(self):
    self.invalid_coins = []

  def select_product(self, product):
    self.selected_product = product
