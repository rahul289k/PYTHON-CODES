# python code to print prime numbers in givne range


def primefind(m,n):
    min_num = min(m,n)
    max_num = max(m,n)
    x = []
    for num in range(min_num,max_num+1):
        for j in range(2,int(((max_num)**0.5))+1):
            if num%j == 0:
                break
        else:
            x.append(num)
    return x
m = int(input())
n = int(input())
print(primefind(m,n))
