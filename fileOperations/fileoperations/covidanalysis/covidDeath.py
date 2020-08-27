f=open("covid_19_india.csv","r")
dict={}

for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    death=data[7]
    if(state not in dict):
        dict[state]=death
    else:
        dict[state]=death
for k,v in dict.items():
    print(k,":",v)

sum=0
for j in dict.values():
    sum=sum+int(j)
print("Total no of Death in India :",sum)
