import unittest

import triangle


class TriangleTestCase(unittest.TestCase):
    def test_027_area_integer(self):
        self.assertEqual(triangle.area(6, 4), 12)

    def test_028_area_zero_base(self):
        self.assertEqual(triangle.area(0, 5), 0)

    def test_029_area_negative_height(self):
        with self.assertRaises(ValueError):
            triangle.area(6, -1)

    def test_030_area_fractional(self):
        self.assertAlmostEqual(triangle.area(2.5, 1.2), 1.5)

    def test_031_perimeter_integer(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_032_perimeter_zero_sides(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_033_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, 4, -1)

    def test_034_perimeter_side_order(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), triangle.perimeter(5, 3, 4))

    def test_035_perimeter_invalid_sides(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 2, 4)


if __name__ == "__main__":
    unittest.main()
