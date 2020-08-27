lst=[10,11,12,13,15,2,3,5,6]
lst.sort()
print(lst)
low=0
upp=len(lst)-1
element=int(input("enter found element : "))
flg=0
while(low<=upp):
    mid=(low+upp)//2

    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flg+=1
        break

if(flg>0):
    print("element found")
else:
    print("not found")