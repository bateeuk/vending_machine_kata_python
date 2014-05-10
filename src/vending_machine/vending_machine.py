NICKEL = "nickel"
DIME = "dime"

class VendingMachine:

  def __init__(self):
    self.valid_coins = {NICKEL : .05, DIME : 0.1}
    self.coins = []
  
  def accept(self, coin):
    if (self.valid_coins[coin]):
      self.coins.append(self.valid_coins[coin])

  def display(self):
    total = sum(self.coins)
    if (total > 0.0):
      return "%s" % "{:.2f}".format(total)

    return "INSERT COIN"
