def list_max(l):
    max_num = l[0]
    for num in l:
        if max_num < num:
            max_num = num
    return max_num

li = [1,2,3,4,5]
print(list_max(li))
            