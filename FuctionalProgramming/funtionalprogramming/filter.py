import functools
list1=[10,20,35,43,22,33,21,70,1110,30,11,25,]
print("List is :",list1)
# even=list(filter(lambda x:x % 2 ==0,list1))
# print("Even : ",even)

even=list(filter(lambda x: x>25,list1))
print(even)
even=(functools.reduce(lambda x,y:x  if x>y else y,list1))
print(even)