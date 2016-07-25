import re

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


class Round:
    marker = -1
    missed_first = False
    missed_second = False
    total = 0

    def _get_score(self, multiplier, bed):
        return {'S':1, 'D':2, 'T':3}[multiplier.upper()] * bed

    def first_dart(self, throw):
        if throw.missed:
            self.missed_first = True
            return
        self.marker = throw.bed
        self.total += throw.score

    def second_dart(self, throw):
        if throw.missed:
            # missed.  score will be determined by 3rd dart
            self.missed_second = True
            return

        if self.missed_first or throw.bed != self.marker:
            # missed first dart or missed marker-> negative second score
            self.total -= throw.score
        else:
            # hit marker:  positive score
            self.total += throw.score

    def third_dart(self, throw):
        if self.missed_first and self.missed_second:
            # missed board on 1st and 2nd dart
            if not throw.missed:
                # hit a number on 3rd
                # 3 * what you hit subtracted from total
                self.total -= 3 * throw.score
            else:
                # missed all 3.  negative 200
                self.total -= 200
        elif self.missed_second:
            # missed board on 2nd dart, but not 1st
            if throw.bed == self.marker:
                # hit marker on 3rd.  No points
                return
            elif throw.missed:
                # missed both 2nd and 3rd darts, -150
                self.total -= 150
            else:
                # hit wrong spot on 3rd, but hit board
                # -2 * what you hit on 3rd
                self.total -= 2 * throw.score
        elif self.missed_first:
            # hit 2nd dart, but missed 1st
            if throw.missed:
                # missed board: subtract 50
                self.total -= 50
            else:
                # hit board: subtract what you hit
                self.total -= throw.score
        else:
            # hit 1st and 2nd
            if throw.missed:
                # miss board: -50
                self.total -= 50
            elif throw.bed == self.marker:
                # hit marker:  add points
                self.total += throw.score
            else:
                # missed marker:  subtract points
                self.total -= throw.score


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
            rnd.first_dart(DartThrow(dart))
            dart = get_throw(2)
            rnd.second_dart(DartThrow(dart))
            dart = get_throw(3)
            rnd.third_dart(DartThrow(dart))

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
