
def popa(x):
    return x+1
class pisya():
    def __init__(self, popa):
        self.count = popa
    def print(self):
        print(self.count)
pisya1 = pisya(popa(121231231))
pisya1.print()