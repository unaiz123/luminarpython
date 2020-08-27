lst=["apple","grape","cherry","guava"]
print(lst)
if "cherry" in lst:
    lst.append("yes")
print(lst)
lst.insert(3,"UNAIZ")
print(lst)
del lst[3]
print(lst)
mylist=lst.copy()
print("mylist : ",mylist)
