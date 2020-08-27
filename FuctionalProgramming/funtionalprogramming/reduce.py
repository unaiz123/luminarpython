import functools


lst=[10,9,3,20,90,120,1500,30,40,50]

total=functools.reduce(lambda num1,num2:num1+num2,lst)
print("Total : ",total)

max=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2 ,lst)
print("Max : ",max)

minValue=functools.reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print("Min : ",minValue)