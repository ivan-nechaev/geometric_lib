import unittest

import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_018_area_integer(self):
        self.assertEqual(rectangle.area(3, 5), 15)

    def test_019_area_zero_side(self):
        self.assertEqual(rectangle.area(0, 5), 0)

    def test_020_area_negative_side(self):
        with self.assertRaises(ValueError):
            rectangle.area(-1, 5)

    def test_021_area_fractional(self):
        self.assertAlmostEqual(rectangle.area(2.5, 1.5), 3.75)

    def test_022_perimeter_integer(self):
        self.assertEqual(rectangle.perimeter(3, 5), 16)

    def test_023_perimeter_zero_side(self):
        self.assertEqual(rectangle.perimeter(0, 5), 10)

    def test_024_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(3, -1)

    def test_025_area_side_order(self):
        self.assertEqual(rectangle.area(3, 5), rectangle.area(5, 3))

    def test_026_perimeter_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(3, '5')


if __name__ == "__main__":
    unittest.main()
