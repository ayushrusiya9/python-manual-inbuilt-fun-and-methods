def list_length(l):
    count = 0
    for _ in l:
        count += 1
    return count

li = [1,2,3,4,5]
print(list_length(li))