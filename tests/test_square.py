import unittest

import square


class SquareTestCase(unittest.TestCase):
    def test_010_area_integer(self):
        self.assertEqual(square.area(5), 25)

    def test_011_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_012_area_negative_side(self):
        with self.assertRaises(ValueError):
            square.area(-1)

    def test_013_perimeter_integer(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_014_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_015_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            square.perimeter(-1)

    def test_016_perimeter_fractional(self):
        self.assertEqual(square.perimeter(0.5), 2)

    def test_017_perimeter_scaling(self):
        self.assertEqual(square.perimeter(6), 2 * square.perimeter(3))


if __name__ == "__main__":
    unittest.main()
