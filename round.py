class Round:
    marker = -1
    missed_first = False
    total = 0
    MISS_COST = 50

    def _get_score(self, multiplier, bed):
        return {'S':1, 'D':2, 'T':3}[multiplier.upper()] * bed

    def dart1(self, throw):
        if throw.missed:
            self.total -= self.MISS_COST
            self.missed_first = True
            return
        self.marker = throw.bed
        self.total += throw.score

    def dart2_and_3(self, throw):
        if throw.missed:
            # missed.  score will be determined by 3rd dart
            self.total -= self.MISS_COST
        elif self.missed_first or throw.bed != self.marker:
            # missed first dart or missed marker-> negative second score
            self.total -= throw.score
        else:
            # hit marker:  positive score
            self.total += throw.score
