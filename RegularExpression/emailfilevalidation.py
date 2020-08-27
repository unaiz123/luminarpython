from re import  *
lst=[]
lst1=[]
f1=open("email","r")
rule="\w*[@]gmail[.]com"

for i in f1:
    data=i.rstrip("\n")
    matcher=fullmatch(rule,data)

    if matcher!=None:
        lst.append(data)

    else:
        lst1.append(data)

f2=open("emailinvalid","w")

for i in lst:
    f2.write("%s\n" % i)
f2=open("emailinvalid","r")

for i in f2:
    print(i)


print(lst)
print(lst1)