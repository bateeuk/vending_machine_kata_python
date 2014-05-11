NICKEL = "nickel"
DIME = "dime"
QUARTER = "quarter"

class VendingMachine:

  def __init__(self):
    self.valid_coins = {NICKEL : .05, DIME : 0.1, QUARTER : 0.25}
    self.coins = []
    self.invalid_coins = []
  
  def accept(self, coin):
    if (self.valid_coins.has_key(coin)):
      self.coins.append(self.valid_coins[coin])
    else:
      self.invalid_coins.append(coin)

  def display(self):
    total = sum(self.coins)
    if (total > 0.0):
      return "%s" % "{:.2f}".format(total)

    return "INSERT COIN"

  def check_coin_slot(self):
    return self.invalid_coins
