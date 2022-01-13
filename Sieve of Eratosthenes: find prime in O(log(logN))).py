x = int(input())
y = [0]*(x+1)
y[0],y[1] = 1,1
for i in range(2,int(x**0.5)+1):
    if y[i] == 0:
        for j in range(i*i,x+1,i):
            y[j] = 1
for i in range(len(y)):
    if y[i]==0:
        print(i)

