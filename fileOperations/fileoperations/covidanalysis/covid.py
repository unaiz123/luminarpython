import operator
f=open("covid_19_india.csv","r")
dict={}
cases=[]

for lines in f:

    data=lines.rstrip("\n").split(",")
    state=data[3]
    case=data[8]

    if (state not in dict):
        dict[state]=case
    else:
        dict[state] = case


for k,v in dict.items():
    print(k,":",v)


    sum=0
for j in dict.values():
    sum=sum+int(j)
print("Total No of Cases in India : ",sum)













