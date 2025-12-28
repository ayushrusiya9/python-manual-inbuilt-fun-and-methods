def count_occurance(l, target):
    count = 0
    for item in l:
        if target == item:
            count += 1
    return count

li = [1,2,2,2,3,3,4,4]
print(count_occurance(li, 2))
print(count_occurance(li, 1))