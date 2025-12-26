def space_remover(s):
    result = ''
    for ch in s:
        # if ch != ' ':
        if ord(ch) != 32:
            result += ch
    return result

a = 'ayush rusiya'
print(space_remover(a))

