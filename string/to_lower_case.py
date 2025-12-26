def to_lower_case(s):
    result = ''
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

a = 'AYUSH'
print(to_lower_case(a))
