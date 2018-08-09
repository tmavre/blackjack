import unittest
import chips


class TestChips(unittest.TestCase):
    def test_take_bet(self):
        test_chips = chips.Chips()
        self.assertEqual(test_chips.take_bet(200), False)
        self.assertEqual(test_chips.take_bet(50), True)
        self.assertEqual(test_chips.bet, 50)

    def test_win_bet(self):
        pass  # TODO

    def test_lose_bet(self):
        pass  # TODO
