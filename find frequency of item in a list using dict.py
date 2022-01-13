# find frequency of item in a list using dict


x = [1,2,3,4,4,4,5,6,7,7,8]
dict = {}
for key in x:
    if key in dict:
        dict[key]+=1
    else:
        dict[key]=1
print(dict)

