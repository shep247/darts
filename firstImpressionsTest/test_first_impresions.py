import unittest
from firstImpressions import Round


class TestFirstDart(unittest.TestCase):
    def setUp(self):
        self.round = Round()

    def test_first_dart_hit(self):
        # 1st dart hit => set the marker,
        #                 add the score to total,
        #                 missed_first remains unchanged
        self.round.first_dart(10)
        self.assertEqual(10, self.round.total)
        self.assertFalse(self.round.missed_first)
        self.assertEqual(10, self.round.marker)

    def test_first_dart_miss(self):
        # 1st dart missed => don't set the marker,
        #                    don't add the score to total,
        #                    missed_first is set to true
        self.round.first_dart(0)
        self.assertEqual(0, self.round.total)
        self.assertTrue(self.round.missed_first)
        self.assertEqual(-1, self.round.marker)

class TestSecondDart(unittest.TestCase):
    def setUp(self):
        self.round = Round()

    def test_first_dart_hit_second_hit_marker(self):
        self.round.missed_first = False
        self.round.marker = 10
        self.round.total = 10
        self.round.second_dart(10)
        self.assertEqual(20, self.round.total)

    def test_first_dart_hit_second_miss_marker(self):
        self.round.missed_first = False
        self.round.marker = 10
        self.round.total = 10
        self.round.second_dart(5)
        self.assertEqual(5, self.round.total)

    def test_first_dart_hit_second_miss_board(self):
        self.round.missed_first = False
        self.round.marker = 10
        self.round.total = 10
        self.round.second_dart(0)
        self.assertEqual(10, self.round.total)
        self.assertTrue(self.round.missed_second)
        self.assertEqual(10, self.round.marker)

    def test_first_dart_miss_second_hit_board(self):
        self.round.missed_first = True
        self.round.second_dart(10)
        self.assertEqual(-10, self.round.total)

    def test_first_dart_miss_second_miss_board(self):
        self.round.missed_first = True
        self.round.second_dart(0)
        self.assertEqual(0, self.round.total)
        self.assertTrue(self.round.missed_second)

class TestThirdDart(unittest.TestCase):
    def setUp(self):
        self.round = Round()

    def test_hit_hit_hit_marker(self):
        self.round.total = 20
        self.round.marker = 10
        self.round.third_dart(10)
        self.assertEqual(30, self.round.total)

    def test_hit_hit_miss_marker(self):
        self.round.total = 20
        self.round.marker = 10
        self.round.third_dart(5)
        self.assertEqual(15, self.round.total)

    def test_hit_hit_miss_board(self):
        self.round.total = 20
        self.round.marker = 10
        self.round.third_dart(0)
        self.assertEqual(-30, self.round.total)

    def test_hit_miss_hit_marker(self):
        self.round.total = 20
        self.round.marker = 20
        self.round.missed_second = True
        self.round.third_dart(20)
        self.assertEqual(20, self.round.total)

    def test_hit_miss_miss_marker(self):
        self.round.total = 20
        self.round.marker = 20
        self.round.missed_second = True
        self.round.third_dart(5)
        self.assertEqual(20-(2*5), self.round.total)

    def test_hit_miss_miss_board(self):
        self.round.total = 20
        self.round.marker = 20
        self.round.missed_second = True
        self.round.third_dart(0)
        self.assertEqual(20 - 150, self.round.total)

    def test_miss_hit_hit_board(self):
        self.round.total = 20
        self.round.marker = -1
        self.round.missed_first = True
        self.round.third_dart(5)
        self.assertEqual(20 - 5, self.round.total)

    def test_miss_hit_miss_board(self):
        self.round.total = 20
        self.round.marker = -1
        self.round.missed_first = True
        self.round.third_dart(0)
        self.assertEqual(20 - 50, self.round.total)

    def test_miss_miss_hit_board(self):
        self.round.total = 0
        self.round.marker = -1
        self.round.missed_first = True
        self.round.missed_second = True
        self.round.third_dart(5)
        self.assertEqual(-3*5, self.round.total)

    def test_miss_miss_miss_board(self):
        self.round.total = 0
        self.round.marker = -1
        self.round.missed_first = True
        self.round.missed_second = True
        self.round.third_dart(0)
        self.assertEqual(-200, self.round.total)


if __name__ == '__main__':
    unittest.main()
