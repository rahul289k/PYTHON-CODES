x= [7,8,9,10,11,12,1,2,3,4,5,6]
mid = 5
low =0
high = 11
a= x[low:mid+1]
b = x[mid+1:high+1]
i,j=0,0
k = low
while i < len(a) and j < len(b):
    if a[i]< b[j]:
        x[k] = a[i]
        k+=1
        i+=1
    else:
        x[k] = b[j]
        k+=1
        j+=1
while i < len(a):
    x[k] = a[i]
    i+=1
    k+=1
while j < (len(b)):
    x[k] = b[j]
    k+=1
    j+=1
print(x)


# output:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
