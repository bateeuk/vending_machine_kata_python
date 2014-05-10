import unittest
from vending_machine import vending_machine 

class AcceptCoinTests(unittest.TestCase):
    
    def test_when_no_coins_entered_then_insert_coin_is_displayed(self):
        machine = vending_machine.VendingMachine()
        self.assertEquals("INSERT COIN", machine.display())
    
    def test_when_nickel_entered_then_five_cents_is_displayed(self):
        machine = vending_machine.VendingMachine()
        machine.accept(vending_machine.NICKEL)
        self.assertEquals("0.05", machine.display())

    def test_when_dime_entered_then_ten_cents_is_diplayed(self):
        machine = vending_machine.VendingMachine()
        machine.accept(vending_machine.DIME)
        self.assertEquals("0.10", machine.display())

    def test_when_quarter_entered_then_twenty_five_cents_is_displayed(self):
        machine = vending_machine.VendingMachine()
        machine.accept(vending_machine.QUARTER)
        self.assertEquals("0.25", machine.display())

