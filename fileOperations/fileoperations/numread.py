f=open("data","r")
lst=[]
even=[]
odd=[]
for num in f:
    lst.append(int(num.rstrip("\n")))
for i in lst:
    if((i%2)==0):
        even.append(i)
    else:
        odd.append(i)
print("List :",lst)
print("Even : ",even)
print("Odd : ",odd)


