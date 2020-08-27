a=["anu","vinu","appu","amulya","asha"]
b=["anu","amulya"]
passed=[]
for x in b:
    for y in a:
        if x == y :
            passed.append(a.index(y))
print(passed)