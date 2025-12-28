def remove_duplicate(l):
    unique = []
    for item in l:
        if item not in unique:
            unique.append(item)
    return unique

l = [1,1,1,2,3,4,1,2]
print(remove_duplicate(l))