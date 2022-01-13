# find number of consecutive number in a list


x = [1,2,3,4,5,56,74,83,93,65]
c = 1
for i in range(len(x)):
    if x[i]+1 in x:
        c+=1
print(c)
