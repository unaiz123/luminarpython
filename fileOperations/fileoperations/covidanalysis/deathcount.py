f=open("covid_19_india.csv","r")
dict={}
clist=[]

for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    confirm=data[8]
    if(state not in dict):

        dict[state]=confirm
    else:

        dict[state] = confirm

for k,v in dict.items():
    clist.append(int(v))

for k,v in dict.items():
    if(max(clist)==int(v)):
        print("\n Confirmed : ",k,v)
