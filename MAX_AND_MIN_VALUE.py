# find max min from a array /list

x = [1,2,3,5,2,2,-1,2,3,4,3,278]
mx = -100000000
mi = 100000000
for i in range(len(x)):
    if x[i]>mx:
        mx = x[i]
    if x[i]<mi:
        mi = x[i]
print("maximum value  = ", mx)
print("minimum value  = ", mi)
