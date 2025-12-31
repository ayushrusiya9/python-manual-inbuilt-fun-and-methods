class A:
    __x =10
    def __xyz(self):
        print('private method')

class B(A):
    pass

obj = B()
# print(obj.__x)
# print(obj.__xyz())
# print(obj._A__xyz())
print(obj._A__x)
print(dir(A))
