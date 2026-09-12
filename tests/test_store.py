import unittest

from store import apply_discount, can_checkout, loyalty_discount, shipping_cost


class StoreTests(unittest.TestCase):
    def test_regular_shipping(self):
        self.assertEqual(shipping_cost(500), 99.0)

    def test_negative_subtotal_is_invalid(self):
        with self.assertRaises(ValueError):
            shipping_cost(-1)

    def test_apply_discount(self):
        self.assertEqual(apply_discount(1000, 10), 900.0)

    def test_checkout_with_items(self): #C1
        self.assertTrue(can_checkout(1))

    def test_checkout_with_zero_items(self): #C
        self.assertFalse(can_checkout(0))

    def test_checkout_with_fifty_items(self): #C
        self.assertTrue(can_checkout(50))
    
    def test_checkout_with_more_than_fifty_items(self): #C
        self.assertFalse(can_checkout(51))

    def test_loyalty_starts_at_zero(self):
        self.assertEqual(loyalty_discount(0), 0)
    def test_loyalty_discount_below_500(self):
        self.assertEqual(loyalty_discount(499), 0)

    def test_loyalty_discount_from_500_to_999(self):
        self.assertEqual(loyalty_discount(500), 5)
        self.assertEqual(loyalty_discount(999), 5)

    def test_loyalty_discount_at_1000(self):
        self.assertEqual(loyalty_discount(1000), 10)


if __name__ == "__main__":
    unittest.main()
