import sys

a = [1,2,3]
b = (1,2,3)

print(sys.getsizeof(a))
print(sys.getsizeof(b))

s = "eulogik"

r = lambda func:func.upper()

print(r(s))

p = [1,2,3,4,5]

q = [val ** 2 for val in p]

print(q)

def fun(**kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))


# Driver code
fun(s1='Geeks', s2='for', s3='Geeks')

class Test:
    pass

print(dir(Test))

from array import array

ar = array("i",[1,2,3,4])
print(ar)

j = range(1,10)
print(j)

key = ['a','b','c']
value = [1,2,3]

keyValue = {k:v for k,v in zip(key,value)}
print(keyValue)
print(zip(key,value))