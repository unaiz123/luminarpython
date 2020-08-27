f1=open("words","r")
data=f1.readlines()
f2=open("new","w")

data1=data[::-1]
for i in data1:
    print(i)
f2.writelines(data1)
