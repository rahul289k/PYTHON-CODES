# Linear search
def linaer(arr):
    for i in range(len(arr)):
        if target == arr[i]:
            return f"element is at index {i}"
    else:
        return "element not found"
arr=[1,2,3,4,5,6,7,8,9,11,15,13]
target = int(input())
print(linaer(arr))
