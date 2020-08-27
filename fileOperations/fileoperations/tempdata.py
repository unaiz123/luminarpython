f=open("tempdata","r")
dict={}

for lines in f:
    data=lines.rstrip("\n").split(",")
    dist=data[0]
    temp=data[1]
    if (dist not in dict):
        dict[dist]=temp
    else:
        old=dict[dist]
        if temp>old:
            dict[dist]=temp
print(dict)