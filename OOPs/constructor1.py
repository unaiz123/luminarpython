# class Employee():
#     def __init__(self,id,name,des):
#         self.id=id
#         self.name=name
#         self.des=des
#     def printEmployee(self):
#         print(self.id)
#         print(self.name)
#         print(self.des)
# # emp=Employee(1001,"unaiz","developer")
# # emp.printEmployee()
# #
# # emp1=Employee(1002,"shefin","Android developer")
# # emp1.printEmployee()
#
# # f=open("file","r")
#
# # for employees in f:
# #     data=employees.split(",")
#
# id=input("enter the id ")
# name=input("enter the name ")
# des=input("enter the des ")
# emp=Employee(id,name,des)
# emp.printEmployee()





class Employee():

    def __init__(self,id,name,des,salary):
        self.id=id
        self.name=name
        self.des=des
        self.salary=salary
    def prinyDetaile(self):
        print("The Employee Details :")
        print(self.id)
        print(self.name)
        print(self.des)
        print(self.salary)
n=0
while(n!=1):
    id=int(input("enter id : "))
    name=input("enter name : ")
    des=input("enter designation : ")
    salary=int(input("enter salary : "))

    obj=Employee(id,name,des,salary)
    obj.prinyDetaile()
    n=int(input("if Exit...pres 1"))

