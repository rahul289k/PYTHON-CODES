x = [9,7,5,4,3,2,2,4,56]
for i in range(1,len(x)):
    a = x[i]
    j = i-1
    while j >=0 and a < x[j]:
        x[j+1] = x[j]
        j-=1
    x[j+1] = a
print(x)
