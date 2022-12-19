import unittest
from unittest.mock import patch
from main import *


class TestConverter(unittest.TestCase):
    @patch('main.input')
    def test_amount_check(self, mock_main_input):
        self.assertEqual(100.0, amount_check("100.0"))
        self.assertEqual(100.0, amount_check("100"))
        self.assertEqual(321.123, amount_check("321.123"))
        mock_main_input.return_value = "12.0"
        self.assertEqual(12.0, amount_check("100."))
        mock_main_input.assert_called()
        mock_main_input.return_value = "13.0"
        self.assertEqual(13.0, amount_check("100,0"))
        mock_main_input.return_value = "14.0"
        self.assertEqual(14.0, amount_check(".0"))
        mock_main_input.return_value = "15.0"
        self.assertEqual(15.0, amount_check("abcdef"))

    @patch('main.input')
    def test_currency_check(self, mock_main_input):
        self.assertEqual("BTC", currency_check("b"))
        self.assertEqual("BTC", currency_check("B"))
        self.assertEqual("BTC", currency_check("btc"))
        self.assertEqual("BTC", currency_check("BTC"))
        self.assertEqual("ETH", currency_check("e"))
        self.assertEqual("ETH", currency_check("E"))
        self.assertEqual("ETH", currency_check("eth"))
        self.assertEqual("ETH", currency_check("ETH"))
        mock_main_input.return_value = "b"
        self.assertEqual("BTC", currency_check("BTCETH"))
        mock_main_input.assert_called()
        mock_main_input.return_value = "ETH"
        self.assertEqual("ETH", currency_check("abcdef"))
        mock_main_input.return_value = "btc"
        self.assertEqual("BTC", currency_check("100.0"))

    @patch('main.get_exchange_rate')
    def test_exchange(self, mock_get_exchange_rate):
        mock_get_exchange_rate.return_value = 10.0
        self.assertEqual(100.0, exchange(10.0, "BTC"))
        mock_get_exchange_rate.assert_called()

        mock_get_exchange_rate.return_value = 100.0
        self.assertEqual(7.0, exchange(0.07, "ETH"))


if __name__ == "__main__":
    unittest.main()
