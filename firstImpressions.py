
class Player:
    score = 0
    darts_thrown = 0
    marks = 0

    @property
    def mpr(self):
        return self.darts_thrown/self.marks


class Round:
    marker = -1
    missed_first = False
    missed_second = False
    total = 0

    def first_dart(self, points):
        if points == 0:
            self.missed_first = True
            return
        self.marker = points
        self.total += points

    def second_dart(self, points):
        if not points:
            # missed.  score will be determined by 3rd dart
            self.missed_second = True
            return

        if self.missed_first or points != self.marker:
            # missed first dart or missed marker-> negative second score
            self.total -= points
        else:
            # hit marker:  positive score
            self.total += points

    def third_dart(self, points):
        if self.missed_first and self.missed_second:
            # missed board on 1st and 2nd dart
            if points:
                # hit a number on 3rd
                # 3 * what you hit subtracted from total
                self.total -= 3 * points
            else:
                # missed all 3.  negative 200
                self.total -= 200
        elif self.missed_second:
            # missed board on 2nd dart, but not 1st
            if points == self.marker:
                # hit marker on 3rd.  No points
                return
            elif not points:
                # missed both 2nd and 3rd darts, -150
                self.total -= 150
            else:
                # hit wrong spot on 3rd, but hit board
                # -2 * what you hit on 3rd
                self.total -= 2 * points
        elif self.missed_first:
            # hit 2nd dart, but missed 1st
            if points:
                # hit board: subtract what you hit
                self.total -= points
            else:
                # missed board: subtract 50
                self.total -= 50
        else:
            # hit 1st and 2nd
            if not points:
                # miss board: -50
                self.total -= 50
            elif points == self.marker:
                # hit marker:  add points
                self.total += points
            else:
                # missed marker:  subtract points
                self.total -= points



def print_score(round):
    score = [(x, y.score) for x, y in players.iteritems()]
    print "Round ", round
    for player, score in score:
        print "  Player {p}: {s}".format(p=player, s=score)

def play_game(rounds):
    for _ in xrange(1,rounds+1):
        print_score(_)
        for pKey, pVal in players.iteritems():
            start_msg = "Player {p}'s turn. Starting score = {s}"
            print start_msg.format(p=pKey, s=pVal.score)
            enter_dart_msg = "  Dart {d} score: "
            rnd = Round()
            dart = int(raw_input(enter_dart_msg.format(d=1)))
            rnd.first_dart(dart)
            dart = int(raw_input(enter_dart_msg.format(d=2)))
            rnd.second_dart(dart)
            dart = int(raw_input(enter_dart_msg.format(d=3)))
            rnd.third_dart(dart)

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
