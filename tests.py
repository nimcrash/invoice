import unittest
from roundcent import *

class TestRoundCent(unittest.TestCase):

    def test_to_nearest(self):
        
        self.assertEqual(to_nearest(520.00 * 1.07), 556.40)
        self.assertEqual(to_nearest(294.04 * 1.07), 314.62)
        self.assertEqual(to_nearest(1829), 1829.00)

    def test_to_nearest_even(self):
      
        self.assertEqual(to_nearest_even(520.00 * 1.07 + 520.00 * 0.16 +
            1983.37 * 0.16 + 1983.37), 2940.30)
        self.assertEqual(to_nearest_even(294.04 * 1.07 + 294.04 * 0.11), 346.96)
        self.assertEqual(to_nearest_even(19385.38 * 1.16 + 1829 * 1.16), 24608.68)

if __name__ == '__main__':
    unittest.main()