# homework 11-1
import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """测试city_functions.py"""

    def test_city_country(self):
        """能够正确地处理像Santiago, Chile这样的字符串吗？"""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')
        