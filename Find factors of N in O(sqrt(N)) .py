
# Find all divisors of N in O(sqrt(N)) time


x = int(input())
y = []
z = []
for i in range(1,int(x**0.5)+1):
    if x%i ==0:
        y.append(i)
        z.append(x//i)
print(y+z[::-1])
