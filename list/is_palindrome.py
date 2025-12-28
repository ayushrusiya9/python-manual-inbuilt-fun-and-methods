from length_list import list_length

def is_palindrome(l):
    n = list_length(l)
    for i in range(n // 2):
        if l[i] != l[n - i -1]:
            return False
    return True

li = [1,2,1]
print(is_palindrome(li))