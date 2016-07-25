import unittest
from firstImpressions import Round, DartThrow
from ddt import ddt, data, unpack

@ddt
class TestFirstDart(unittest.TestCase):
    def setUp(self):
        self.round = Round()

    @data(('S10', 10), # test single
          ('D10', 20), # test double
          ('T10', 30), # test triple
          ('s10', 10)  # test lower case
          )
    @unpack
    def test_hit(self, throw, total):
        # 1st dart hit => set the marker,
        #                 add the score to total,
        #                 missed_first remains unchanged
        dart_throw = DartThrow(throw)
        self.round.first_dart(dart_throw)
        self.assertEqual(total, self.round.total)
        self.assertFalse(self.round.missed_first)
        self.assertEqual(int(throw[1:]), self.round.marker)

    def test_miss(self):
        # 1st dart missed => don't set the marker,
        #                    don't add the score to total,
        #                    missed_first is set to true
        dart_throw = DartThrow('M')
        self.round.first_dart(dart_throw)
        self.assertEqual(0, self.round.total)
        self.assertTrue(self.round.missed_first)
        self.assertEqual(-1, self.round.marker)


@ddt
class TestSecondDart(unittest.TestCase):
    def setUp(self):
        self.round = Round()

    @data(('S10', 20),
          ('s10', 20),
          ('D10', 30),
          ('T10', 40))
    @unpack
    def test_first_dart_hit_second_hit_marker(self, throw, total):
        self.round.missed_first = False
        self.round.marker = 10
        self.round.total = 10
        self.round.second_dart(DartThrow(throw))
        self.assertEqual(total, self.round.total)

    def test_first_dart_hit_second_miss_marker(self):
        self.round.missed_first = False
        self.round.marker = 10
        self.round.total = 10
        self.round.second_dart(DartThrow('S5'))
        self.assertEqual(5, self.round.total)

    def test_first_dart_hit_second_miss_board(self):
        self.round.missed_first = False
        self.round.marker = 10
        self.round.total = 10
        self.round.second_dart(DartThrow('M'))
        self.assertEqual(10, self.round.total)
        self.assertTrue(self.round.missed_second)
        self.assertEqual(10, self.round.marker)

    def test_first_dart_miss_second_hit_board(self):
        self.round.missed_first = True
        self.round.second_dart(DartThrow('S10'))
        self.assertEqual(-10, self.round.total)

    def test_first_dart_miss_second_miss_board(self):
        self.round.missed_first = True
        self.round.second_dart(DartThrow('M'))
        self.assertEqual(0, self.round.total)
        self.assertTrue(self.round.missed_second)

@ddt
class TestThirdDart(unittest.TestCase):
    def setUp(self):
        self.round = Round()

    @data(('S10', 30), # hit marker Single
          ('s10', 30), # hit marker Single (testing case sensitive)
          ('D10', 40), # hit marker Double
          ('T10', 50), # hit marker Triple
          ('S5', 15), # miss marker Single
          ('M', -30) # miss board
          )
    @unpack
    def test_hit_hit_hit_marker(self, throw, total):
        self.round.total = 20
        self.round.marker = 10
        self.round.third_dart(DartThrow(throw))
        self.assertEqual(total, self.round.total)

    @data(('S20', 20), # hit marker Single
          ('S5', 10), # miss marker 20 - (2*5) = 10
          ('M', -130), # miss board 20 - 150 = -130
          )
    @unpack
    def test_hit_miss_hit_marker(self, throw, total):
        self.round.total = 20
        self.round.marker = 20
        self.round.missed_second = True
        self.round.third_dart(DartThrow(throw))
        self.assertEqual(total, self.round.total)

    @data(('S5', 15), # hit board, subtract value
          ('M', -30), # missed board, subtract 50
          )
    @unpack
    def test_miss_hit_hit_board(self, throw, total):
        self.round.total = 20
        self.round.marker = -1
        self.round.missed_first = True
        self.round.third_dart(DartThrow(throw))
        self.assertEqual(total, self.round.total)

    @data(('S5', -15), # hit board: subtract 3 * value
          ('M', -200) # miss board: subtract 200
          )
    @unpack
    def test_miss_miss_hit_board(self, throw, total):
        self.round.total = 0
        self.round.marker = -1
        self.round.missed_first = True
        self.round.missed_second = True
        self.round.third_dart(DartThrow(throw))
        self.assertEqual(total, self.round.total)

if __name__ == '__main__':
    unittest.main()
