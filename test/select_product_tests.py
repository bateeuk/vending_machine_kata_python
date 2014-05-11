import unittest
from vending_machine import vending_machine

class SelectProductTests(unittest.TestCase):

  def setUp(self):
    self.machine = vending_machine.VendingMachine()
  
  def test_given_no_money_accepted_when_candy_selected_then_PRICE_and_amount_is_displayed(self):
    self.machine.select_product(vending_machine.CANDY)

    self.assertEqual("PRICE 0.65", self.machine.display())

  def test_given_no_money_accepted_when_chips_selected_then_PRICE_and_amount_is_displayed(self):
    self.machine.select_product(vending_machine.CHIPS)

    self.assertEqual("PRICE 0.50", self.machine.display())

  def test_given_no_money_accepted_when_cola_selected_then_PRICE_and_amount_is_displayed(self):
    self.machine.select_product(vending_machine.COLA)

    self.assertEquals("PRICE 1.00", self.machine.display())

  def test_given_no_money_accepted_and_product_selected_when_display_called_twice_then_second_display_shows_INSERT_COINS(self):
    self.machine.select_product(vending_machine.COLA)
    self.machine.display()

    self.assertEquals("INSERT COIN", self.machine.display())

  def test_given_money_accepted_and_product_selected_when_display_called_twice_then_second_display_shows_PRICE_and_amount(self):
    self.machine.accept(vending_machine.QUARTER)
    self.machine.select_product(vending_machine.COLA)
    self.machine.display()

    self.assertEquals("0.25", self.machine.display())

  def test_given_enough_money_accepted_when_product_selected_then_display_shows_THANK_YOU(self):
    self.machine.accept(vending_machine.QUARTER)
    self.machine.accept(vending_machine.QUARTER)
    self.machine.select_product(vending_machine.CHIPS)
    
    self.assertEquals("THANK YOU", self.machine.display())
