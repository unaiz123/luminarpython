f=open("movies - Copy.csv","r")
dict={}

for lines in f:
    data=lines.rstrip("\n").split(",")
    year=data[2]
    rating=data[3]
    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1

print("Year Wise Movie Count :")
for k,v in dict.items():
    print(k ,":", v)
print(sorted(dict.items(),key=lambda  kv:kv[1]))

#...............Covid_Rating_Wise...................................#
#
# for lines in f:
#     data=lines.rstrip("\n").split(",")
#     year=data[2]
#     rating=data[3]
#     if(rating not in dict):
#         dict[rating]=1
#     else:
#         dict[rating]+=1
#
# print("Rating Wise Movie Count :")
# for k,v in dict.items():
#     print(k ,":", v)