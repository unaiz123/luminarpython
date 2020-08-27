lst=["x","y","z"]
print(lst)
lst1=[]
lstlength=len(lst)
num=lstlength-1
for i in range(0,num):
    pair=lst[i],lst[i+1]

    if pair not in lst1:
        lst1.append(pair)
    # print(pair)
    pair2=lst[0],lst1(num)
    if pair2 not in lst1:

        lst1.append(pair2)
print(lst1)