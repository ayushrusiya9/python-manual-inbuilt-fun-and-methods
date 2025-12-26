def count_char(s, target):
    c = 0
    for i in s:
        if target == i:
            c += 1
    return c

a = 'aaayush'
print(count_char(a,'a'))