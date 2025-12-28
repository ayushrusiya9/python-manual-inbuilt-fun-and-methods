from length_list import list_length

def reverse_list(l):
    revrsed_list = []
    for index in range(list_length(l) - 1,-1,-1):
        revrsed_list.append(l[index])
    return revrsed_list

li = [1,2,4,5,5]
print(reverse_list(li))