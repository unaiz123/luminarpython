list=[10,25,44,22,15,32,30]
print(list)
element=int(input("enter element to find"))
flag=0
for i in list:
    if(i==element):
        flag=1
        break
    else:
        flag=0

if(flag>0):
    print("element found")
else:
    print("elementnot found")