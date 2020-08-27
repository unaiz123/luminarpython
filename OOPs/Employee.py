import functools


class Employee:
    def __init__(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary

    def PrintVal(self):
        print("name ",self.name)
        print("dei ",self.desig)

    def __str__(self):
        return self.name
f=open("file","r")
lst=[]
for data in f:
    values=data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    desig=values[2]
    salary=values[3]
    obj=Employee(id,name,desig,salary)
    lst.append(obj)

upper=list(map(lambda i:i.name.upper(),lst))
update=list(map(lambda i:int(i.salary)+5000,lst))
greater=list(filter(lambda i:int(i.salary)>=25000,lst))
print("Upper case Conversion.........")
# for i in N:
print(upper)
print("Salary Incrementing...........")
# for i in update:
print(update)
print("Salary above 25000...........")
for i in greater:
    print(i)
salaries=list(map(lambda sal:sal.salary,lst))
print("Salaries : ",salaries)

maxVal=functools.reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,salaries)
print("Max Salary : ",maxVal)


maxsal=list(filter(lambda i:i.salary==maxVal,lst))
for emp in maxsal:
    print(emp)