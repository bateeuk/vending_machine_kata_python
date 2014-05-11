import unittest
from vending_machine import vending_machine 

class AcceptCoinTests(unittest.TestCase):

    def setUp(self):
        self.machine = vending_machine.VendingMachine()
    
    def test_when_no_coins_entered_then_insert_coin_is_displayed(self):
        self.assertEquals("INSERT COIN", self.machine.display())
    
    def test_when_nickel_entered_then_five_cents_is_displayed(self):
        self.machine.accept(vending_machine.NICKEL)
        self.assertEquals("0.05", self.machine.display())

    def test_when_dime_entered_then_ten_cents_is_diplayed(self):
        self.machine.accept(vending_machine.DIME)
        self.assertEquals("0.10", self.machine.display())

    def test_when_quarter_entered_then_twenty_five_cents_is_displayed(self):
        self.machine.accept(vending_machine.QUARTER)
        self.assertEquals("0.25", self.machine.display())

    def test_given_only_an_invalid_coin_when_total_is_displayed_then_invalid_message_is_shown(self):
        self.machine.accept("bad penny")
        self.assertEquals("INSERT COIN", self.machine.display())

    def test_given_valid_coin_when_invalid_coin_is_accepted_then_total_is_not_updated(self):
        self.machine.accept(vending_machine.NICKEL)
        self.machine.accept("bad penny")
        self.assertEquals("0.05", self.machine.display())
