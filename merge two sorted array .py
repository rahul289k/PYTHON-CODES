a = [2,3,4,5,6,7]
b = [8,9,10,11,12,13,14,15]
x = len(a)
y = len(b)
lst = []
i=0
j=0

while i< x and j< y:
    if a[i]<b[j]:
        lst.append(a[i])
        i+=1
    else:
        lst.append(b[j])
        j+=1
while i <x:
    lst.append(a[i])
    i+=1
while j < y:
    lst.append(b[j])
    j+=1
print(lst)
