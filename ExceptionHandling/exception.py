num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
lst=[1,2,4,10,25]
try:

    result=num1/num2
    print("Result : ",result)

except Exception as e:
    print(e.args)

try:
    pos = print(int(input("enter index")))
    print(lst[pos])

except Exception as e:
    print(e.args)

finally:

    print("Num1 : ",num1)
    print("Num1 : ", num2)
    print("Suuccess....")

