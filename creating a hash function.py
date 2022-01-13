# hash function

class Myhash:
    def __init__(self,s):
        self.s = s
        self.table  = [[] for x in range(s)]
    def insert(self,a):
        i = a%self.s
        self.table[i].append(a)
    def delete(self,b):
        i = b%self.s
        self.table[i].remove(b)
    def search(self,c):
        i = c%self.s
        return c in self.table[i]
o = Myhash(7)
o.insert(1)
o.insert(2)
o.insert(3)
o.insert(4)
o.insert(5)
o.insert(6)
o.insert(7)
x = o.search(4)
print(x)
