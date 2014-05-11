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

    def test_given_multiple_coins_when_total_is_displayed_then_total_is_the_sum_of_coins(self):
        self.machine.accept(vending_machine.NICKEL)
        self.machine.accept(vending_machine.QUARTER)
        
        self.assertEquals("0.30", self.machine.display())

    def test_given_an_invalid_coin_when_the_return_slot_is_checked_then_the_invalid_coin_is_in_the_return_slot(self):
        bad_penny = "bad penny"
        self.machine.accept(bad_penny)
        
        self.assertTrue(bad_penny in self.machine.check_return_slot())

    def test_given_multiple_invalid_coins_when_the_return_slot_is_checked_then_the_invalid_coins_are_in_the_return_slot(self):
        bad_penny = "bad penny"
        canadian_quarter = "fake monies"
        self.machine.accept(bad_penny)
        self.machine.accept(canadian_quarter)
        
        self.assertTrue(set([bad_penny, canadian_quarter]).issubset(set(self.machine.check_return_slot())))
