ages={"unaiz":27,"rahmath":19,"saeed":33,"Amina":18,"salahudheen":15,"ashraf":50,"aysha":48}

for k,v in ages.items():
    print(k,":",v)

new=sorted(ages.items(),key=lambda xv:(xv[1],xv[0]))
print(new)