# finding duplicates in a given list

lst = [1,1,2,3,3,3,4,5,7,8]
duplic, seen = set(), set()
for i in lst:
    if i not in seen:
        seen.add(i)
    else:
        duplic.add(i)
print(duplic)
print(seen)
