strng="ABABABCAAA"
print(strng)
dict={}

for i in strng:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
freq=max(dict,key=dict.get)
print(freq)