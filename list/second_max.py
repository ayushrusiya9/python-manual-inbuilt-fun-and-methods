from length_list import list_length

def second_max(l):
    max_num1 = l[0]
    for i in l:
        if max_num1 < i:
            max_num1 = i
    max_num2 = None 
    
    for j in l:
        if max_num1 != j:
            if max_num2 is None or j > max_num2:
                max_num2 = j
    return max_num2

li = [1,2,1,2,1,2,5,4,2,6,7]
print(second_max(li))