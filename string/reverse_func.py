from length_func import length_checker

def reverse_string(s):
    s1 = ''
    for i in range(length_checker(s) - 1, -1 , -1):
        s1 += s[i]
    return s1

a = "ayush"
print(reverse_string(a))
    