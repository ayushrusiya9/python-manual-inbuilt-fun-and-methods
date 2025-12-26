from length_func import length_checker

def is_palindrome(s):
    n = str(s)
    n = length_checker(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

a = '1221'
if is_palindrome(a):
    print('Plaindrome')
else:
    print('Not Palindrome')


