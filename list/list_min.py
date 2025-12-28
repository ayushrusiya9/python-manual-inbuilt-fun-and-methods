def list_min(l):
    min_num = l[0]
    for num in l:
        if min_num > num:
            min_num = num
    return min_num

li = [1,2,3,4,5]
print(list_min(li))