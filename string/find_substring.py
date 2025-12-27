from length_func import length_checker

# def find_substring(s, sub):
#     n = length_checker(s)
#     m = length_checker(sub)
#     for i in range(n - m + 1):
#         match = True
#         for j in range(m):
#             if s[i + j] != sub[j]:
#                 match = False
#                 break
#             else:
#                 return i

#     return -1

def find_substring(s, sub):
    if sub in s:
        return True
    else:
        return False

a = 'ayush'
# b = "ayu"
b = 'rus'
print(find_substring(a,b))