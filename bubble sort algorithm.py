x= [9,7,6,5,4,3,2,2]
for i in range(len(x)-1):
    for j in range(len(x)-1):
        if x[j]>x[j+1]:
            x[j+1],x[j] = x[j],x[j+1]
print(x)
