word="hello hai hello hai"
worsplit=word.split(" ")
print(worsplit)
dict={}

for i in worsplit:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)