import unittest
from temperature import celsius_to_fahrenheit

class TestTemperature(unittest.TestCase):

    def test_freezing_point(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_boiling_point(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_negative_temperature(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

if __name__ == "__main__":
    unittest.main()