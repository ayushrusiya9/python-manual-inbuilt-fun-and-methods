def get_unique_char(s):
    result = ''
    for ch in s:
        exist = False
        for r in result:
            if ch == r:
                exist = True
                break
        if not exist:
            result += ch
    return result

a = 'aayush'
print(get_unique_char(a))