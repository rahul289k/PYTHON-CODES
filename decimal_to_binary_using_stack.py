# decimal to binary using stack data structure
class Stack:
    def __init__(self):
        self.items = []
    def isempty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
def decito(num):
    sobj = Stack()
    while num>0:
        rem = num%2
        sobj.push(rem)
        num = num//2
    st = ""
    while not sobj.isempty():
        st += str(sobj.pop())
    return st
print(decito(10))
