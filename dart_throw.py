import re


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
        d = input(enter_dart_msg.format(d=dart_num))
        dart = parse_dart_input(d)
        if not dart:
            print("  Invalid Input.  Try Again")
    return dart