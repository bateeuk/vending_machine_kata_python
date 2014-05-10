import unittest
from vending_machine import vending_machine 

class AcceptCoinTests(unittest.TestCase):
    
    def test_given_no_coins_entered_when_total_is_displayed_then_insert_coin_is_displayed(self):
        machine = vending_machine.VendingMachine()
        self.assertEquals("INSERT COIN", machine.display())
