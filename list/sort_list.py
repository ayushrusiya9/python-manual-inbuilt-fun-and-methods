from length_list import list_length

def sort_list(l):
    n = list_length(l)
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]
    return l

li = [3,5,1,2,3,85,33]
print(sort_list(li))