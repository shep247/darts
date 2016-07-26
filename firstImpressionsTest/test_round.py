import unittest
from dart_throw import DartThrow
from round import Round
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
        self.round.dart1(dart_throw)
        self.assertEqual(total, self.round.total)
        self.assertFalse(self.round.missed_first)
        self.assertEqual(int(throw[1:]), self.round.marker)

    def test_miss(self):
        # 1st dart missed => don't set the marker,
        #                    don't add the score to total,
        #                    missed_first is set to true
        dart_throw = DartThrow('M')
        self.round.dart1(dart_throw)
        self.assertEqual(-50, self.round.total)
        self.assertTrue(self.round.missed_first)
        self.assertEqual(-1, self.round.marker)


@ddt
class TestSecondDart(unittest.TestCase):
    def setUp(self):
        self.round = Round()

    @data(('S10', 20),
          ('s10', 20),
          ('D10', 30),
          ('T10', 40),
          ('M', -40),
          ('S5', 5))
    @unpack
    def test_first_dart_hit(self, throw, total):
        self.round.missed_first = False
        self.round.marker = 10
        self.round.total = 10
        self.round.dart2_and_3(DartThrow(throw))
        self.assertEqual(total, self.round.total)

    @data(('S10', 20),
          ('M', -50))
    @unpack
    def test_first_dart_miss(self, throw, total):
        self.round.missed_first = True
        self.round.total = 0
        self.round.dart2_and_3(DartThrow('S10'))
        self.assertEqual(-10, self.round.total)


if __name__ == '__main__':
    unittest.main()
