import unittest

import circle


class CircleTestCase(unittest.TestCase):
    def test_001_area_integer(self):
        self.assertAlmostEqual(circle.area(2), 12.566370614359172)

    def test_002_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_003_area_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.area(-1)

    def test_004_area_fractional(self):
        self.assertAlmostEqual(circle.area(0.5), 0.7853981633974483)

    def test_005_perimeter_integer(self):
        self.assertAlmostEqual(circle.perimeter(3), 18.84955592153876)

    def test_006_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_007_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-1)

    def test_008_area_scaling(self):
        self.assertAlmostEqual(circle.area(4), 4 * circle.area(2))

    def test_009_area_none(self):
        with self.assertRaises(TypeError):
            circle.area(None)


if __name__ == "__main__":
    unittest.main()
