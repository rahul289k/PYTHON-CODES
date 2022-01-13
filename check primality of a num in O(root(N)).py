
def checkprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

t= int(input())
while t:
    n = int(input())
    print(checkprime(n))
    t = t-1
