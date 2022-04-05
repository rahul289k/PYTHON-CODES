def strcheck(val):
    flag = 0
    for i in range(len(val)):
        if val.count(val[i])>1:
            flag = 1
    if flag ==1:
        return 'duplicate present'
    else:
        return "duplicate absent"


val = str(input())
print(strcheck(val))
# x = 'hello'
# print(x.count('l'))