class Slice(object):
    def __init__(self, value):
        self.value = value

    @property
    def triple(self):
        return self.value * 3

    @property
    def double(self):
        return self.value * 3


class Board(object):
    def __init__(self):
        self.one = Slice(1)
        self.two = Slice(2)
        self.three = Slice(3)
        self.four = Slice(4)
        self.five = Slice(5)
        self.six = Slice(6)
        self.seven = Slice(7)
        self.eight = Slice(8)
        self.nine = Slice(9)
        self.ten = Slice(10)
        self.eleven = Slice(11)
        self.twelve = Slice(12)
        self.thirteen = Slice(13)
        self.fourteen = Slice(14)
        self.fifteen = Slice(15)
        self.sixteen = Slice(16)
        self.seventeen = Slice(17)
        self.eighteen = Slice(18)
        self.nineteen = Slice(19)
        self.twenty = Slice(20)
        self.bullseye = Slice(50)

        self.layout = [self.twenty, self.one, self.eighteen, self.four,
                       self.thirteen, self.six, self.ten, self.fifteen,
                       self.two, self.seventeen, self.three, self.nineteen,
                       self.seven, self.sixteen, self.eight, self.eleven,
                       self.fourteen, self.nine, self.twelve, self.five]

    def is_adjacent(self, value):
        return True
