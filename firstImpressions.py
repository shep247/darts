import re

from round import Round


class Player:
    score = 0
    darts_thrown = 0
    marks = 0

    @property
    def mpr(self):
        return self.darts_thrown/self.marks


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


def print_score(round):
    score = [(x, y.score) for x, y in players.iteritems()]
    print "Round ", round
    for player, score in score:
        print "  Player {p}: {s}".format(p=player, s=score)

def get_throw(dart_num):
    enter_dart_msg = "  Dart {d} score: "
    dart = ""
    while True:
        dart = raw_input(enter_dart_msg.format(d=dart_num))
        if not dart:
            print "  Incorrect Input.  Try Again."
            continue
        elif dart.upper() == 'M':
            return dart
        elif re.search('^\d{1,2}$', dart) is not None:
            # only a number.  assume single
            if (0 < int(dart) < 21) or int(dart) == 25:
                return 'S'+dart
        elif re.search('^[STDstd]\d{1,2}$', dart ) is not None:
            # letter followed by a number
            if (0 < int(dart[1:]) < 21) or int(dart[1:]) == 25:
                return dart
        print "  Incorrect Input.  Try Again."


def play_game(rounds):
    for _ in xrange(1,rounds+1):
        print_score(_)
        for pKey, pVal in players.iteritems():
            start_msg = "Player {p}'s turn. Starting score = {s}"
            print start_msg.format(p=pKey, s=pVal.score)
            rnd = Round()
            dart = get_throw(1)
            rnd.dart1(DartThrow(dart))
            dart = get_throw(2)
            rnd.dart2_and_3(DartThrow(dart))
            dart = get_throw(3)
            rnd.dart3(DartThrow(dart))

            pVal.score += rnd.total


if __name__ == "__main__":
    numOfPlayers = int(raw_input("How many players?\n"))
    rounds = int(raw_input("How many rounds?\n"))

    outputStr = "We're going to play {rds} rounds with {numpl} players"
    print outputStr.format(numpl=numOfPlayers, rds=rounds)
    players = {}
    for _ in xrange(numOfPlayers):
        players[_] = Player()
    play_game(rounds)
    print "-------------"
    print_score('FINAL')
    print "-------------"
