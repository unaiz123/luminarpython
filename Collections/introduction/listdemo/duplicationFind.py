lst=[1,1,1,2,2,2,10,10,20,20,30,31,31,15,12,12,9,7]
lst.sort()
slst=[]
print(lst)
for i in lst:
    if i not  in slst:
        slst.append(i)

print(slst)



