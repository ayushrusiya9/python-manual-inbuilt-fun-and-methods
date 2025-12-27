def replace_char(s, old, new):
    result = ''
    for ch in s:
        if ch == old:
            result += new
        else:
            result += ch
    return result

a = "ayush"
print(replace_char(a,'a','p'))