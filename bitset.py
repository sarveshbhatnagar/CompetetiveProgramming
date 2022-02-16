class Bitset:

    def __init__(self, size: int):
        self.bits = set()
        self.notBits = set([i for i in range(size)])
        self.size = size

    def fix(self, idx: int) -> None:
        if(idx < self.size):
            if(idx in self.notBits):
                self.notBits.remove(idx)
            self.bits.add(idx)

    def unfix(self, idx: int) -> None:
        if(idx < self.size):
            if idx in self.bits:
                self.bits.remove(idx)
            self.notBits.add(idx)

    def flip(self) -> None:
        t = self.bits
        self.bits = self.notBits
        self.notBits = t

    def all(self) -> bool:
        return len(self.bits) == self.size

    def one(self) -> bool:
        return len(self.bits) >= 1

    def count(self) -> int:
        return len(self.bits)

    def toString(self) -> str:
        a = ["0"] * self.size
        for i in self.bits:
            a[i] = "1"
        return "".join(a)
