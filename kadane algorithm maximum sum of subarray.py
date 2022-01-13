# kadane algorithm maximum sum of subarray


x = [-2, -5, 6, -2, -3, 1, 5, -6]
sum= 0
sum_so_far = x[0]
for i in range(len(x)):
    sum +=x[i]
    if sum_so_far< sum:
        sum_so_far = sum
    if sum < 0:
        sum =0
print(sum_so_far)
