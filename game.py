from round import Round
import re


def parse_dart_input(dart):
    if not dart:
        return False
    elif dart.upper() == 'M':
        return dart.upper()
    elif re.search('^\d{1,2}$', dart) is not None:
        # only a number.  assume single
        if (0 < int(dart) < 21) or int(dart) == 25:
            return 'S' + dart
    elif re.search('^[STDstd]\d{1,2}$', dart) is not None:
        # letter followed by a number
        if (0 < int(dart[1:]) < 21) or int(dart[1:]) == 25:
            return dart.upper()
    return False


def get_throw(dart_num):
    enter_dart_msg = "  Dart {d} score: "
    dart = ""
    while not dart:
        d = raw_input(enter_dart_msg.format(d=dart_num))
        dart = parse_dart_input(d)
        if not dart:
            print "  Invalid Input.  Try Again"
    return dart

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
        score = [(x, y.score) for x, y in self.players.iteritems()]
        print "Round ", 'FINAL' if not self.game_in_progress else self.current_round
        for player, score in score:
            print "  Player {p}: {s}".format(p=player, s=score)


class DartThrow:
    def __init__(self, dart):
        self.missed = False
        if dart.upper() == 'M':
            self.missed = True
            self.multiplier = 'S'
            self.bed = 0
        else:
            self.multiplier = dart[:1].upper()
            self.bed = int(dart[1:])

    @property
    def score(self):
        return {'S': 1, 'D': 2, 'T': 3}[self.multiplier] * self.bed
