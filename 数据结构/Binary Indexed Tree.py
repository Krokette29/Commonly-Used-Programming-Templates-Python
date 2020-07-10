class BinaryIndexedTree:
    def __init__(self, length):
        self.c = [0] * length

    def lowBit(self, x):
        return x & (-x)
    
    def update(self, pos, value=1):
        while pos < len(self.c):
            self.c[pos] += value
            pos += self.lowBit(pos)
    
    def query(self, pos):
        ans = 0
        while pos > 0:
            ans += self.c[pos]
            pos -= self.lowBit(pos)
        return ans