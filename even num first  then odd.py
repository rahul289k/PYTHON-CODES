def even_first(arr):

    a = 0
    b = len(arr)-1
    while a < b:
        #  checking if even form beggining
        if arr[a] %2 ==0:
            #  if even keep moving
            a+=1
        else:
            # else swap odd num with num in end of arr

            arr[a],arr[b] = arr[b],arr[a]
            b-=1

    return arr


arr = [1,2,3,4,5,6,7,8,9]

print(even_first(arr))
