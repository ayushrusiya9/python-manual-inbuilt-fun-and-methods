def to_upper_case(s):
    result =''
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result

a = 'ayush'
print(to_upper_case(a))