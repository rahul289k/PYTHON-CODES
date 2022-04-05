x = [1,2,2,2,3,4,5,56,56,65,6,7,8,8,9]
new_list = []
for i in x:
    if i not in new_list:
        new_list.append(i)
print(new_list)



# using list comprehension
# x= [1,1,1,2,3,4,5,5,6,76,87,89,9]
# new_list = []
# y= [new_list.append(num) for num in x if num not in new_list]
# print(new_list)