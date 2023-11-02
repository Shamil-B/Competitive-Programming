class Bitset:

    def __init__(self, size: int):
        self.bitset = [0] * size
        self.zeros = set([i for i in range(size)])
        self.ones = set()

    def fix(self, idx: int) -> None:
        self.bitset[idx] = 1
        if idx in self.zeros:
            self.zeros.remove(idx)

        self.ones.add(idx)

    def unfix(self, idx: int) -> None:
        self.bitset[idx] = 0
        if idx in self.ones:
            self.ones.remove(idx)

        self.zeros.add(idx)

    def flip(self) -> None:
        self.ones, self.zeros = self.zeros, self.ones

    def all(self) -> bool:
        return len(self.ones) == len(self.bitset)

    def one(self) -> bool:
        return len(self.ones) > 0

    def count(self) -> int:
        return len(self.ones)

    def toString(self) -> str:
        s = ""
        for i in range(len(self.bitset)):
            if i in self.zeros:
                s += "0"
            else:
                s += "1"
        return s


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()