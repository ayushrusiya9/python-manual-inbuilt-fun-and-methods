#abstract class 
#-> jab hogi ye abstaract clas jab isme ABC inherit ho or, isme abstract methods hot.

# Encapsulation 
# -> access specifier/modifier
# -> variable/properties
# -> methods/behaviours methdo
# public -> x= 10/ def xyz():, chid me access ker skte hai, outside bhi
# protect -> _x = 10/def _xyz():, child class ma acess ker skte hai, outside nhi but python ma possible hi
# private -> __X = 10/ def __xyz():, na to bahar na toh chil ma

# name mangling -> _CLASSNAME__PRIVATEVARIABLE/METHOD
from test import A
class C(A):
    pass

# print(dir(A))
print(C()._A__xyz())