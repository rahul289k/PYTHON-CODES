# /\/\/\/\/\/\/\/\/\/\/\/\/\/
# arrange numbers in a waveforms


x =  [3,5,12,2,6,10,7,9,8]
for i in range(0,len(x),2):
    if i>0 and x[i]<x[i-1]:
        x[i],x[i-1] = x[i-1],x[i]
    elif i<(len(x)-1) and x[i]<x[i+1]:
        x[i], x[i+1]= x[i+1], x[i]
print(x)
