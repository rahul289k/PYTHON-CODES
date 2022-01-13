# selection sort algorithm

def selectiosort(arr):
    for i in range(len(arr)-1,0,-1):
        pos = 0
        for j in range(1,i+1):
            if arr[j]>arr[pos]:
                pos = j
        temp = arr[i]
        arr[i] = arr[pos]
        arr[pos] = temp
arr = [4,7,54343,56,67,67,46,34,2]
selectiosort(arr)
print(arr)
