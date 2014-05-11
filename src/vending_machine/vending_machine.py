
''' Valid coins '''
NICKEL = "nickel"
DIME = "dime"
QUARTER = "quarter"

''' Valid products '''
CANDY = "candy"

class VendingMachine:

  def __init__(self):
    self.valid_coins = {NICKEL : .05, DIME : 0.1, QUARTER : 0.25}
    self.coins = []
    self.invalid_coins = []
    self.product_selected = False
  
  def accept(self, coin):
    if (self.valid_coins.has_key(coin)):
      self.coins.append(self.valid_coins[coin])
    else:
      self.invalid_coins.append(coin)

  def display(self):
    total_coins = sum(self.coins)
    
    if self.product_selected:
        return self.display_with_product_selected(total_coins)
    else:
        return self.display_without_product_selected(total_coins)
    
  def display_without_product_selected(self, total):
    if (total > 0.0):
      return "%s" % "{:.2f}".format(total)

    return "INSERT COIN"

  def display_with_product_selected(self, total):
      return "PRICE 0.65"

  def check_return_slot(self):
    return self.invalid_coins

  def clear_return_slot(self):
    self.invalid_coins = []

  def select_product(self, product):
      self.product_selected = True
