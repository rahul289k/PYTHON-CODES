
#  binary search in python
x = [1,2,3,4,5,6,7,8,9,12,13,14]
target = 7
low = 0
high =len(x)-1
mid =0

while low<=high:
    mid = (low + high) // 2
    if target > x[mid]:
        low = mid+1
    if target < x[mid]:
        high = mid-1
    if target == x[mid]:
        print(mid)
        break
