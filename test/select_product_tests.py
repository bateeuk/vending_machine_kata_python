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
