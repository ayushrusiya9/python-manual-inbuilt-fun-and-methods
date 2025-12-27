def capitalize_first_letter(s):
    result = ''
    capitalize = True
    for c in s:
        if c == ' ':
            result += c
            capitalize = True
        elif capitalize and 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
            capitalize = False
        else:
            result += c
            capitalize = False
    return result

a = 'python is best language.'
print(capitalize_first_letter(a))