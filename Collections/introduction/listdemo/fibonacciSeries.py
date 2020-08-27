num=int(input("enter the no of numbers in series : "))
fno=0
sno=1
count=0
while(count<num):
    print(fno)
    res=fno+sno
    fno=sno
    sno=res
    count+=1
