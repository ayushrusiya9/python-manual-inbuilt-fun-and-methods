def merge_list(l1, l2):
    m = []
    for i in l1:
        m.append(i)
    for j in l2:
        m.append(j)
    return m

li = [1,2,3,4]
li2 = [5,6,7,8]
print(merge_list(li,li2))