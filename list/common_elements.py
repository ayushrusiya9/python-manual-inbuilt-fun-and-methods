def common_elements(lst1, lst2):
    common = []
    for i in lst1:
        for j in lst2:
            if i == j:
                already_added = False
                for k in common:
                    if k == i:
                        already_added = True
                if not already_added:
                    common.append(i)
    return common

l = [1,2,1,1]
l2 = [1,2,1,3]
print(common_elements(l,l2))