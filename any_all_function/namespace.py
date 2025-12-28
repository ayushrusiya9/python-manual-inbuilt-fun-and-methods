# namespace
# 1. locals
# 2. globals
# 3. builtin

import builtins

x = 10
y = 15
z = 20
def first():
    x = 1
    y = 2
    z = 3
    print(locals())

first()
# print(globals())

# print(dir(builtins))

# scope -  local/global/nonlocal
# non local 
x = 10 # global
def outer_fun():
    # print(x)
    # nonlocal x -> error dega kyuki ye local hai 
    x = 20 # local
    def inner_fun():
        nonlocal x # ye nested function ki condition ma lagega 
        x = 30 # non local

    inner_fun()
    print(x)

outer_fun()
