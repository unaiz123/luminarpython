from re import *
lst=[]
lst2=[]
f=open("regno","r")

rule='[Kk][Ll][0-9]{2}[a-z]{1,2}\d{4}'

for i in f:
    regno=i.rstrip("\n")
    matcher = fullmatch(rule, regno)

    if matcher !=None :
        lst.append(regno)
    else:
        lst2.append(regno)

f1=open("invalid","w")
for i in lst:

    f1.write("%s\n" % i)

f1=open("invalid","r")
for i in f1:
    print(i)


print("Valid Reg No:",lst)
print("Invalid Reg No:",lst2)