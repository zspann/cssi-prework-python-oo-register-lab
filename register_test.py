import sys
import unittest

from register import CashRegister

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.cash_register=CashRegister()
        self.cash_register_with_discount=CashRegister(20)

    def test_init(self):
        """It sets an instance variable total on initialization to zero"""
        self.assertEqual(self.cash_register.total, 0)
    def test_init_param(self):
        """It optionally takes an employee discount on initialization"""
        self.assertEqual(self.cash_register_with_discount.discount,20)

    def test_add_item(self):
        """It accepts a title and a price and increases the total"""
        self.cash_register.add_item("eggs", 0.98)
        self.assertEqual(self.cash_register.total,.98)
        self.assertEqual(self.cash_register.items,["eggs"])

    def test_add_item_quant(self):
        """It accepts an accepts an optional quantity"""
        self.cash_register.add_item("magazine", 5.00, 3)
        self.assertEqual(self.cash_register.total,15)
        self.assertEqual(self.cash_register.items,["magazine", "magazine","magazine"])

    def test_add_multiple_items(self):
        """It stores multiple items and correctly calculates the total"""
        self.cash_register.add_item("Lucky Charms", 4.5)
        self.assertEqual(self.cash_register.total,4.5)
        self.cash_register.add_item("Ritz Crackers", 5.0)
        self.assertEqual(self.cash_register.total,9.5)
        self.cash_register.add_item("Reese's Peanut Butter Cups", 2.50, 2)
        self.assertEqual(self.cash_register.total,14.5)
        self.assertEqual(self.cash_register.items,["Lucky Charms", "Ritz Crackers", "Reese's Peanut Butter Cups","Reese's Peanut Butter Cups"])

    def test_discount(self):
        """It applies the discount to the total price"""
        self.cash_register_with_discount.add_item("chicken", 10)
        self.cash_register_with_discount.apply_discount()
        self.assertEqual(self.cash_register_with_discount.total,8)

    def test_discount_message(self):
        """It returns success message with updated total"""
        self.cash_register_with_discount.add_item("chicken", 10)
        self.assertEqual(self.cash_register_with_discount.apply_discount(),"After the discount, the total comes to $8.00.")

    def test_no_discount(self):
         """It returns no discount message"""
         self.cash_register.add_item("chicken", 10)
         self.assertEqual(self.cash_register.apply_discount(),"There is no discount to apply.")

    def test_void_discount(self):
         """It removes the most recently added item"""
         self.cash_register.add_item("chicken", 10)
         self.cash_register.add_item("tomato", 1.76)
         self.assertEqual(self.cash_register.items,["chicken", "tomato"])
         self.cash_register.void_last_transaction()
         self.assertEqual(self.cash_register.total,10)
         self.assertEqual(self.cash_register.items,["chicken"])

    def test_void_discount_multiple(self):
         """It removes the most recently added items"""
         self.cash_register.add_item("chicken", 10)
         self.cash_register.add_item("tomato", 1.76, 2)
         self.assertEqual(self.cash_register.items,["chicken", "tomato", "tomato"])
         self.cash_register.void_last_transaction()
         self.assertEqual(self.cash_register.total,10)
         self.assertEqual(self.cash_register.items,["chicken"])

if __name__ == '__main__':
    unittest.main()
