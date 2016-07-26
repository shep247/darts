from dart_throw import DartThrow, get_throw
from round import Round


class Player:
    score = 0
    darts_thrown = 0
    marks = 0

    @property
    def mpr(self):
        return self.darts_thrown/self.marks


class Game:
    def __init__(self, rounds, num_of_players):
        self.rounds = rounds
        self.players = {}
        self.current_round = 0
        self.game_in_progress = True
        for _ in xrange(num_of_players):
            self.players[_] = Player()

    def play(self):
        for _ in xrange(1, self.rounds + 1):
            self.current_round += 1
            self.print_score()
            for pKey, pVal in self.players.iteritems():
                start_msg = "Player {p}'s turn. Starting score = {s}"
                print start_msg.format(p=pKey, s=pVal.score)
                rnd = Round()
                dart = get_throw(1)
                rnd.dart1(DartThrow(dart))
                dart = get_throw(2)
                rnd.dart2_and_3(DartThrow(dart))
                dart = get_throw(3)
                rnd.dart2_and_3(DartThrow(dart))

                pVal.score += rnd.total
        self.game_in_progress = False

    def print_score(self):
        score = [(x+1, y.score) for x, y in self.players.iteritems()]
        print "Round ", 'FINAL' if not self.game_in_progress else self.current_round
        for p, s in score:
            print "  Player {p}: {s}".format(p=p, s=s)
