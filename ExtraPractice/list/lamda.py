def mul(x):
    return lambda y:x*y
result=mul(5)
print(result(4))