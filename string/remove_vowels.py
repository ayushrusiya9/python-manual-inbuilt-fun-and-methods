def remove_vowels(s):
    result = ''
    for ch in s:
        if ch not in 'aeiouAEIOU':
            result += ch
    return result

a = 'ayush'
print(remove_vowels(a))