lst=[2,4,6]
olst=[]
total=sum(lst)
print("Totl :",total)
for element in lst:
    res=total-element
    olst.append(res)
print(olst)


