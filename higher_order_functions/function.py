def test(a, b):
    return a + b , a * b

t =test(2,4)
print(type(t))
# when return single value they give int if return multiple value thay give tuple.